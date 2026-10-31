#!/usr/bin/env python3
"""Create a self-contained Level-1 release from the verified working artifact."""

from __future__ import annotations

import argparse
import csv
import json
import shutil
from pathlib import Path


MANIFEST_PATH_FIELDS = [
    "transcript_path",
    "trajectory_path",
    "scored_output_path",
    "config_path",
]

INTERNAL_ONLY_PATHS = {
    Path("data/annotations/private_sample_key.csv"),
    Path("data/annotations/sample_plan.csv"),
    Path("scripts/build_coder_packets.py"),
    Path("docs/proposal_corrections.md"),
    Path("SUBMISSION_CHECKLIST.md"),
}


def is_internal_only(rel: Path) -> bool:
    return (
        rel in INTERNAL_ONLY_PATHS
        or rel.parts[:2] == ("data", "coder_packets")
        or ".github" in rel.parts
    )


def require_empty_destination(destination: Path) -> None:
    if destination.exists() and any(destination.iterdir()):
        raise FileExistsError(f"destination must be absent or empty: {destination}")
    destination.mkdir(parents=True, exist_ok=True)


def copy_artifact_code(artifact_root: Path, destination: Path) -> None:
    for source in artifact_root.rglob("*"):
        if not source.is_file():
            continue
        rel = source.relative_to(artifact_root)
        if (
            ".git" in rel.parts
            or "__pycache__" in rel.parts
            or ".ruff_cache" in rel.parts
            or rel.suffix == ".pyc"
            or is_internal_only(rel)
        ):
            continue
        target = destination / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)


def manifest_paths(artifact_root: Path) -> set[str]:
    manifest = artifact_root / "data" / "manifests" / "run_manifest.csv"
    paths: set[str] = set()
    with manifest.open(newline="", encoding="utf-8") as stream:
        for row in csv.DictReader(stream):
            for field in MANIFEST_PATH_FIELDS:
                if row.get(field):
                    paths.add(row[field])

    cached = artifact_root / "data" / "derived" / "provisional_evidence_table.csv"
    with cached.open(newline="", encoding="utf-8") as stream:
        for row in csv.DictReader(stream):
            if row.get("source_path"):
                paths.add(row["source_path"])

    instruments = (
        artifact_root / "data" / "audit_instruments" / "current_instruments.json"
    )
    payload = json.loads(instruments.read_text(encoding="utf-8"))
    for instrument in payload.get("instruments", []):
        if instrument.get("source_path"):
            paths.add(instrument["source_path"])
    return paths


def copy_case_files(artifact_root: Path, source_root: Path, destination: Path) -> int:
    copied = 0
    for rel in sorted(manifest_paths(artifact_root)):
        source = source_root / rel
        if not source.is_file():
            raise FileNotFoundError(f"manifested source file is missing: {source}")
        target = destination / "data" / "cases" / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
        copied += 1
    return copied


def main() -> None:
    artifact_root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", type=Path, required=True)
    parser.add_argument("--destination", type=Path, required=True)
    args = parser.parse_args()

    source_root = args.source_root.resolve()
    destination = args.destination.resolve()
    require_empty_destination(destination)
    copy_artifact_code(artifact_root, destination)
    copied = copy_case_files(artifact_root, source_root, destination)
    print(f"staged {destination} with {copied} case files")
    print(
        "verify with: python scripts/verify_artifact.py "
        f"--release-mode --source-root {destination / 'data' / 'cases'}"
    )


if __name__ == "__main__":
    main()
