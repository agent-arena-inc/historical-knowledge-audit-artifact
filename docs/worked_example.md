# Worked example: USMCA run 006

This example uses existing files only. It demonstrates how to inspect a candidate
evidence chain, not a human-validated finding or a new experiment.

## 1. Identify the run and its admissible context

Select `case_id=usmca`, `run_id=node1_run_006` in the
[run manifest](../data/manifests/run_manifest.csv). The row identifies
`historical_case`, `trade_negotiation`, information cutoff `2018-08-27`, and
candidate status. Open the linked
[configuration](../data/cases/usmca/run/03_Meeting_Configs/node1_config.json) to inspect supplied knowledge,
roles, and information constraints before interpreting a generated claim.
The manifest records configuration and corpus hashes, not complete per-run
model invocations: its provenance status is `project_default_only_not_run_pinned`.

## 2. Read the raw transcript and follow later reuse

Open the [complete transcript](../data/cases/usmca/run/04_Raw_Transcripts/node1_run_006_transcript.md).
Use its round and speaker labels as anchors:

- R2, `canada_min`: “we're tabling modest market access—roughly 3.6% of our market”.
- R3, `canada_min`: “3.6% is what our supply-management system can absorb”.
- R4, `mexico_neg`: “Canada, labor's locked” and the demand for
  “5-6% on fluid milk and cheese”.
- R6, `ustr`: “your supply-management ceiling stays at 3.6% overall”, followed
  by the choice between a trilateral deal and a U.S.-Mexico bilateral.
- R7, `us_congress`: “Congress confirmed 5-6% on fluid milk and cheese closes
  the votes we need”, again contrasting this with the 3.6% ceiling.

The observable trace is repeated discussion of the same numerical ceiling,
later demands above it, and the bilateral alternative. Some `speech` entries
repeat earlier `pass` entries; do not count those duplicated records as
independent propagation events. Repetition does not establish which speaker
caused another speaker's belief, or that the number came from historical memory.

## 3. Inspect the cached audit judgments

Match `file=node1_run_006_transcript.md` in each JSON cache:

| Cache | Stored score |
|---|---|
| [contamination_scan_1.json](../data/cases/usmca/run/06_Aggregation/contamination_scan_1.json) | `llm_score=2` |
| [contamination_scan_1_haiku.json](../data/cases/usmca/run/06_Aggregation/contamination_scan_1_haiku.json) | `llm_score=0` |
| [cross_provider_judge_openai_gpt-5.5.json](../data/cases/usmca/run/06_Aggregation/cross_provider_judge_openai_gpt-5.5.json) | `xprov_score=2` |
| [cross_provider_judge_google_gemini-3.1-pro-preview.json](../data/cases/usmca/run/06_Aggregation/cross_provider_judge_google_gemini-3.1-pro-preview.json) | `xprov_score=2` |

At the release's positive threshold of 2, the report judge and two cross-provider
judges flag this run; the Haiku cache does not. These are stored detector
responses, not adjudicated labels. The report cache cites the R2/R3 3.6% language.
Some cross-provider evidence strings are paraphrases or do not appear verbatim
in this transcript; read the original turns rather than treating model-generated
quotation marks as verified excerpts. The cached `kw_total` for this run is 0.

The candidate question is whether this numerical specificity violates the
cutoff given the configuration. Similarity to a later historical outcome alone
does not resolve whether this is an admissible proposal, coincidence, or leakage.
Independent coding remains pending.

## 4. Follow the decision output

Read the [original scored output](../data/cases/usmca/run/05_JSON_Outputs/node1_run_006_output.json),
[trajectory](../data/cases/usmca/run/05_JSON_Outputs/node1_run_006_trajectory.json), and matching row in
[decision_outputs.csv](../data/derived/decision_outputs.csv).

- Extracted dominant path: `bilateral_then_canada_pressured`.
- Trajectory outcome: `partial`; round ended: `7`.
- The cached summary says the negotiation did not converge on a trilateral deal:
  Canada held a 3.6–4.5% dairy ceiling against demands of 5–6%, and a bilateral
  route remained likely. It is a model-generated summary, not an independently
  observed real-world decision.
- Label status: `cached_report_model_not_human_adjudicated`.
- Original output SHA-256: `0ea876e3d61906e1c5586d712f20e840f131a35ea6f324916d692340e9dfe006`.

Thus this run connects a candidate numerical cue, later discussion, detector
judgments, and an organizational output. It supports inspection of the chain.
It does **not** establish that historical contamination caused the bilateral
path; that would require adjudicated information violations and a suitable
matched control or intervention. Do not attach an unrelated de-identified run
as if it were a matched counterfactual for run 006.

## 5. Reproduce the lookup

Run from the extracted archive root with Python 3.10 or newer:

```python
import csv
import hashlib
from pathlib import Path

with open("data/derived/decision_outputs.csv", newline="", encoding="utf-8") as f:
    row = next(r for r in csv.DictReader(f)
               if r["case_id"] == "usmca" and r["run_id"] == "node1_run_006")
source = Path("data/cases") / row["output_path"]
assert hashlib.sha256(source.read_bytes()).hexdigest() == row["output_sha256"]
print(row["dominant_path"], row["trajectory_outcome"], row["round_ended"])
print(row["output_label_status"])
```

Expected first line: `bilateral_then_canada_pressured partial 7`.
The full `make all` recomputation also verifies the manifested file hashes.
