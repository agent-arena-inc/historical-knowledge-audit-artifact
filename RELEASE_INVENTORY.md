# Release inventory

Status labels:

- **Available**: present in the working case export.
- **Generated**: deterministically created by an artifact script.
- **Pending verification**: present but not yet independently validated.
- **Planned**: required before submission but not yet complete.

| Item | Status | Submission role |
|---|---|---|
| Two-case transcript corpus | Available | Source material for recomputation and annotation |
| Per-run trajectory JSON | Available | Simulation outcomes and event traces |
| Cached per-run scoring outputs | Available | Inputs to deterministic aggregation |
| Meeting configurations and control variants | Available | Documents case and condition setup |
| Cached cross-provider audit judgments | Pending verification | Preliminary evaluator comparison |
| Current audit prompts and lexical rules | Generated | Exact snapshot of current source; historical cache linkage remains pending |
| Run manifest with SHA-256 hashes | Generated | Maps denominators and exclusions to run IDs |
| Provisional cached-judgment table | Generated | Recomputes current, non-human-verified counts |
| Transcript schema | Available | Documents the supplied transcript representation |
| Human annotation codebook | Available as draft | Defines labels and adjudication rules |
| Evaluator-blinded independent coder packets | Generated | Two separate worksheets with hidden run IDs and automated labels |
| Independently coded annotation sample | Planned | Establishes preliminary external evidence |
| Adjudication log | Planned | Records disagreement resolution |
| Organizational-conclusion evidence table | Planned | Links leakage evidence to supported inference |
| Anonymous self-contained corpus export | Generated pre-submission snapshot | Review-server deliverable; active coding keys and packets are excluded |
| Fresh-audit API cost and variation report | Planned | Documents audit rerun requirements |
| Simulation-regeneration access arrangement | Planned | Required only for control-effect claims |
| External-user execution record | Planned | Practical usability check |

## Release gate

The package is not submission-ready until the following are true:

1. Every reported numerator and denominator maps to named run IDs.
2. Selected evidence has two independent human labels and documented
   adjudication.
3. At least one submitted table can be rebuilt without API access.
4. The anonymous export contains no personal paths, author identifiers,
   repository-owner identifiers, credentials, or identifying platform names.
5. A person outside the implementation team has executed the instructions.
