# Submission completion checklist

This file separates what the current reviewer artifact already demonstrates
from work that still requires human judgment, author decisions, or access to the
simulation service.

## Complete in the current artifact

- [x] Self-contained two-case corpus export.
- [x] Run manifest with file hashes and explicit condition denominators.
- [x] Deterministic reconstruction of the provisional evidence table.
- [x] Snapshot of current audit prompts and lexical rules.
- [x] Written annotation codebook and structured annotation template.
- [x] Anonymous release checks and exclusion of active coder materials.
- [x] One-command, dependency-free Level-1 recomputation (`make all`).
- [x] Continuous verification on pushes and pull requests.
- [x] Conservative proposal-correction memo and technical-appendix scaffold.
- [x] Organizational-inference table with candidate conclusions and explicit
      pending fields.
- [x] Model-provenance gap inventory.
- [x] Medium-confidence model-route reconstruction with unresolved fields kept
      explicit.
- [x] Harmonized run-level table for the 160 existing focal decision outputs.

## Required before Stage 1 submission

- [ ] Obtain two independent human labels for the frozen sample.
- [ ] Adjudicate disagreements and publish de-identified labels plus an
      adjudication log.
- [ ] Replace provisional automated findings with a verified evidence table.
- [ ] Select one organizational conclusion per case and link it to the relevant
      output, information condition, leakage evidence, and inference status.
- [ ] Freeze exact model/provider identifiers and document any API cost needed
      to rerun model-based audits.
- [ ] State the simulation-regeneration access arrangement without exposing the
      proprietary engine.
- [ ] Have a person outside the implementation team execute `make all` from a
      fresh clone and record the result.
- [ ] Align every numerical claim in the proposal and technical appendix with a
      machine-readable row in the final evidence table.
- [ ] Run the final anonymity audit on the proposal, appendix, repository, and
      document metadata.

## Claims that must remain qualified

- Automated `0/50` means no automated positives under that instrument; it does
  not establish absence of contamination.
- Seeded inputs test detector response; output correctness requires independent
  human labels.
- The existing de-identification condition is a bundled counterfactual, not an
  isolated identity manipulation.
- Stability under a tested control supports robustness only under that control;
  it does not establish uncontaminated or human-like reasoning.
