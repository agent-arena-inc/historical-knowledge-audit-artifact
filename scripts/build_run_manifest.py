#!/usr/bin/env python3
"""Build a run-level manifest without modifying the source case export."""

from __future__ import annotations

import argparse
import csv
import hashlib
import re
from dataclasses import dataclass
from pathlib import Path


TRANSCRIPT_RE = re.compile(r"^(?P<prefix>node.+)_run_(?P<index>\d+)_transcript\.md$")


@dataclass(frozen=True)
class Condition:
    condition_id: str
    stage: str
    information_cutoff: str
    config_name: str
    analysis_status: str = "candidate"
    exclusion_reason: str = ""
    notes: str = ""


CONDITIONS: dict[str, dict[str, Condition]] = {
    "usmca": {
        "node1": Condition(
            "historical_case",
            "trade_negotiation",
            "2018-08-27",
            "node1_config.json",
            notes="Named historical setting.",
        ),
        "node1blind": Condition(
            "deidentification_control",
            "trade_negotiation",
            "",
            "node1_blind_config.json",
            notes="Bundled identity, sector, and date transformation; not an isolated identity effect.",
        ),
        "node1pilot": Condition(
            "pilot",
            "trade_negotiation",
            "2018-08-27",
            "node1_config.json",
            analysis_status="excluded",
            exclusion_reason="Pilot run; exclude from confirmatory denominators.",
        ),
        "nodebaseoneshot": Condition(
            "one_shot_baseline",
            "trade_negotiation",
            "2018-08-27",
            "",
            notes="Single-model analyst baseline generated from source notes.",
        ),
        "node2": Condition(
            "ratification_seed_on",
            "domestic_ratification",
            "2019-12-09",
            "node2_config.json",
        ),
        "node2off": Condition(
            "ratification_seed_off",
            "domestic_ratification",
            "2019-12-09",
            "node2_config_seedoff.json",
        ),
        "node3": Condition(
            "downstream_risk_translation",
            "supply_chain_risk",
            "",
            "node3_config.json",
        ),
    },
    "credit_suisse": {
        "node1": Condition(
            "historical_case",
            "weekend_resolution",
            "2023-03-17",
            "node1_config.json",
            notes="Named historical setting.",
        ),
        "node1ctrl": Condition(
            "control",
            "weekend_resolution",
            "2023-03-17",
            "node1_config_nocutoff.json",
            notes="Control label retained from working files; transformation requires verification.",
        ),
        "node1hind": Condition(
            "hindsight_control",
            "weekend_resolution",
            "",
            "node1_config_hindsight.json",
            notes="Hindsight condition; exact supplied information requires verification.",
        ),
        "node1leak": Condition(
            "seeded_positive_control",
            "weekend_resolution",
            "2023-03-17",
            "node1_config_leaky.json",
            notes="Tests detector response; generated outputs require independent labels.",
        ),
        "nodebaseoneshot": Condition(
            "one_shot_baseline",
            "weekend_resolution",
            "2023-03-17",
            "",
            notes="Single-model analyst baseline generated from source notes.",
        ),
        "node2": Condition(
            "litigation_seed_on",
            "post_resolution",
            "",
            "node2_config.json",
        ),
        "node2off": Condition(
            "litigation_seed_off",
            "post_resolution",
            "",
            "node2_config_seedoff.json",
        ),
        "node3": Condition(
            "downstream_risk_translation",
            "insurance_risk",
            "",
            "node3_config.json",
        ),
    },
}


FIELDS = [
    "case_id",
    "condition_id",
    "stage",
    "run_id",
    "run_index",
    "information_cutoff",
    "analysis_status",
    "exclusion_reason",
    "condition_notes",
    "transcript_path",
    "transcript_sha256",
    "trajectory_path",
    "trajectory_sha256",
    "scored_output_path",
    "scored_output_sha256",
    "config_path",
    "config_sha256",
    "run_model_provenance",
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def relative_path(path: Path, source_root: Path) -> str:
    return path.relative_to(source_root).as_posix()


def companion(path: Path, source_root: Path) -> tuple[str, str]:
    if not path.exists():
        return "", ""
    return relative_path(path, source_root), sha256(path)


def build_rows(source_root: Path) -> list[dict[str, str | int]]:
    rows: list[dict[str, str | int]] = []
    for case_id, mappings in CONDITIONS.items():
        case_dir = source_root / case_id
        transcript_dir = case_dir / "run" / "04_Raw_Transcripts"
        output_dir = case_dir / "run" / "05_JSON_Outputs"
        config_dir = case_dir / "run" / "03_Meeting_Configs"
        if not transcript_dir.is_dir():
            raise FileNotFoundError(f"missing transcript directory: {transcript_dir}")

        for transcript in sorted(transcript_dir.glob("*_transcript.md")):
            match = TRANSCRIPT_RE.match(transcript.name)
            if not match:
                continue
            prefix = match.group("prefix")
            if prefix not in mappings:
                raise ValueError(
                    f"unmapped condition prefix {prefix!r} in {transcript}"
                )
            condition = mappings[prefix]
            run_id = transcript.name.removesuffix("_transcript.md")
            trajectory = output_dir / f"{run_id}_trajectory.json"
            scored_output = output_dir / f"{run_id}_output.json"
            config = (
                config_dir / condition.config_name if condition.config_name else None
            )
            transcript_rel, transcript_hash = companion(transcript, source_root)
            trajectory_rel, trajectory_hash = companion(trajectory, source_root)
            output_rel, output_hash = companion(scored_output, source_root)
            config_rel, config_hash = (
                companion(config, source_root) if config else ("", "")
            )

            rows.append(
                {
                    "case_id": case_id,
                    "condition_id": condition.condition_id,
                    "stage": condition.stage,
                    "run_id": run_id,
                    "run_index": int(match.group("index")),
                    "information_cutoff": condition.information_cutoff,
                    "analysis_status": condition.analysis_status,
                    "exclusion_reason": condition.exclusion_reason,
                    "condition_notes": condition.notes,
                    "transcript_path": transcript_rel,
                    "transcript_sha256": transcript_hash,
                    "trajectory_path": trajectory_rel,
                    "trajectory_sha256": trajectory_hash,
                    "scored_output_path": output_rel,
                    "scored_output_sha256": output_hash,
                    "config_path": config_rel,
                    "config_sha256": config_hash,
                    "run_model_provenance": "project_default_only_not_run_pinned",
                }
            )
    return rows


def write_manifest(rows: list[dict[str, str | int]], output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    artifact_root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", type=Path, required=True)
    parser.add_argument(
        "--output",
        type=Path,
        default=artifact_root / "data" / "manifests" / "run_manifest.csv",
    )
    args = parser.parse_args()
    source_root = args.source_root.resolve()
    rows = build_rows(source_root)
    write_manifest(rows, args.output)
    included = sum(row["analysis_status"] != "excluded" for row in rows)
    print(f"wrote {args.output} ({len(rows)} rows; {included} candidate runs)")


if __name__ == "__main__":
    main()
