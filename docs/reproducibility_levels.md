# Reproducibility levels

## Level 1: Recompute reported analyses

Required materials:

- immutable transcripts and trajectory files;
- cached automated judgments;
- human annotations and adjudication records;
- a run manifest with exclusions and file hashes;
- deterministic aggregation scripts; and
- expected tables for comparison.

This level verifies what follows from the supplied corpus. It does not require
an API key or access to the simulation engine.

## Level 2: Rerun audit instruments

Required additional materials:

- exact audit prompts;
- provider and model identifiers;
- decoding parameters and output limits;
- date of execution;
- parser behavior and failure handling; and
- expected API access and approximate cost.

Fresh calls may differ from cached labels. Such variation must be reported, not
silently substituted into the submitted result.

## Level 3: Regenerate simulations

Required additional materials:

- scenario inputs and agent objectives;
- information cutoffs and visibility rules;
- model routing and generation parameters;
- control transformations;
- executable engine access or a workable controlled-access arrangement; and
- procedures for assigning regenerated runs to analysis conditions.

Claims about the effect of a simulation control require this level or must be
narrowed to the supplied runs.

