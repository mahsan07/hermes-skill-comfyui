#!/usr/bin/env python3
"""Validate the local harness manifest without third-party dependencies."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "harness" / "manifest.json"


def validate(data: dict) -> list[str]:
    errors: list[str] = []
    required = {
        "protocol_version", "skill", "task_profile", "modules", "execution",
        "verification", "failure_policy", "maturity",
    }
    missing = sorted(required - data.keys())
    if missing:
        errors.append(f"missing top-level fields: {', '.join(missing)}")
    if data.get("protocol_version") != "0.1":
        errors.append("protocol_version must be 0.1")
    modules = data.get("modules", {})
    for name in ("memory", "planning", "action", "capability"):
        module = modules.get(name)
        if not isinstance(module, dict):
            errors.append(f"modules.{name} must be an object")
        elif not module.get("strategy") or not module.get("responsibility"):
            errors.append(f"modules.{name} requires strategy and responsibility")
    stages = data.get("execution", {}).get("stages", [])
    if not isinstance(stages, list) or len(stages) < 2:
        errors.append("execution.stages must contain at least two stages")
    if data.get("failure_policy", {}).get("max_repairs", 99) not in range(0, 4):
        errors.append("failure_policy.max_repairs must be between 0 and 3")
    if data.get("maturity", {}).get("runtime_scope") != "validation_and_dry_run_planning":
        errors.append("runtime_scope must remain validation_and_dry_run_planning")
    return errors


def main() -> int:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    errors = validate(data)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"VALID: {data['skill']['id']} ({len(data['execution']['stages'])} stages)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
