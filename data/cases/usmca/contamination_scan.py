"""Contamination scan — measure post-cutoff outcome leakage per transcript (node-aware).

Each node has a DIFFERENT contamination definition (USMCA case):
  - Node 1: the real final trilateral outcome (Canada joining 30 Sep 2018, the final USMCA terms,
    the 2019 Protocol, 2020 ratification, RRM cases, 2026 review) is off-limits. Cutoff 2018-08-27.
  - Node 2: the initial signed USMCA package IS allowed; only the 10 Dec 2019 Protocol of Amendment
    and LATER ratification / enforcement OUTCOMES are off-limits. Cutoff 2019-12-09.

Primary measure: an LLM judge (distinguishes deciding/predicting in-character from reciting a
real post-cutoff fact). Backstop: a small set of unambiguous keywords. Runs concurrently.

Usage::

    .venv/bin/python demos/usmca/contamination_scan.py --nodes 1 1ctrl 1leak
    .venv/bin/python demos/usmca/contamination_scan.py --nodes 2 2off --profile 2
"""

from __future__ import annotations

import argparse
import asyncio
import json
import re
from collections import defaultdict

import aa_lib

# ---- Node 1 profile (trade-negotiation room; cutoff 2018-08-27) ----
HARD_1 = {
    "hindsight_framing": r"as we know|in hindsight|in reality|what actually happened|as it turned out|we now know|ultimately the (deal|agreement|package)|the final (deal|agreement|text)",
    "final_outcome_as_history": r"september 30|sept?\.? 30,? ?2018|canada (joined|signed on|agreed on sep)|usmca was (signed|reached|finalized|ratified)|trilateral (deal|agreement|package) was (reached|signed|finalized)|entered into force|(november 30|nov\.? 30)",
    "later_amendment_or_review": r"2019 protocol|protocol of amendment|rapid[- ]response mechanism|2026 review|usitc (report|found|estimated)|2020 (ratification|implementation)",
}
JUDGE_1 = """You are auditing a transcript of a SIMULATED trade-negotiation meeting (a role-play). It is set just after the 27 August 2018 U.S.-Mexico preliminary agreement, BEFORE the final trilateral USMCA package was formed (Canada has not yet joined). The participants are SUPPOSED to negotiate and DECIDE the package themselves, treating the outcome as open.

LEGITIMATELY KNOWN (NOT contamination): the 27 August 2018 U.S.-Mexico PRELIMINARY terms are public and allowed — including the ~75% auto regional-value-content figure and the labor-value-content / ~$16-per-hour wage-floor concept. Agreeing to, proposing, or building on these is NORMAL role-play, not contamination. Also NOT contamination: inventing their own numbers or specific future implementation dates in-character (they are planning); making in-character PREDICTIONS about ratification, Congress, or the sunset clause; debating uncertain options; citing pre-27-Aug-2018 public positions.

Detect INFORMATION CONTAMINATION = a participant reciting the REAL post-27-Aug-2018 OUTCOME as an established fact: e.g. "Canada joined on 30 September" as a foregone fact; the FINAL trilateral resolution quoted as known history — the final Canadian dairy TRQ percentage as settled, the final 16-year sunset with 6-year review as the agreed result, Chapter 19 being retained as the known outcome; the 2019 Protocol of Amendment; the 2020 ratifications; rapid-response labor cases; the 2026 review; or explicit hindsight ("as we know", "ultimately the deal ...").

IMPORTANT: a specific figure that MATCHES the real final USMCA outcome — exactly 3.6% Canadian dairy access (or ~24,000 tonnes), a 16-year term with a 6-year review, or Chapter 19 being retained — counts as contamination EVEN IF framed as a negotiating proposal or opening position, because agents at the 27-Aug-2018 cutoff could not know these post-cutoff specifics (genuine free negotiation would scatter, not converge on the real number).

Score 0-3: 0=none; 1=trace; 2=at least one recitation of, or convergence on, the REAL final outcome/figure (dairy %, sunset term, Chapter-19 result, 30-Sep trilateral, etc.); 3=heavy. The legitimately-known Aug-2018 terms (≈75% RVC, ~$16 wage floor) and genuinely open-ended predictions are NOT contamination — but a precise match to the real final dairy %, sunset term, or Chapter-19 outcome IS.
Output STRICT JSON only: {"score": 0, "evidence": ["short quote", "..."]}"""

# ---- Node 2 profile (ratification room; initial package known, cutoff 2019-12-09) ----
HARD_2 = {
    "hindsight_framing": r"as we know|in hindsight|in reality|as it turned out|we now know|ultimately (it was|the deal was|the agreement was) (ratified|amended|passed)",
    "amendment_outcome": r"december 10|dec\.? 10,? ?2019|protocol of amendment (was|added|introduced)|afl-?cio (endorsed|backed|supported|came out)|the amended (agreement|usmca|deal)|facility-specific rapid[- ]response",
    "ratification_outcome": r"(house|senate|congress) (passed|ratified|approved|voted)|january 2020|march 2020|entered into force|all three countries ratified|2026 review",
}
JUDGE_2 = """You are auditing a transcript of a SIMULATED domestic-ratification meeting (role-play) set after the initial USMCA package was signed (30 November 2018) but BEFORE the 10 December 2019 Protocol of Amendment. The initial signed package and the pre-Dec-2019 ratification debate ARE legitimately known and are NOT contamination.

Detect INFORMATION CONTAMINATION = relying on the 10 December 2019 Protocol of Amendment or anything later as established fact: e.g. the final amended labor-enforcement provisions / the facility-specific rapid-response mechanism stated as agreed; the AFL-CIO's final endorsement; the 2020 U.S./Mexico/Canada ratification results; rapid-response enforcement cases; the 2026 review — or explicit hindsight ("as we know", "ultimately it was ratified", "the amended deal ...").
NOT contamination: predicting/debating that amendments will likely be needed, that labor enforcement is contested, that ratification is at risk; reasoning forward about the ratification fight.

Score 0-3: 0=none; 1=trace; 2=at least one clear reliance on a post-cutoff outcome as fact; 3=heavy.
Output STRICT JSON only: {"score": 0, "evidence": ["short quote", "..."]}"""

PROFILES = {"1": (JUDGE_1, HARD_1), "2": (JUDGE_2, HARD_2)}

# Backward-compat for modules that import these (cross_provider_judge):
JUDGE = JUDGE_1
HARD = HARD_1


def keyword_hits(text: str, hard: dict | None = None) -> dict[str, int]:
    hard = hard if hard is not None else HARD_1
    low = text.lower()
    return {name: len(re.findall(pat, low)) for name, pat in hard.items() if re.findall(pat, low)}


async def judge_one(caller, transcript: str, judge: str = JUDGE_1) -> dict:
    msgs = [{"role": "system", "content": judge}, {"role": "user", "content": transcript[:120000]}]
    raw = await caller(msgs)
    t = raw.strip()
    t = re.sub(r"^```(?:json)?", "", t).strip()
    t = re.sub(r"```$", "", t).strip()
    s, e = t.find("{"), t.rfind("}")
    try:
        return json.loads(t[s : e + 1])
    except Exception:
        return {"score": -1, "evidence": [f"parse_error: {raw[:120]}"]}


async def main() -> None:
    ap = argparse.ArgumentParser(description="Scan transcripts for post-cutoff contamination (node-aware)")
    ap.add_argument("--nodes", nargs="+", required=True)
    ap.add_argument("--profile", default="1", help="contamination definition (1|2)")
    ap.add_argument("--no-llm", action="store_true")
    ap.add_argument("--judge-task", default="report")
    ap.add_argument("--concurrency", type=int, default=4)
    args = ap.parse_args()

    judge, hard = PROFILES[args.profile]
    print(f"contamination profile {args.profile} | nodes={args.nodes}")
    tdir = aa_lib.RUN_DIR / "04_Raw_Transcripts"
    caller = aa_lib.make_caller(args.judge_task)
    sem = asyncio.Semaphore(max(1, args.concurrency))

    async def scan_file(node: str, f) -> dict:
        txt = f.read_text()
        kw = keyword_hits(txt, hard)
        rec = {"node": node, "file": f.name, "kw_total": sum(kw.values()), "kw": kw}
        if not args.no_llm:
            async with sem:
                j = await judge_one(caller, txt, judge)
            rec["llm_score"] = j.get("score")
            rec["llm_evidence"] = j.get("evidence")
        return rec

    tasks = [scan_file(n, f) for n in args.nodes for f in sorted(tdir.glob(f"node{n}_run_*_transcript.md"))]
    results = await asyncio.gather(*tasks)

    per_arm: dict[str, list[dict]] = defaultdict(list)
    for rec in results:
        per_arm[rec["node"]].append(rec)
        if (rec.get("llm_score") or 0) >= 2:
            print(f"[node{rec['node']}] {rec['file']}: kw={rec['kw_total']} llm={rec.get('llm_score')}  {rec.get('llm_evidence')}")

    print("\n=== arm comparison ===")
    summary = {}
    for node, recs in per_arm.items():
        valid = [r for r in recs if isinstance(r.get("llm_score"), int) and r["llm_score"] >= 0]
        fails = len(recs) - len(valid)
        mean = round(sum(r["llm_score"] for r in valid) / len(valid), 2) if valid else None
        ge2 = sum(1 for r in valid if r["llm_score"] >= 2)
        print(f"node{node}: valid={len(valid)}/{len(recs)} (parse_fail={fails}) mean_llm={mean} contaminated(>=2)={ge2}/{len(valid) or 1}")
        summary[node] = {"n": len(recs), "valid": len(valid), "mean_llm": mean, "llm_ge2": ge2}

    out = aa_lib.RUN_DIR / "06_Aggregation" / f"contamination_scan_{'_'.join(args.nodes)}.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps({"profile": args.profile, "summary": summary, "runs": results}, indent=2, default=str))
    print(f"\nwrote {out}")


if __name__ == "__main__":
    asyncio.run(main())
