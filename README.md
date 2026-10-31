# Historical Knowledge Contamination Audit Artifact

This Stage 1 research prototype supports a two-case study of historical
knowledge contamination in LLM-agent simulations. The supplied corpus and
dependency-free scripts reproduce the cached automated results and extract the
existing organizational decision outputs. Independent human coding and the
final inference assessment are planned for the development stage.

## Start here

1. [Technical appendix](TECHNICAL_APPENDIX.md): research question, case
   conditions, methods, and the current scope of reproducibility.
2. [Cached-judgment evidence table](data/derived/provisional_evidence_table.md)
   ([CSV](data/derived/provisional_evidence_table.csv)): the numerical results
   that can be recomputed now. These are automated detector responses, not
   human-verified leakage rates.
3. [Evidence reconciliation](docs/evidence_reconciliation.md) and
   [model provenance](docs/model_provenance.md): denominators, missing records,
   parse failures, and historical invocation gaps.
4. [Run manifest](data/manifests/run_manifest.csv) and
   [decision-output summary](data/derived/decision_output_summary.md): links
   to the source corpus and the 160 extracted focal outputs.
5. Run the instructions below. The [release inventory](RELEASE_INVENTORY.md)
   distinguishes supplied evidence from planned validation.

## Reproduce the supplied results

Use the frozen reviewer ZIP and checksum from the repository's **Releases** page
for submission. **Code → Download ZIP** follows the selected branch and is not a
frozen submission package. Extract the reviewer ZIP and open a
terminal in the extracted directory containing `Makefile` and `README.md`.
Reviewers using the submitted archive can start in its extracted directory.
Python 3.10 or newer and `make` are sufficient:

```bash
make all
```

If `make` is unavailable, run the same existing scripts in order:

```bash
python3 scripts/build_run_manifest.py --source-root data/cases
python3 scripts/freeze_audit_instruments.py --source-root data/cases
python3 scripts/reproduce_provisional_table.py --source-root data/cases
python3 scripts/extract_decision_outputs.py --source-root data/cases
python3 scripts/verify_artifact.py --release-mode --source-root data/cases
```

Expected results are a manifest with 286 rows (280 candidate runs and six
excluded pilots), two current instrument snapshots, 12 cached-judgment summary
rows, 160 focal decision outputs, and the final message
`artifact verification passed`. Generated outputs are in `data/manifests`,
`data/audit_instruments`, and `data/derived`. In a Git checkout,
`git diff --exit-code` should then report no changes.

No network, third-party Python package, API credential, or proprietary
simulation engine is needed for this Level-1 recomputation. Source transcripts
and cached model outputs are not modified. Exact historical audit reruns and
simulation regeneration are separate capabilities, documented in
[reproducibility levels](docs/reproducibility_levels.md).

## Repository layout

| Location | Contents |
|---|---|
| `TECHNICAL_APPENDIX.md` | Methods and current research status |
| `data/cases/` | Supplied transcripts, trajectories, configurations, scores, audit caches, and instrument source |
| `data/manifests/` | Run inventory, source paths, hashes, and provenance reconstruction |
| `data/derived/` | Deterministic cached-result and decision-output tables |
| `data/annotations/` | Human-coding and organizational-inference templates |
| `docs/` | Evidence reconciliation, provenance, codebook, and schema explanations |
| `schemas/` | Machine-readable annotation schema |
| `scripts/` and `Makefile` | Existing recomputation, verification, and release commands |

## Prepare the reviewer archive

The **Verify research artifact** workflow rebuilds the tables, checks that the
outputs are unchanged, stages a reviewer copy without Git metadata or active
coder materials, verifies that copy, and uploads a `reviewer-release` artifact.
For the commit selected for submission, download that artifact from its
successful Actions run and extract the download. The enclosed
`reviewer-release.zip` is the self-contained reviewer package;
`reviewer-release.zip.sha256` records its checksum.

The repository is public. Publish the verified ZIP and checksum as fixed Release
assets for direct download; Actions artifacts are temporary build outputs.
Upload the same ZIP to the submission portal or the editor's review server.
Keep the submitted archive and checksum as the frozen submission version.
The reviewer ZIP excludes Git metadata, workflow configuration, active coder
materials, internal proposal revisions, and the internal submission checklist.

To stage the same package locally, use an empty destination outside this
checkout:

```bash
python3 scripts/stage_release.py --source-root data/cases --destination ../reviewer-release
```

Open the staged directory and run `make all` before distributing it.

## Study status

The current release demonstrates recomputation from the supplied corpus.
Independent human labels, adjudication, and the final organizational-inference
assessment remain development-stage work. Current prompts are supplied;
historical cache-to-invocation linkage and simulation regeneration remain
limited as documented in the appendix and provenance record.

Separate evaluator-blinded coder packets and their private sample key belong
to the internal study workspace and are excluded from the reviewer release.
De-identified adjudicated annotations can be added after coding is frozen.

## External usability evidence

[Test B](docs/usability/test_b.md) records a successful execution from an extracted
reviewer ZIP, with the original returned terminal log and its version limits.

## Worked example and provenance limits

Follow [USMCA run 006](docs/worked_example.md) from its input configuration and
transcript through four cached audit judgments to the extracted organizational
output. The manifest records run IDs, conditions, paths, hashes, and provenance
status. It does not supply complete per-run model invocation configurations.
