#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class HarnessContractTest(unittest.TestCase):
    def test_manifest_validates(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "validate_harness.py")],
            cwd=ROOT, capture_output=True, text=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_example_produces_dry_run_receipt(self):
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "receipt.json"
            result = subprocess.run(
                [sys.executable, str(ROOT / "scripts" / "run_harness.py"),
                 str(ROOT / "examples" / "task.json"), "--output", str(output)],
                cwd=ROOT, capture_output=True, text=True,
            )
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            receipt = json.loads(output.read_text(encoding="utf-8"))
            manifest = json.loads((ROOT / "harness" / "manifest.json").read_text(encoding="utf-8"))
            self.assertEqual(receipt["skill_id"], manifest["skill"]["id"])
            self.assertEqual(receipt["status"], "planned_not_executed")
            self.assertEqual(receipt["planned_stages"], manifest["execution"]["stages"])
            self.assertEqual(set(receipt["selected_modules"]), {"memory", "planning", "action", "capability"})


if __name__ == "__main__":
    unittest.main()
