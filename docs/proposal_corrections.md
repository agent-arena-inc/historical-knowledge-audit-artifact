# Proposal corrections and evidence review — 22 October 2026

Evidence baseline: commit b04f8ee017840ac5c20d9bd8bfb9742ef5c48887.
The current proposal was read in full. Retain its research question, two cases,
and contribution structure. The replacements below correct evidence and delivery
status; they do not add cases, redesign the research, or replace existing tools.

## 1. What is mechanically verified

The existing script scripts/reproduce_provisional_table.py was executed against
the seven supplied cache files. Its 12 rows match the committed
[provisional table](../data/derived/provisional_evidence_table.md).
Positive means an integer score at least 2; it is not a human leakage label.

| Case / condition | Cached evaluator | Eligible runs | Attempted | Valid | Positive | Missing | Parse failures |
|---|---|---:|---:|---:|---:|---:|---:|
| USMCA historical | Report | 50 | 50 | 50 | 22 | 0 | 0 |
| USMCA historical | Legacy Haiku | 50 | 49 | 49 | 0 | 1 | 0 |
| USMCA historical | OpenAI | 50 | 49 | 48 | 5 | 1 | 1 |
| USMCA historical | Google | 50 | 49 | 48 | 11 | 1 | 1 |
| Credit Suisse historical | Report | 50 | 50 | 50 | 0 | 0 | 0 |
| Credit Suisse historical | OpenAI | 50 | 50 | 50 | 0 | 0 | 0 |
| Credit Suisse historical | Google | 50 | 50 | 50 | 0 | 0 | 0 |
| Credit Suisse seeded | Report | 5 | 5 | 5 | 1 | 0 | 0 |
| Credit Suisse seeded | OpenAI | 5 | 5 | 5 | 4 | 0 | 0 |
| Credit Suisse seeded | Google | 5 | 5 | 5 | 2 | 0 | 0 |
| Credit Suisse control | Report | 4 | 4 | 4 | 0 | 0 | 0 |
| Credit Suisse hindsight | Report | 5 | 5 | 5 | 0 | 0 | 0 |

Run-level reconciliation from cache filenames:

- All three incomplete USMCA caches omit node1_run_017.
- OpenAI fails to parse node1_run_022; Google fails to parse node1_run_019.
  Their 48 valid outputs therefore are not the same set.
- On the common 47 valid runs across all four USMCA caches, the positive counts
  are Report 20/47, legacy Haiku 0/47, OpenAI 5/47, and Google 10/47.
  These are descriptive instrument differences, not isolated provider effects:
  historical prompt/configuration equivalence has not been established.
- Credit Suisse seeded positive IDs are Report {004}, OpenAI {002,003,004,005},
  and Google {002,005}; their three-way intersection is empty.
- The manifest contains 286 rows: 280 candidates and six excluded pilots.
  This is the full artifact inventory, not the denominator for either headline.
- The existing extraction contains 160 focal decision outputs. These are cached
  model-derived representations, not adjudicated organizational findings.

### Lexical counts: do not turn a memo tally into a verified result

The historical 27/50 has no recoverable frozen rule and run-ID mapping and must
be withdrawn. The reconciliation memo reports a current uniform screen of
28/50, or 27/49 after removing run 017. However, the reviewed snapshot does not
provide a corresponding executable rule plus machine-readable hit list.
The current snapshot freezes HARD_1/HARD_2; the table script instead summarizes
stored kw_total values, producing 9/50 for Report and 13/49 for the other USMCA
caches. Those are different measures and cannot substantiate 28/50.

Retain 28/50 and 27/49 only as documented, unverified screen tallies until the
technical lead supplies the already-used rule, its hash, run-ID hits and command.
Do not reverse engineer a new rule to recover a target number.

The reported 1/30 de-identification screen likewise is a candidate tally.
Direct inspection confirms that
[node1blind_run_010](../data/cases/usmca/run/04_Raw_Transcripts/node1blind_run_010_transcript.md)
contains a 16-year proposal with a year-10 review and later moves to 17 years
with year-10 consultation. It is not a literal reproduction of the final
16-year/year-6 combination. Its substantive label remains for human coding.

## 2. A dated-source problem must be resolved before human coding

The USMCA configuration says the scene is just after the 27 August 2018
U.S.–Mexico preliminary agreement, with information knowable on or before
that date. The current judge nevertheless treats a 16-year term with six-year
review as necessarily post-cutoff, including when proposed in character.

A contemporaneous government press-call transcript dated 27 August 2018,
12:39–13:02 EDT, already describes the 16-year term and six-year review:
[archived primary transcript](https://www.presidency.ucsb.edu/documents/press-call-the-united-states-mexico-trade-agreement).
The scenario also says to use only supplied notes. These are different boundaries:

- A fact may have been publicly available by the historical cutoff.
- The same fact may be absent from the actor's permitted supplied materials.
- An assertion that Canada had already agreed to a final trilateral settlement
  may still be temporally improper even when the numbers were already public.

Therefore, a number match alone cannot establish post-cutoff historical leakage.
Confirm the within-day cutoff and actor-access policy, then distinguish temporal
violations from use of unsupplied but contemporaneously public information.
Do not silently relabel or overwrite cached automated judgments.

The current USMCA judge counts exact outcome matches even as proposals; the
Credit Suisse judge excludes in-character proposals. The draft codebook also
contains both VIOLATION_OUTCOME_MATCH and NEGOTIATING_PROPOSAL. Freeze a dated
precedence rule before independent coding, including how admissible prior
sources override a numerical match. Retain unresolved cases explicitly.

## 3. Direct replacements for the proposal

### A. “Preliminary evidence: status and verification plan”

Replace the paragraph beginning “Two candidate discrepancies motivate this
proposal” with these two paragraphs:

> Cached automated audits motivate two candidate discrepancies, neither yet a human-verified contamination finding. For the 50-run historical USMCA condition, the current Report cache records 22 positive labels at a score threshold of at least 2. A legacy cache records zero positives among 49 valid labels, omitting run 017 and lacking complete invocation provenance. OpenAI and Google caches record 5/48 and 11/48 positives; each attempted 49 runs, omitted run 017, and had one parse failure, on runs 022 and 019 respectively. These 48-run valid sets differ. The earlier 27/50 lexical headline is withdrawn. A reconciliation memo records replacement screen tallies of 28/50 and 27/49, but their executable rule and hit list still require confirmation. The de-identification screen's reported 1/30 is a candidate, not confirmed leakage.

> For Credit Suisse, each of three cached evaluators records zero positives among 50 valid historical-condition outputs. In the five-run seeded condition, the same evaluator labels yield 1/5, 4/5, and 2/5 positives, with no run flagged by all three. These counts characterize instrument responses. Agreement on negatives is not external validation, and seeded inputs do not establish which generated outputs violate the information boundary. Cross-instrument differences also reflect potentially different definitions and configurations, not model family alone.

Replace the paragraph beginning “Before this proposal can rely on either number”
with:

> The repository now contains a hashed run manifest, current-source instrument snapshot, deterministic cache-summary script, draft codebook and annotation templates. Independent labels, adjudication and the final evidence table remain incomplete. Before treating these counts as substantive findings, we will freeze the coding rules and sample, then obtain two independent, evaluator-blinded annotations using actor-specific inputs and dated sources. In USMCA, the 16-year term and six-year review were publicly described on 27 August 2018, so numerical agreement alone cannot establish post-cutoff leakage; the coding must distinguish temporal violations from use of unsupplied but contemporaneously public facts. We will retain the original labels and document adjudication, sources, access, claim locators and affected conclusions. A diagnostic sample enriched for suspected positives and disagreements can identify failure modes but cannot estimate corpus leakage prevalence. If validation remains incomplete, we will report that status rather than present automated labels as confirmed leakage.

### B. “Protocol and decision-output comparisons”

The existing bundled-control qualification should be retained. Replace the
sentence beginning “Where feasible, we will design an additional control” with:

> Additional controls that vary identifying cues while preserving institutional structure and substantive information are development-stage work; the October 24 checkpoint concerns reconciliation and independent verification of the existing cases.

After the sentence ending “which would limit what the comparison can establish
regardless of audit outcome,” insert:

> The existing extractor already harmonizes 160 focal outputs, but matched control-output comparisons and independent inference judgments remain incomplete. Current output patterns therefore identify candidate conclusions, not demonstrated effects of information controls. Existing Node-2 decision outputs must not be assigned the Node-1 audit counts.

For contribution wording, use:

> We develop and test an auditable protocol linking actor-specific information boundaries to questionable claims, their reuse in interaction, and the organizational conclusions researchers draw from simulation outputs. Observable reuse establishes a propagation trace; causal influence requires an appropriate control or intervention. Portability beyond the supplied transcript schema is an intended capability, not yet independently demonstrated.

Call the existing USMCA manipulation a “bundled de-identification control.”
Do not call it an isolated identity experiment or infer a contamination-specific
causal effect from a change under that bundle. This supersedes the earlier memo's
“de-identification and anonymization controlled counterfactual experiment” advice.

### C. “Research artifact and adoption”

Replace both paragraphs with:

> We distinguish recomputation, audit rerunning and simulation regeneration. The current repository supports deterministic recomputation of its cached-judgment and extracted-output tables from the supplied corpus without API credentials or the private engine. It includes the README, hashed run manifest, schema, current instrument snapshot, draft annotation codebook and templates, release inventory and runnable scripts. Independent human labels and the final adjudicated evidence table have not yet been added; recomputation of those findings will be claimed only after they exist.

> Faithful rerunning of every historical audit is not yet supported: current prompts are frozen but not proven to match every cache, and exact invocation records, dates, parameters, parser versions and API access/cost documentation remain incomplete. Fresh model calls may differ from cached results and will be reported separately. Regenerating the original simulations also remains unverified because per-run provenance and executable or controlled engine access are incomplete. We will state the deliverable and access status explicitly at submission and limit inference accordingly. A fresh-clone execution by a person outside the implementation team remains a separate usability check; successful automated verification does not complete it.

### D. “Development risks and milestones”

Replace the paragraph beginning “The most consequential risk” with:

> The principal risk is that dated-source checking and independent annotation revise or remove the proposed discrepancies. We will preserve the cache results as instrument responses and report what survives harmonization. By October 24 our evidence checkpoint is to freeze run mappings, resolve the lexical-rule and cutoff issues, and obtain the independent labels and adjudication needed for any confirmed examples. Unfinished items will remain explicitly pending. The October 27 package checkpoint and planned October 30 submission ahead of the November 1 deadline remain the internal schedule. Additional cases and new information-control experiments remain development-stage work.

Retain the question and opening as research aims. Do not phrase causal effects,
demonstrated portability, or a validated contamination rate as existing results.

### E. “Expected scientific gain” and title

Replace “where two independently engineered audits of the same transcripts can
disagree and why” with:

> where documented audit instruments yield different responses on overlapping transcripts, and what independent adjudication establishes about those differences

“Bounding” in the title should mean limits on supported organizational inference,
not a statistical upper bound on contamination. Add:

> Here, bounding refers to delimiting supported inference, not estimating an upper bound on contamination prevalence.

### F. Related work and references

The cited papers exist. Keep their positioning but correct these details:

- The Zhang, Chen and Stadie v2 title includes “Detection and Mitigation.”
  Use “Shapley-DCLR,” and describe TimeSPEC as the authors' inference-time
  architecture with a temporally filtered, claim-supervised aggregator.
  [Primary paper](https://arxiv.org/html/2602.17234v2).
- Tranchero and colleagues benchmark simulated behavior and check GPT-4's
  familiarity with their particular experiment. This does not certify all
  unfamiliarity tests or validate the current two cases.
  [Author-hosted paper](https://faculty.wharton.upenn.edu/wp-content/uploads/2026/08/Tranchero-et-al_SMJ_2026.pdf).
- Wiedmann and colleagues support configuration-sensitive evaluation; they do
  not establish the validity of the present caches.
  [Primary paper](https://arxiv.org/abs/2610.01618).
- Remove “rather than a formal agreement statistic” from the Gan sentence:
  the paper describes agreement computation on an independently double-annotated
  subset. Its recoverable false-negative finding is about task completion,
  not historical contamination. Use this replacement:

> Gan et al. (2026) show that human review can recover task successes missed by automated WebArena-Lite evaluation. We treat this as motivation for independent verification, not evidence that our historical-knowledge judges have the same errors; transfer to this setting remains to be tested.

[Primary paper, human-verification protocol](https://arxiv.org/html/2610.01491v1).

## 4. Existing organizational outputs: usable evidence and limits

Source: [decision-output summary](../data/derived/decision_output_summary.md) and
[inference worksheet](../data/annotations/organizational_inference_template.csv).

| Existing representation | Cached pattern | What remains unverified |
|---|---|---|
| USMCA trade negotiation | trilateral_package 48/50 | Objective prescription, admissibility, and matched de-identification output comparison |
| USMCA ratification | reopened_for_amendment 27/30; stalled_on_labor_enforcement 3/30 | Node-2 leakage coding and comparable control outputs |
| Credit Suisse rescue | acquisition 40/50; at1_tail_risk present 50/50 | Distinguish acquisition path from heterogeneous AT1 choices; check objectives and human evidence |
| Credit Suisse reaction | negotiated_settlement 15/30; litigation_dominant 13/30; no_consensus 2/30 | Litigation prominence is not universal litigation dominance; Node-2 human audit and controls remain absent |

All four inference statuses remain unresolved in the supplied worksheet.
The de-identification arm has transcripts but no harmonized decision-output JSON;
Credit Suisse control and seeded arms likewise lack the matched output
representation needed for the proposed comparison. Do not convert frequencies
within the original condition into a finding of robustness across controls.

## 5. October 24 closure checklist and author confirmations

Use existing scripts, templates and privately held blinded packets. Do not send
the evidence tables or automated labels to coders with their packets.

| Priority | Owner role | Confirmation or deliverable needed |
|---|---|---|
| P0 | Technical lead | Supply the already-used uniform lexical rule, hash, command and run-ID list supporting 28/50, 27/49 and 1/30, or remove them from the submission's numerical evidence |
| P0 | Both leads | Freeze the exact cutoff/access policy and source-based precedence for public-at-cutoff facts, unsupplied facts, proposals and asserted final history |
| P0 | Both leads | Name two independent coders and an adjudicator; confirm packet/sample version, random-negative selection seed, and completion time |
| P0 | Coders/adjudicator | Freeze original labels separately; retain disagreements, adjudication reasons and dated source evidence; at least one coder outside the platform team is preferable |
| P0 | Proposal lead + technical lead | Select one conclusion per case using the existing worksheet; verify objective prescription; keep unsupported control-effect claims unresolved |
| P1 | Technical lead | Recover exact historical audit invocation records where available; otherwise record unknowns and narrow Level-2 promises |
| P1 | Technical lead | Confirm regeneration-access scope and arrange an outside-team fresh-clone usability run with a dated execution record |
| P1 | Proposal lead | Apply replacements, confirm unresolved claims are labeled, and finalize anonymous proposal/appendix/artifact access |

If two human coders cannot finish by the checkpoint, report partial coverage
and unresolved items accurately. Do not call an AI review a second independent
human annotation. Missing human evidence must not be backfilled by assumption.

## 6. Reproduction and submission checks

- Existing cache-table script: executed successfully in this review; 12 rows
  agree with the committed table. Raw cache records also establish the missing
  and parse-failed run IDs and the shared-47 counts above.
- Existing CI at the reviewed baseline passed make all, artifact verification,
  and git diff --exit-code. That supports the existing mechanical checks,
  not human labels, semantic correctness, or an outside-team execution.
- The [model provenance inventory](model_provenance.md) is a medium-confidence
  reconstruction, not exact per-run proof. Preserve its unknown fields and
  the documented temperature-comment/settings discrepancy.
- The supplied proposal contains an author/affiliation block and an identifying
  disclosure placeholder. It is a working copy, not an anonymous submission.
  Repository access is private; confirm reviewer/editor access and anonymous
  package contents rather than promising a public corpus already exists.
- The [official call](https://orgsci.org/) states November 1, 2026 and
  approximately 1,500–2,000 words plus references. A whitespace count of the
  reviewed text is 2,139 overall / 2,053 before references, including headings
  and the working author/disclosure material. This is a diagnostic count, not
  a journal word-count ruling; recount the final anonymous revised copy.
