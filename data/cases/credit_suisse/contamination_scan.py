"""Contamination scan — measure post-cutoff outcome leakage per transcript (node-aware).

Each node has a DIFFERENT contamination definition:
  - Node 1: the real rescue outcome (UBS takeover, AT1-to-zero, March 19, real figures) is off-limits.
  - Node 2: the deal + AT1 write-down ARE allowed (post-announcement); only LATER 2024-2025
    litigation OUTCOMES / court rulings are off-limits.

Primary measure: an LLM judge (distinguishes deciding/predicting in-character from reciting a
real post-cutoff fact). Backstop: a small set of unambiguous keywords. Runs concurrently.

Usage::

    .venv/bin/python demos/credit_suisse/contamination_scan.py --nodes 1 1ctrl 1leak
    .venv/bin/python demos/credit_suisse/contamination_scan.py --nodes 2 2off --profile 2
"""

from __future__ import annotations

import argparse
import asyncio
import json
import re
from collections import defaultdict

import aa_lib

# ---- Node 1 profile (rescue-room cutoff) ----
HARD_1 = {
    "hindsight_framing": r"as we know|in hindsight|in reality|what actually happened|as it turned out|historically[, ]|the actual outcome|we now know",
    "real_deal_as_history": r"19 march (deal|takeover|was announced)|march 19 (deal|takeover|announcement)|ubs (ultimately|eventually|did) (acquire|take over)|the takeover (happened|was announced)",
    "later_litigation": r"2024 (lawsuit|ruling|court|litigation)|2025 (lawsuit|ruling|court|litigation)|federal administrative court|quinn emanuel",
}
JUDGE_1 = """You are auditing a transcript of a SIMULATED crisis decision-meeting (a role-play). It is set on Friday 17 March 2023, BEFORE any rescue was decided for Credit Suisse. The participants are SUPPOSED to debate and DECIDE the outcome themselves, treating it as open.

Detect INFORMATION CONTAMINATION = participants drawing on knowledge of what REALLY happened after 17 March 2023, stated as an external established fact (e.g. "UBS took over" as a foregone fact; "AT1 was written to zero" as what happened; the real CHF 3bn / 9bn / 100bn / 16bn / 61bn figures as history; the 19 March announcement; any 2024-2025 ruling; explicit hindsight).
NOT contamination: proposing/deciding these in-character now; inventing their own figures; debating uncertain options.

Score 0-3: 0=none; 1=trace; 2=at least one clear reference to the real outcome as established fact; 3=heavy.
Output STRICT JSON only: {"score": 0, "evidence": ["short quote", "..."]}"""

# ---- Node 2 profile (post-announcement; only later litigation outcomes off-limits) ----
HARD_2 = {
    "hindsight_framing": r"as we know|in hindsight|in reality the court|the court ultimately|as it turned out|we now know the court",
    "litigation_outcome": r"court ruled|ruled (un)?lawful|tribunal ruled|won the (case|appeal|suit)|lost the (case|appeal|suit)|damages (were )?awarded|overturned the write-?down|2025 ruling|2024 ruling|appeal (was )?(upheld|dismissed)",
}
JUDGE_2 = """You are auditing a transcript of a SIMULATED reaction meeting (role-play) set in late March 2023, AFTER the UBS rescue and the FINMA-ordered full write-down of Credit Suisse AT1 to zero were announced. Those announcements (the UBS takeover, the AT1 write-down to zero, FINMA's viability-event basis, the immediate market reaction) ARE legitimately known and are NOT contamination.

Detect INFORMATION CONTAMINATION = relying on knowledge of LATER (2024-2025) litigation OUTCOMES as established fact: e.g. stating that a court ruled the write-down lawful or unlawful, that AT1 holders won or lost, specific 2024/2025 rulings (e.g. the Swiss Federal Administrative Court decision), named lawsuits' results, damages awarded — or explicit hindsight ("as we know", "in hindsight", "the court ultimately ...").
NOT contamination: predicting/debating that litigation is likely, long, or may succeed/fail; citing the announced deal/write-down; reasoning forward about the claims tail.

Score 0-3: 0=none; 1=trace; 2=at least one clear reliance on a post-event litigation outcome as fact; 3=heavy.
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
