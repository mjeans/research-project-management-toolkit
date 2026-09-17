"""Semantic validation of worked plans, in addition to blank template structure."""
import csv
from datetime import date
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def read(path):
    with path.open(encoding="utf-8", newline="") as stream:
        rows = list(csv.DictReader(stream))
    if any(None in row or any(v is None for v in row.values()) for row in rows):
        raise ValueError(f"Malformed CSV row: {path}")
    return rows


def moment(value):
    if re.fullmatch(r"Week [1-9][0-9]*", value):
        return "relative", int(value[5:])
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        raise ValueError(f"Use ISO dates or explicit Week N: {value}")
    return "calendar", date.fromisoformat(value).toordinal()


def ordered(first, last):
    a, b = moment(first), moment(last)
    if a[0] != b[0] or a[1] > b[1]:
        raise ValueError(f"Inconsistent chronology: {first} to {last}")


def validate_plan(work):
    ids = {r["work_id"] for r in work}
    if len(ids) != len(work):
        raise ValueError("Duplicate work ID")
    by_id = {r["work_id"]: r for r in work}
    graph = {}
    for row in work:
        ordered(row["planned_start"], row["planned_finish"])
        percent = float(row["percent_complete"])
        if not 0 <= percent <= 100:
            raise ValueError("Completion must be 0–100")
        if row["status"] == "Complete" and percent != 100:
            raise ValueError("Complete work must be 100%")
        if row["status"] == "Not started" and percent != 0:
            raise ValueError("Not-started work must be 0%")
        predecessors = list(filter(None, row["predecessor"].split(";")))
        graph[row["work_id"]] = predecessors
        for previous in predecessors:
            if previous not in ids:
                raise ValueError(f"Unknown predecessor: {previous}")
            ordered(by_id[previous]["planned_finish"], row["planned_start"])
    def visit(node, trail):
        if node in trail:
            raise ValueError("Cyclic work dependencies")
        for parent in graph[node]:
            visit(parent, trail | {node})
    for node in ids:
        visit(node, set())


def validate_example(folder):
    work = read(folder / "work-plan.csv")
    validate_plan(work)
    risks = read(folder / "risk-register.csv")
    if len({r["risk_id"] for r in risks}) != len(risks):
        raise ValueError("Duplicate risk ID")
    scale = {"Low": 1, "Medium": 2, "High": 3}
    for r in risks:
        ordered(r["date_identified"], r["target_date"])
        ordered(r["date_identified"], r["last_reviewed"])
        product = scale[r["probability"]] * scale[r["impact"]]
        expected = "High" if product >= 6 else "Medium" if product >= 3 else "Low"
        if r["exposure"] != expected or not r["owner"] or not r["trigger"]:
            raise ValueError("Inconsistent exposure or missing risk ownership/trigger")
    path = folder / "requirements-traceability-matrix.csv"
    if path.exists():
        requirements = read(path)
        if len({r["requirement_id"] for r in requirements}) != len(requirements):
            raise ValueError("Duplicate requirement ID")
        charter = (folder / "charter.md").read_text(encoding="utf-8")
        deliverables = {r["deliverable_or_exit_condition"] for r in work}
        for r in requirements:
            if r["deliverable"] not in deliverables or r["deliverable"] not in charter:
                raise ValueError("Untraced deliverable")
            if r["linked_evaluation_question"] not in charter or r["notes"] not in {w["work_id"] for w in work}:
                raise ValueError("Untraced question/work ID")


if __name__ == "__main__":
    for folder in sorted((ROOT / "examples").iterdir()):
        if folder.is_dir():
            validate_example(folder)
            print(f"Validated semantic controls: {folder.name}")
