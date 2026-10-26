# Proposal corrections supported by the current artifact

This drafting aid records evidence-consistent wording while independent human
coding remains planned. It is not a list of required edits or new experiments.
Use the generated cached-judgment table as the numerical reference.

## Central question

> How does historical knowledge contamination affect the organizational
> conclusions drawn from LLM-agent simulations, and which conclusions remain
> supported under documented information controls?

## Preliminary-evidence wording

### USMCA

Use:

> In the 50-run historical USMCA condition, the current cached report-judge
> marks 22 outputs at or above its positive threshold. Two other cached model
> judges mark 5 of 48 and 11 of 48 valid outputs, respectively; each cache is
> missing one eligible run and contains one parse failure. An older cache
> records zero positives among 49 attempted outputs but lacks sufficient prompt
> and invocation provenance for faithful reconstruction. These are automated
> detector responses, not human-verified contamination rates.

The earlier `27/50` lexical headline lacks its original frozen rule and run-ID
map. Later working notes report `28/50` and `27/49` excluding run 017, but those
replacement tallies are not reconstructed by the committed aggregation script.
Use the reproducible cached-judge counts above for preliminary numerical claims.
The table's `keyword_positive` field summarizes stored `kw_total` values and is
a separate measure.

For the 30-run de-identification condition, use:

> The current lexical screen produces one candidate in 30 runs. That output
> proposes a 16-year term with a year-10 review, rather than reproducing the
> historical year-6 review, and therefore requires human coding. The condition
> jointly changes identity, sector, dates, role and variable identifiers, and
> numerical details; any difference is attributable only to the bundled
> transformation.

### Credit Suisse

Use:

> Across 50 historical-condition outputs, each of three cached automated judges
> records zero positives under its own instrument. This supports only the claim
> that those instruments did not flag the outputs; sampled negative judgments
> still require independent review.

For the five-run seeded condition, use:

> The three cached judges mark 1/5, 4/5, and 2/5 outputs. Their positive-run
> intersection is empty. Because the seed is supplied in the input, these
> figures characterize detector response rather than detector accuracy;
> correctness must be assessed against independently labeled generated text.

## Interpretation guidance

These distinctions guide interpretation; existing proposal language that
already respects them does not need additional editing.

- Call the USMCA manipulation a **de-identification and anonymization controlled
  counterfactual experiment**.
- Describe the studies as **two cross-domain cases**, not independent
  replications.
- Describe the seeded arm as a **positive-control input testing detector
  response**, with correctness assessed at the generated-output level.
- Say that prior historical exposure **may exist and cannot be excluded through
  input quarantine alone**.
- A passed audit does not establish genuine reasoning, absence of latent
  historical knowledge, or validity as a model of human decision-making.

## Contribution wording

> We develop and test an auditable protocol that links actor-specific
> information boundaries to the introduction and reuse of questionable claims
> in interaction and, ultimately, to the organizational conclusions researchers
> draw from simulation outputs. The protocol distinguishes detection evidence,
> propagation traces, controlled decision-output changes, and the inferential
> status of each conclusion. Observed transcript reuse establishes a propagation
> trace; causal influence requires an appropriate control or intervention.
