# Evidence reconciliation log

This is a working reconciliation of cached automated judgments. It does not
replace independent human annotation.

## Denominator policy

Every evaluator result must report these quantities separately:

- `corpus_total`: all eligible runs in the condition;
- `attempted_records`: runs sent to the evaluator and retained in its cache;
- `valid_labels`: successfully parsed labels;
- `positive_ge_2`: valid labels at or above the evaluator's positive threshold;
- `missing_from_corpus`: eligible runs absent from that cache; and
- `parse_failures`: attempted runs without a valid label.

The denominator for a model response rate is `valid_labels`. Attempted and
corpus totals must remain visible so missing runs and parse failures are not
silently absorbed.

## USMCA

- The cached 0/49 result is traceable. Run `node1_run_017` is absent from that
  cache. The cache does not contain a prompt hash, model invocation record, or
  code version, so the old instrument cannot yet be faithfully rerun.
- The current sharpened cached report-judge result is 22 positives from 50
  valid labels. Positive run IDs are: 002, 003, 004, 006, 009, 010, 013, 017,
  018, 021, 022, 024, 025, 029, 032, 034, 036, 038, 040, 041, 042, and 045.
- The cached OpenAI cross-provider result contains 49 attempted runs, 48 valid
  labels, five positives, one missing run, and one parse failure. The cached
  Gemini result likewise contains 49 attempted runs and 48 valid labels, with
  eleven positives, one missing run, and one parse failure.
- The previously stated lexical count of 27/50 is not backed by a frozen rule,
  machine-readable result, or run-ID map. Later working notes report 28/50 and
  27/49 after removing run 017, but the committed aggregation script does not
  reconstruct those replacement tallies. They are not verified headline results
  in this release. Its `keyword_positive` column instead summarizes stored
  `kw_total` values, a separate cached measure. Preliminary numerical claims
  should use the reproducible cached-judge table.
- The 30-run de-identification condition has one lexical candidate,
  `node1blind_run_010`. It mentions a 16-year term with a year-10 review rather
  than the historical year-6 review. It requires human coding and must not be
  called confirmed leakage from the lexical match alone.
- The de-identification condition changes identity, sector, dates, role and
  variable identifiers, and specific numbers together. It is a bundled control,
  not a single-factor identity manipulation.

## Credit Suisse

- The current primary cached results contain zero automated positives among 50
  valid treatment runs for each of three evaluators. This means "automated
  detector positives = 0/50 pending human audit," not absence of leakage.
- In the five-run seeded condition, the three cached evaluators produce 1/5,
  4/5, and 2/5 positives. All records are present and parse successfully.
- The one-positive evaluator flags run 004. The four-positive evaluator flags
  002, 003, 004, and 005. The two-positive evaluator flags 002 and 005. The
  intersection of positive run IDs across all three evaluators is empty.
- The seeded configuration supplies historical outcome information, but a
  generated output is not automatically positive. Detector correctness must be
  assessed against independently labeled output excerpts.
- Cue-rich treatment negatives should be included in human review because the
  absence of automated positives depends on contextual distinctions between
  in-simulation proposals and assertions of established history.

## Proposed annotation strata

The initial sample should cover:

1. USMCA multi-evaluator positives: runs 006, 025, and 045.
2. USMCA evaluator disagreements: runs 014 and 049.
3. USMCA sharpened/lexical positives: runs 003, 004, 017, and 018.
4. USMCA de-identification candidate: blind run 010.
5. USMCA randomly sampled current negatives, selected after the canonical label
   table is frozen.
6. All five Credit Suisse seeded runs.
7. Credit Suisse cue-rich treatment negatives: runs 001, 030, and 040.
8. Random Credit Suisse treatment negatives, selected with a recorded seed.
