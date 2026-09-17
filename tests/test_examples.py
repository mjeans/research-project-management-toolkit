import copy
import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from validate_examples import ROOT, read, validate_plan, moment


class PlanTests(unittest.TestCase):
    def test_bad_dates_and_dependencies_fail(self):
        with self.assertRaises(ValueError):
            moment("2026-02-30")
        source = read(ROOT / "examples/nutrition-evaluation/work-plan.csv")
        for field, value in [("predecessor", "W999"), ("percent_complete", "101"),
                             ("planned_finish", "2026-01-01"), ("predecessor", "W001")]:
            records = copy.deepcopy(source)
            records[0][field] = value
            with self.assertRaises(ValueError):
                validate_plan(records)

    def test_completed_status_requires_full_completion(self):
        records = read(ROOT / "examples/nutrition-evaluation/work-plan.csv")
        records[0]["status"] = "Complete"
        with self.assertRaises(ValueError):
            validate_plan(records)
