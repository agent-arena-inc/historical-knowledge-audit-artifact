# Model and execution provenance status

This file records what the supplied corpus can and cannot currently establish.
It prevents provider labels in cached audit files from being mistaken for
complete run provenance.

## Simulation runs

The run manifest identifies each transcript, trajectory, scored output,
configuration, information cutoff, and file hash. The exported run files do not
pin a provider/model invocation, decoding parameters, API date, or code commit
for each simulation run. The manifest therefore labels simulation provenance as
`project_default_only_not_run_pinned`.

Until stronger records are recovered, the artifact supports recomputation from
the supplied corpus but not exact regeneration of the original simulations.

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
