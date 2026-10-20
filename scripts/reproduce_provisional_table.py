#!/usr/bin/env python3
"""Summarize cached audit judgments without making validity claims."""

from __future__ import annotations

import argparse
import csv
import json
from collections import defaultdict
from pathlib import Path
from typing import Any


FIELDS = [
    "case_id",
    "condition_id",
    "evaluator",
    "source_path",
    "corpus_total",
    "attempted_records",
    "valid_labels",
    "positive_ge_2",
    "missing_from_corpus",
    "parse_failures",
    "keyword_positive",
    "verification_status",
]


INPUTS = {
    "usmca": [
        ("contamination_scan_1.json", "cached_anthropic_report_judge"),
        ("contamination_scan_1_haiku.json", "cached_anthropic_haiku_judge"),
        ("cross_provider_judge_openai_gpt-5.5.json", "model_from_file"),
        ("cross_provider_judge_google_gemini-3.1-pro-preview.json", "model_from_file"),
    ],
    "credit_suisse": [
        (
            "contamination_scan_1_1ctrl_1hind_1leak.json",
            "cached_anthropic_report_judge",
        ),
        ("cross_provider_judge_openai_gpt-5.5.json", "model_from_file"),
        ("cross_provider_judge_google_gemini-3.1-pro-preview.json", "model_from_file"),
    ],
}


CONDITION_IDS = {
    ("usmca", "1"): "historical_case",
    ("usmca", "1blind"): "deidentification_control",
    ("credit_suisse", "1"): "historical_case",
    ("credit_suisse", "1ctrl"): "control",
    ("credit_suisse", "1hind"): "hindsight_control",
    ("credit_suisse", "1leak"): "seeded_positive_control",
}


CORPUS_TOTALS = {
    ("usmca", "1"): 50,
    ("usmca", "1blind"): 30,
    ("credit_suisse", "1"): 50,
    ("credit_suisse", "1ctrl"): 4,
    ("credit_suisse", "1hind"): 5,
    ("credit_suisse", "1leak"): 5,
}


def load_records(payload: dict[str, Any]) -> tuple[list[dict[str, Any]], str]:
    if "runs" in payload:
        return payload["runs"], "llm_score"
    if "contamination" in payload:
        return payload["contamination"], "xprov_score"
    raise ValueError("cached judgment file has neither 'runs' nor 'contamination'")


def evaluator_name(payload: dict[str, Any], fallback: str) -> str:
    if fallback != "model_from_file":
        return fallback
    model = payload.get("model")
    if not model:
        raise ValueError("cross-provider file is missing its model identifier")
    return f"cached_{model}"


def summarize_file(
    case_id: str, path: Path, source_root: Path, fallback: str
) -> list[dict[str, Any]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    records, score_key = load_records(payload)
    groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for record in records:
        groups[str(record.get("node", "unknown"))].append(record)

    rows = []
    for node, group in sorted(groups.items()):
        scores = [record.get(score_key) for record in group]
        valid = [score for score in scores if isinstance(score, int) and score >= 0]
        corpus_total = CORPUS_TOTALS.get((case_id, node), len(group))
        rows.append(
            {
                "case_id": case_id,
                "condition_id": CONDITION_IDS.get(
                    (case_id, node), f"working_node_{node}"
                ),
                "evaluator": evaluator_name(payload, fallback),
                "source_path": path.relative_to(source_root).as_posix(),
                "corpus_total": corpus_total,
                "attempted_records": len(group),
                "valid_labels": len(valid),
                "positive_ge_2": sum(score >= 2 for score in valid),
                "missing_from_corpus": max(0, corpus_total - len(group)),
                "parse_failures": len(group) - len(valid),
                "keyword_positive": sum(
                    (record.get("kw_total") or 0) > 0 for record in group
                ),
                "verification_status": "provisional_not_human_verified",
            }
        )
    return rows


def collect_rows(source_root: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for case_id, files in INPUTS.items():
        aggregation = source_root / case_id / "run" / "06_Aggregation"
        for filename, evaluator in files:
            path = aggregation / filename
            if not path.exists():
                raise FileNotFoundError(f"missing cached judgment file: {path}")
            rows.extend(summarize_file(case_id, path, source_root, evaluator))
    return rows


def write_csv(rows: list[dict[str, Any]], output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)


def write_markdown(rows: list[dict[str, Any]], output: Path) -> None:
    lines = [
        "# Provisional cached-judgment counts",
        "",
        "These counts are mechanically recomputed from cached model judgments. They are not human-verified leakage rates.",
        "",
        "| Case | Condition | Evaluator | Corpus | Attempted | Valid | Score >= 2 | Missing | Parse failures | Keyword-positive |",
        "|---|---|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            "| {case_id} | {condition_id} | {evaluator} | {corpus_total} | "
            "{attempted_records} | {valid_labels} | {positive_ge_2} | "
            "{missing_from_corpus} | {parse_failures} | {keyword_positive} |".format(
                **row
            )
        )
    lines.extend(
        [
            "",
            "Do not cite this table as a validated false-negative rate. Denominators, prompt versions, and human labels must be reconciled first.",
        ]
    )
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    artifact_root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", type=Path, required=True)
    parser.add_argument(
        "--csv-output",
        type=Path,
        default=artifact_root / "data" / "derived" / "provisional_evidence_table.csv",
    )
    parser.add_argument(
        "--markdown-output",
        type=Path,
        default=artifact_root / "data" / "derived" / "provisional_evidence_table.md",
    )
    args = parser.parse_args()
    rows = collect_rows(args.source_root.resolve())
    write_csv(rows, args.csv_output)
    write_markdown(rows, args.markdown_output)
    print(f"wrote {args.csv_output} and {args.markdown_output} ({len(rows)} rows)")


if __name__ == "__main__":
    main()
