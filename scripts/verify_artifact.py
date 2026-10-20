#!/usr/bin/env python3
"""Verify required files, manifest hashes, and basic anonymity checks."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import zipfile
from pathlib import Path


REQUIRED_RELEASE_FILES = [
    "README.md",
    "RELEASE_INVENTORY.md",
    "docs/annotation_codebook.md",
    "docs/evidence_reconciliation.md",
    "docs/reproducibility_levels.md",
    "docs/transcript_schema.md",
    "schemas/annotation.schema.json",
    "data/annotations/annotation_template.csv",
    "data/audit_instruments/current_instruments.json",
    "data/manifests/run_manifest.csv",
    "data/derived/provisional_evidence_table.csv",
]


REQUIRED_INTERNAL_FILES = [
    "data/annotations/sample_plan.csv",
    "data/annotations/private_sample_key.csv",
    "data/coder_packets/coder_1/INSTRUCTIONS.md",
    "data/coder_packets/coder_1/coding_sheet.csv",
    "data/coder_packets/coder_1/packet_manifest.csv",
    "data/coder_packets/coder_2/INSTRUCTIONS.md",
    "data/coder_packets/coder_2/coding_sheet.csv",
    "data/coder_packets/coder_2/packet_manifest.csv",
    "data/coder_packets/coder_1_packet.zip",
    "data/coder_packets/coder_2_packet.zip",
]


INTERNAL_ONLY_PATHS = [
    "data/annotations/sample_plan.csv",
    "data/annotations/private_sample_key.csv",
    "data/coder_packets",
    "scripts/build_coder_packets.py",
]


ANONYMITY_PATTERNS = {
    "personal home path": re.compile(r"/(?:Users|home)/[^/\s]+/"),
    "email address": re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.I),
    "author identifier": re.compile(r"\b(?:xiangyu|eugene|yunxiao|sean)\b", re.I),
    "identifying platform name": re.compile(r"\bagent\s*arena\b", re.I),
    "credential-like token": re.compile(r"\bsk-[A-Za-z0-9_-]{12,}\b"),
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def verify_required_files(artifact_root: Path, release_mode: bool) -> list[str]:
    required = [*REQUIRED_RELEASE_FILES]
    if not release_mode:
        required += REQUIRED_INTERNAL_FILES
    return [
        f"missing artifact file: {rel}"
        for rel in required
        if not (artifact_root / rel).is_file()
    ]


def verify_internal_files_absent(artifact_root: Path) -> list[str]:
    return [
        f"internal-only path present in reviewer release: {rel}"
        for rel in INTERNAL_ONLY_PATHS
        if (artifact_root / rel).exists()
    ]


def verify_manifest(artifact_root: Path, source_root: Path) -> list[str]:
    manifest = artifact_root / "data" / "manifests" / "run_manifest.csv"
    if not manifest.exists():
        return [f"missing run manifest: {manifest}"]
    errors: list[str] = []
    path_hash_pairs = [
        ("transcript_path", "transcript_sha256"),
        ("trajectory_path", "trajectory_sha256"),
        ("scored_output_path", "scored_output_sha256"),
        ("config_path", "config_sha256"),
    ]
    seen_run_ids: set[tuple[str, str]] = set()
    with manifest.open(newline="", encoding="utf-8") as stream:
        for row_number, row in enumerate(csv.DictReader(stream), start=2):
            key = (row["case_id"], row["run_id"])
            if key in seen_run_ids:
                errors.append(f"manifest row {row_number}: duplicate run ID {key}")
            seen_run_ids.add(key)
            for path_field, hash_field in path_hash_pairs:
                rel = row.get(path_field, "")
                expected = row.get(hash_field, "")
                if not rel:
                    continue
                target = source_root / rel
                if not target.is_file():
                    errors.append(f"manifest row {row_number}: missing {rel}")
                elif sha256(target) != expected:
                    errors.append(f"manifest row {row_number}: hash mismatch for {rel}")
    if not seen_run_ids:
        errors.append("run manifest contains no data rows")
    return errors


def verify_instruments(artifact_root: Path, source_root: Path) -> list[str]:
    snapshot = artifact_root / "data" / "audit_instruments" / "current_instruments.json"
    if not snapshot.exists():
        return [f"missing audit instrument snapshot: {snapshot}"]
    payload = json.loads(snapshot.read_text(encoding="utf-8"))
    errors: list[str] = []
    for instrument in payload.get("instruments", []):
        rel = instrument.get("source_path", "")
        expected = instrument.get("source_sha256", "")
        target = source_root / rel
        if not target.is_file():
            errors.append(f"missing audit instrument source: {rel}")
        elif sha256(target) != expected:
            errors.append(f"audit instrument hash mismatch: {rel}")
    if not payload.get("instruments"):
        errors.append("audit instrument snapshot contains no instruments")
    return errors


def read_csv_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as stream:
        return list(csv.DictReader(stream))


def verify_coder_packets(artifact_root: Path) -> list[str]:
    errors: list[str] = []
    key_path = artifact_root / "data" / "annotations" / "private_sample_key.csv"
    if not key_path.exists():
        return [f"missing private sample key: {key_path}"]
    key_rows = read_csv_rows(key_path)
    key_ids = {row["sample_id"] for row in key_rows}
    run_ids = {row["sample_id"]: row["run_id"] for row in key_rows}
    if len(key_ids) != len(key_rows):
        errors.append("private sample key contains duplicate sample IDs")

    for coder_id in ("coder_1", "coder_2"):
        packet = artifact_root / "data" / "coder_packets" / coder_id
        manifest_rows = read_csv_rows(packet / "packet_manifest.csv")
        manifest_ids = {row["sample_id"] for row in manifest_rows}
        if manifest_ids != key_ids:
            errors.append(
                f"{coder_id}: packet manifest sample IDs differ from private key"
            )
        coding_ids = {
            row["sample_id"] for row in read_csv_rows(packet / "coding_sheet.csv")
        }
        if coding_ids != key_ids:
            errors.append(
                f"{coder_id}: coding-sheet sample IDs differ from private key"
            )

        for row in manifest_rows:
            for path_field, hash_field in (
                ("transcript_file", "transcript_sha256"),
                ("input_file", "input_sha256"),
            ):
                target = packet / row[path_field]
                if not target.is_file():
                    errors.append(f"{coder_id}: missing packet file {row[path_field]}")
                elif sha256(target) != row[hash_field]:
                    errors.append(f"{coder_id}: hash mismatch for {row[path_field]}")
            transcript = packet / row["transcript_file"]
            if transcript.is_file():
                text = transcript.read_text(encoding="utf-8", errors="replace")
                if run_ids[row["sample_id"]] in text:
                    errors.append(
                        f"{coder_id}: original run ID leaked in {row['transcript_file']}"
                    )
                if re.search(r"\b(?:llm_score|xprov_score|positive_ge_2)\b", text):
                    errors.append(
                        f"{coder_id}: automated-label field leaked in {row['transcript_file']}"
                    )

        archive = artifact_root / "data" / "coder_packets" / f"{coder_id}_packet.zip"
        if archive.is_file():
            with zipfile.ZipFile(archive) as zipped:
                names = set(zipped.namelist())
            if "coding_sheet.csv" not in names:
                errors.append(f"{coder_id}: archive is missing coding_sheet.csv")
            if any("private_sample_key" in name for name in names):
                errors.append(f"{coder_id}: archive contains the private sample key")
    return errors


def verify_anonymity(artifact_root: Path) -> list[str]:
    errors: list[str] = []
    text_suffixes = {".md", ".txt", ".csv", ".json", ".py", ".toml", ".yaml", ".yml"}
    checker_path = Path(__file__).resolve()
    for path in artifact_root.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in text_suffixes:
            continue
        if path.resolve() == checker_path:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for label, pattern in ANONYMITY_PATTERNS.items():
            match = pattern.search(text)
            if match:
                rel = path.relative_to(artifact_root)
                errors.append(f"anonymity check: {label} in {rel}: {match.group(0)!r}")
    return errors


def main() -> None:
    artifact_root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", type=Path, required=True)
    parser.add_argument(
        "--release-mode",
        action="store_true",
        help="verify a reviewer release with internal coding materials removed",
    )
    args = parser.parse_args()

    errors = []
    errors.extend(verify_required_files(artifact_root, args.release_mode))
    errors.extend(verify_manifest(artifact_root, args.source_root.resolve()))
    errors.extend(verify_instruments(artifact_root, args.source_root.resolve()))
    if args.release_mode:
        errors.extend(verify_internal_files_absent(artifact_root))
    else:
        errors.extend(verify_coder_packets(artifact_root))
    errors.extend(verify_anonymity(artifact_root))
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        raise SystemExit(1)
    print("artifact verification passed")


if __name__ == "__main__":
    main()
