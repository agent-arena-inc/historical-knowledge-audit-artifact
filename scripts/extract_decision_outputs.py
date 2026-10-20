#!/usr/bin/env python3
"""Extract existing organizational decision outputs into a harmonized table."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from collections import Counter
from pathlib import Path


SERIES = [
    {
        "case_id": "usmca",
        "stage": "trade_negotiation",
        "prefix": "node1",
        "markers": ["labor_enforcement_key", "ratification_risk"],
    },
    {
        "case_id": "usmca",
        "stage": "ratification_pressure",
        "prefix": "node2",
        "markers": ["labor_enforcement_pressure", "ratification_risk", "agreement_stability"],
    },
    {
        "case_id": "credit_suisse",
        "stage": "weekend_rescue",
        "prefix": "node1",
        "markers": ["ubs_rescue_path", "at1_tail_risk", "capital_structure_conflict"],
    },
    {
        "case_id": "credit_suisse",
        "stage": "creditor_reaction",
        "prefix": "node2",
        "markers": ["litigation_likelihood", "creditor_hierarchy_controversy", "claims_tail"],
    },
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def matching_outputs(source_root: Path, case_id: str, prefix: str) -> list[Path]:
    output_dir = source_root / case_id / "run" / "05_JSON_Outputs"
    pattern = re.compile(rf"^{re.escape(prefix)}_run_\d{{3}}_output\.json$")
    return [path for path in sorted(output_dir.glob(f"{prefix}_run_*_output.json")) if pattern.match(path.name)]


def collect_rows(source_root: Path) -> tuple[list[dict[str, str]], dict[tuple[str, str], list[str]]]:
    rows: list[dict[str, str]] = []
    selected: dict[tuple[str, str], list[str]] = {}
    for spec in SERIES:
        case_id = spec["case_id"]
        stage = spec["stage"]
        prefix = spec["prefix"]
        selected[(case_id, stage)] = spec["markers"]
        for output_path in matching_outputs(source_root, case_id, prefix):
            payload = json.loads(output_path.read_text(encoding="utf-8"))
            run_id = payload.get("meeting_id") or output_path.name.removesuffix("_output.json")
            transcript_rel = f"{case_id}/run/04_Raw_Transcripts/{run_id}_transcript.md"
            trajectory_rel = f"{case_id}/run/05_JSON_Outputs/{run_id}_trajectory.json"
            trajectory_path = source_root / trajectory_rel
            final_outcome: dict = {}
            if trajectory_path.is_file():
                trajectory = json.loads(trajectory_path.read_text(encoding="utf-8"))
                final_outcome = trajectory.get("final_outcome") or {}
            output_rel = output_path.relative_to(source_root).as_posix()
            rows.append(
                {
                    "case_id": case_id,
                    "stage": stage,
                    "run_id": run_id,
                    "dominant_path": str(payload.get("dominant_path", "")),
                    "final_recommendation": str(payload.get("final_recommendation", "")),
                    "trajectory_outcome": str(final_outcome.get("type", "")),
                    "round_ended": str(final_outcome.get("round_ended", "")),
                    "marker_scores_json": json.dumps(payload.get("markers") or {}, sort_keys=True, ensure_ascii=False),
                    "marker_evidence_json": json.dumps(
                        payload.get("marker_evidence") or {}, sort_keys=True, ensure_ascii=False
                    ),
                    "transcript_path": transcript_rel,
                    "trajectory_path": trajectory_rel,
                    "output_path": output_rel,
                    "output_sha256": sha256(output_path),
                    "output_label_status": "cached_report_model_not_human_adjudicated",
                }
            )
    return rows, selected


def render_summary(rows: list[dict[str, str]], selected: dict[tuple[str, str], list[str]]) -> str:
    lines = [
        "# Existing organizational decision outputs",
        "",
        "This summary is mechanically extracted from the supplied run-level output JSON files. "
        "The paths and marker scores were produced by a cached report-model pass and are not "
        "human-adjudicated contamination labels.",
        "",
    ]
    for spec in SERIES:
        key = (spec["case_id"], spec["stage"])
        subset = [row for row in rows if (row["case_id"], row["stage"]) == key]
        n = len(subset)
        lines.extend([f"## {spec['case_id']} — {spec['stage']} ({n} runs)", "", "Dominant paths:"])
        for path, count in Counter(row["dominant_path"] for row in subset).most_common():
            lines.append(f"- `{path}`: {count}/{n} ({count / n:.1%})")
        lines.extend(["", "Selected marker distributions:", "", "| Marker | Mean | At scale maximum | Present (>0) |", "|---|---:|---:|---:|"])
        decoded = [json.loads(row["marker_scores_json"]) for row in subset]
        for marker in selected[key]:
            values = [int(item.get(marker, 0)) for item in decoded]
            maximum = max(values) if values else 0
            lines.append(
                f"| `{marker}` | {sum(values) / n:.2f} | "
                f"{sum(value == maximum for value in values)}/{n} (max={maximum}) | "
                f"{sum(value > 0 for value in values)}/{n} |"
            )
        lines.append("")
    lines.extend(
        [
            "The full recommendations, marker evidence, source paths, and output hashes are in "
            "`decision_outputs.csv`. Stability here describes the cached output representation; "
            "inferential robustness still depends on the information-control and human-audit comparisons.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    artifact_root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", type=Path, default=artifact_root / "data" / "cases")
    args = parser.parse_args()

    rows, selected = collect_rows(args.source_root.resolve())
    output_dir = artifact_root / "data" / "derived"
    output_dir.mkdir(parents=True, exist_ok=True)
    csv_path = output_dir / "decision_outputs.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    summary_path = output_dir / "decision_output_summary.md"
    summary_path.write_text(render_summary(rows, selected), encoding="utf-8")
    print(f"wrote {csv_path} and {summary_path} ({len(rows)} run-level outputs)")


if __name__ == "__main__":
    main()
