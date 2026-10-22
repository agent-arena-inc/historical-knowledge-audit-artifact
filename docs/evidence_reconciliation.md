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
  machine-readable result, or run-ID map and is stale and unverified. The working
  reconciliation records replacement screen tallies of 28/50, or 27/49 after
  excluding run 017. Review on 22 October found no committed executable rule
  plus hit list reproducing these replacement tallies in the reviewed snapshot.
  Treat them as documented but unverified until that evidence is supplied.
  The existing table script summarizes cached kw_total values instead (9/50 for
  the Report cache and 13/49 for the other caches); those are different measures.
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


## Review addendum — 22 October 2026

The existing cache-summary script was executed successfully against all seven
cache files; its 12 rows match the committed provisional table. This verifies
mechanical cache counts, not historical contamination or detector accuracy.

- The OpenAI parse failure is node1_run_022; the Google parse failure is
  node1_run_019. Their 48 valid outputs are not the same subset.
- Across the common 47 valid USMCA runs, positive counts are Report 20/47,
  legacy Haiku 0/47, OpenAI 5/47 and Google 10/47. Prompt and configuration
  equivalence is not established, so these are instrument differences rather
  than isolated model-provider effects.
- The historical 16-year term and six-year review were publicly described in
  a government press call on 27 August 2018, the stated scenario cutoff date:
  [contemporaneous primary transcript](https://www.presidency.ucsb.edu/documents/press-call-the-united-states-mexico-trade-agreement).
  Confirm the within-day cutoff and actor-access policy before coding.
  A fact absent from supplied notes may violate a supplied-only boundary
  without being post-cutoff historical knowledge. A numerical match alone
  does not resolve that distinction or establish that Canada had agreed.
- The current USMCA judge treats certain exact matches as positive even when
  proposed; the Credit Suisse judge excludes in-character proposals. Preserve
  cached labels and freeze a dated human-coding precedence rule before
  comparing substantive errors.
- Use a bundled de-identification control description. The earlier advice
  calling it a controlled counterfactual experiment must not imply isolation
  of identity or a causal effect of historical contamination.
- Ready-to-paste proposal replacements, remaining human-evidence requirements,
  and author confirmations are in [proposal_corrections.md](proposal_corrections.md).
