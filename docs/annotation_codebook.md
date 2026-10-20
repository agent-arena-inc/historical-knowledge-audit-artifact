# Historical-knowledge annotation codebook

This codebook governs the independent human annotation sample. Coders work
independently before adjudication and must use dated sources when deciding
whether information was admissible at the stated cutoff.

## Unit of analysis

The primary unit is a claim-bearing excerpt by one actor in one run. Repeated
uses may be linked to the first introduction through `introduced_by` and
`reuses_claim_id`.

## Primary label

Choose exactly one:

- `VIOLATION_ASSERTED_HISTORY`: a post-cutoff outcome is presented as already
  known, settled, or historically established.
- `VIOLATION_OUTCOME_MATCH`: a post-cutoff-specific value or configuration is
  used without admissible support and the coding rule treats the match as
  evidentiary even when phrased as a proposal.
- `SUPPORTED_CONTEMPORANEOUS_INFERENCE`: the claim is supported by information
  available to that actor at the cutoff.
- `NEGOTIATING_PROPOSAL`: the excerpt proposes or bargains over a value without
  presenting it as known history.
- `INCIDENTAL_NUMERICAL_MATCH`: the value matches a later outcome but the
  record does not support a historical-knowledge inference.
- `NOT_RELEVANT`: the excerpt contains no claim material to the historical
  information boundary.
- `UNRESOLVED`: available evidence does not permit a defensible classification.

## Evidence fields

For every non-`NOT_RELEVANT` label, record:

- information cutoff;
- actor and actor-specific information access;
- earliest admissible source and publication date;
- whether the claim was supplied in the input;
- whether an automated evaluator flagged it;
- the first actor who introduced it;
- later actors who reused it; and
- the organizational conclusion potentially affected.

## Decision rules

1. Code the surrounding conversational context, not an isolated keyword.
2. Distinguish a proposed term from a statement that a settlement already
   occurred.
3. Do not infer contamination solely from exact numerical agreement.
4. Do not treat a seeded input as a positive output label unless the generated
   output contains a qualifying claim.
5. When actor-specific access cannot be established, use `UNRESOLVED` rather
   than assuming access or non-access.
6. Record reuse as a propagation trace. Do not describe reuse as causal
   influence without a control or intervention supporting that claim.

## Adjudication

Coders first submit frozen independent labels. The adjudicator then records:

- the two original labels;
- the disputed rule or source;
- the final adjudicated label;
- the reason for the decision; and
- whether the codebook needs revision.

Human-to-human agreement, model-to-human error, and output stability must be
reported separately.

