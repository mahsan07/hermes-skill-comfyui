#!/usr/bin/env python3
"""Emit a deterministic, side-effect-free execution plan for this skill."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("task", type=Path, help="JSON task containing a non-empty 'task' string")
    parser.add_argument("--output", type=Path, help="Optional path for the generated receipt")
    args = parser.parse_args()

    manifest = json.loads((ROOT / "harness" / "manifest.json").read_text(encoding="utf-8"))
    request = json.loads(args.task.read_text(encoding="utf-8"))
    task = request.get("task")
    if not isinstance(task, str) or not task.strip():
        raise SystemExit("task JSON must contain a non-empty 'task' string")

    receipt = {
        "protocol_version": manifest["protocol_version"],
        "skill_id": manifest["skill"]["id"],
        "mode": "dry_run",
        "task": task.strip(),
        "selected_modules": {
            name: value["strategy"] for name, value in manifest["modules"].items()
        },
        "planned_stages": manifest["execution"]["stages"],
        "required_gates": manifest["execution"]["gates"],
        "expected_evidence": manifest["verification"]["evidence"],
        "status": "planned_not_executed",
        "claim_boundary": manifest["maturity"]["claim_boundary"],
    }
    rendered = json.dumps(receipt, indent=2, ensure_ascii=True) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
