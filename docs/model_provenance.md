# Model and execution provenance status

This file records what the supplied corpus can and cannot currently establish.
It prevents provider labels in cached audit files from being mistaken for
complete run provenance.

## Reconstructed execution windows

Filesystem timestamps in the supplied working export place the four primary
trajectory series in these windows. Timestamps are supporting metadata, not an
immutable execution log.

| Case and stage | Trajectory timestamp window |
|---|---|
| Credit Suisse weekend rescue | 2026-06-07 23:12 to 2026-06-08 18:31 (UTC-04:00) |
| Credit Suisse creditor reaction | 2026-06-09 16:46 to 2026-06-09 17:50 (UTC-04:00) |
| USMCA trade negotiation | 2026-06-25 18:11 to 2026-06-27 04:15 (UTC-04:00) |
| USMCA ratification pressure | 2026-06-26 11:51 to 2026-06-26 12:48 (UTC-04:00) |

The closest settings snapshot committed before these timestamp windows routes
agent turns to `anthropic/claude-haiku-4-5-20251001`, GM arbitration to
`anthropic/claude-sonnet-4-5-20250929`, and classification to
`anthropic/claude-3-haiku-20240307`. The batch runner routes those three tasks
through the corresponding settings profiles and applies an evenly spaced
agent-temperature jitter whose CLI defaults are 0.7 to 0.95.

This is a **medium-confidence reconstruction**, not run-level proof. The
candidate settings are recorded in
`data/manifests/provenance_reconstruction.csv` and must not be described as
exactly pinned unless invocation logs are recovered.

## Simulation runs

The run manifest identifies each transcript, trajectory, scored output,
configuration, information cutoff, and file hash. The exported run files do not
pin a provider/model invocation, decoding parameters, API date, or code commit
for each simulation run. The manifest therefore labels simulation provenance as
`project_default_only_not_run_pinned`.

Until stronger records are recovered, the artifact supports recomputation from
the supplied corpus but not exact regeneration of the original simulations.

## Decision-output extraction

The supplied extractor routes transcript summarization and marker scoring to the
`report` profile. The closest pre-run settings snapshot assigns that profile to
`anthropic/claude-sonnet-4-5-20250929`, temperature 0.3, and maximum output 8192
tokens. A source-code comment instead says temperature 0.1, while the executable
call does not override the settings value. Because the historical invocation
log is absent, the discrepancy remains documented rather than silently resolved.

## Cached audit judgments

The cache filenames identify these evaluator families:

| Cache label | Supplied identifier | Current limitation |
|---|---|---|
| Report judge | `cached_anthropic_report_judge` | Exact model invocation and historical prompt hash are not pinned in every cache. |
| Haiku judge | `cached_anthropic_haiku_judge` | One eligible USMCA run is absent; invocation metadata are incomplete. |
| OpenAI cross-provider judge | `cached_openai/gpt-5.5` | Provider/model label is present; one USMCA run is absent and one attempted result does not parse. |
| Google cross-provider judge | `cached_google/gemini-3.1-pro-preview` | Provider/model label is present; one USMCA run is absent and one attempted result does not parse. |

`data/audit_instruments/current_instruments.json` freezes the prompts and lexical
rules found in the current source export. Its provenance status explicitly says
that these current instruments have not been proven to match every historical
cached label.

## Required recovery record

Before claiming Level-2 audit rerunnability, add a machine-readable record with:

- cache filename and SHA-256;
- provider and exact model identifier;
- execution date;
- prompt or source-code SHA-256;
- temperature, seed when supported, token limit, and other decoding settings;
- parser version and failure policy;
- attempted run IDs; and
- approximate API cost and access requirements.

If an item cannot be recovered, mark it `unknown` rather than filling it from a
current project default.
