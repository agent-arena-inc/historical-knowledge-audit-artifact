# Transcript schema

## File identity

Each transcript filename has the form:

```text
<condition>_run_<three-digit-index>_transcript.md
```

The run manifest supplies the case, condition, run index, related trajectory,
related scored output, configuration, inclusion status, and SHA-256 hashes.

## Observed record types

The Markdown transcripts contain the following logical records:

| Record | Typical representation | Required fields for annotation |
|---|---|---|
| Discussion statement | `**[R#] actor** ...: text` | round, actor, text |
| Speech | `**[R#] actor** [speech]: text` | round, actor, text |
| Proposal | `**[R#] actor** [PROPOSAL]: text` | round, actor, text |
| Proposal reaction | actor reaction line | round, actor, proposer, text |
| Game-master ruling | blockquote beginning with `GM` | round, target actor, outcome, text |
| Stage transition | Markdown heading | stage index, stage name |
| Round end | italicized state snapshot | round, termination status, state values |

## Stable annotation locator

Until a normalized turn-level JSONL export is produced, an annotated excerpt
must be located by all of the following:

- `case_id`
- `condition_id`
- `run_id`
- `round_id`
- `actor_id`
- `excerpt_sha256`
- the verbatim excerpt in the annotation table

Line numbers alone are not stable identifiers because transcripts may be
reformatted without changing their content.

## Known limitations

- Some spoken content appears both as a discussion statement and as a speech
  event. Coders must not count duplicated rendering as two independent claims.
- Game-master summaries may repeat agent content. The first-introducer field
  should identify the earliest actor-level occurrence, not a later summary.
- A transcript does not by itself establish which fact was present in model
  pretraining. The audit concerns observable output relative to a specified
  information boundary.

