# Stage 1 submission checklist

This checklist separates the supplied prototype, the submission handoff, and
the development-stage research plan. Pending validation is not described as
completed evidence.

## Supplied prototype

- [x] Self-contained two-case corpus export.
- [x] Run manifest with source hashes and explicit candidate/pilot status.
- [x] Deterministic reconstruction of the 12-row cached-judgment table.
- [x] Snapshot of current audit prompts and lexical rules.
- [x] Annotation codebook, blank coding template, and organizational-inference
      template with pending fields.
- [x] Harmonized table for the 160 existing focal decision outputs.
- [x] Model-provenance record with unresolved invocation fields kept explicit.
- [x] Dependency-free Level-1 recomputation (`make all`) and continuous
      verification on pushes and pull requests.
- [x] Reviewer reading order, direct evidence links, and expected outputs.
- [x] Release staging excludes Git metadata and active coder materials.
- [x] Verification workflow builds and verifies a reviewer ZIP and checksum.
- [x] Technical appendix distinguishes current capabilities from planned work.

## Final submission handoff

- [ ] Freeze the final merged commit as Release `stage1-2026-10-31` after CI passes.
- [ ] Confirm preliminary numerical claims in the submitted proposal and
      appendix match the generated cached-judgment table and its denominators.
      Do not use an unreproduced lexical tally as a verified headline result.
- [ ] Upload the verified `reviewer-release.zip` to the submission portal or
      editor's review server; confirm the submitted materials are accessible
      through the portal or the fixed public Release assets.
- [ ] Check the submitted proposal, appendix, and document metadata for author
      identifiers. Keep the archive and checksum as the frozen submission copy.

The anonymity checker scans all supported text files, including its own source.
For author-specific checks, use `--identity-blocklist /path/to/private-list.txt`
with one identifier per line. Keep this private file outside the artifact and
never include it in the reviewer archive. Generic checks run without this option.

## Development-stage research plan

These items remain planned work; this release does not claim their completion.

- [ ] Obtain independent human labels and preserve each coder's original file.
- [ ] Adjudicate disagreements and publish de-identified labels and a log.
- [ ] Complete the validated evidence and organizational-conclusion tables.
- [ ] Recover historical audit invocation details where available before
      claiming faithful Level-2 rerunnability; otherwise retain the documented
      limits.
- [ ] Establish an executable or controlled-access arrangement before offering
      Level-3 simulation regeneration.
- [x] Record an external user's execution as a usability check: [Test B](docs/usability/test_b.md)
      and its original terminal log. Exact tested revision was not captured;
      this record does not claim an external rerun of the anonymity repair.

## Interpretation of the preliminary evidence

Cached model counts describe detector responses, not human-verified leakage
rates. Seeded inputs do not by themselves establish positive generated outputs.
The existing de-identification condition is a bundled transformation; stability
under it supports robustness within that tested condition. These distinctions
are already part of the proposed validation method.
