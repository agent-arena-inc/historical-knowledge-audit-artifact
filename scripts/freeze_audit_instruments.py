#!/usr/bin/env python3
"""Freeze current audit prompts and lexical rules without importing case code."""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
from pathlib import Path
from typing import Any


ASSIGNMENTS = ["JUDGE_1", "JUDGE_2", "HARD_1", "HARD_2"]
CASES = ["usmca", "credit_suisse"]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def extract_literals(path: Path) -> dict[str, Any]:
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    values: dict[str, Any] = {}
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        for target in node.targets:
            if isinstance(target, ast.Name) and target.id in ASSIGNMENTS:
                values[target.id] = ast.literal_eval(node.value)
    missing = set(ASSIGNMENTS) - values.keys()
    if missing:
        raise ValueError(f"{path} is missing literal assignments: {sorted(missing)}")
    return values


def build_snapshot(source_root: Path) -> dict[str, Any]:
    instruments = []
    for case_id in CASES:
        source = source_root / case_id / "contamination_scan.py"
        if not source.is_file():
            raise FileNotFoundError(f"missing audit source: {source}")
        instruments.append(
            {
                "case_id": case_id,
                "source_path": source.relative_to(source_root).as_posix(),
                "source_sha256": sha256(source),
                "assignments": extract_literals(source),
            }
        )
    return {
        "provenance_status": "current_source_snapshot_not_proven_to_match_all_cached_labels",
        "instruments": instruments,
    }


def main() -> None:
    artifact_root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", type=Path, required=True)
    parser.add_argument(
        "--output",
        type=Path,
        default=artifact_root
        / "data"
        / "audit_instruments"
        / "current_instruments.json",
    )
    args = parser.parse_args()
    snapshot = build_snapshot(args.source_root.resolve())
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(snapshot, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(f"wrote {args.output} ({len(snapshot['instruments'])} case instruments)")


if __name__ == "__main__":
    main()
