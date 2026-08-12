"""Validate the structure of reusable project-control templates."""

from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

EXPECTED_HEADERS = {
    "templates/work-plan.csv": [
        "work_id",
        "phase",
        "work_item",
        "owner",
        "planned_start",
        "planned_finish",
        "predecessor",
        "deliverable_or_exit_condition",
        "status",
        "percent_complete",
        "notes",
    ],
    "templates/stakeholder-register.csv": [
        "stakeholder_id",
        "stakeholder_or_group",
        "role_or_interest",
        "decision_right",
        "influence",
        "impact",
        "information_need",
        "engagement_method",
        "cadence",
        "owner",
        "notes",
    ],
    "templates/risk-register.csv": [
        "risk_id",
        "date_identified",
        "category",
        "risk_statement",
        "probability",
        "impact",
        "exposure",
        "trigger",
        "response_strategy",
        "response_actions",
        "contingency",
        "owner",
        "target_date",
        "status",
        "last_reviewed",
    ],
    "templates/decision-log.csv": [
        "decision_id",
        "date_raised",
        "decision_needed",
        "options_considered",
        "recommendation",
        "decision_owner",
        "decision",
        "decision_date",
        "rationale",
        "affected_requirements",
        "follow_up_owner",
        "follow_up_due",
        "status",
    ],
    "templates/requirements-traceability-matrix.csv": [
        "requirement_id",
        "source",
        "requirement",
        "priority",
        "linked_evaluation_question",
        "planned_evidence",
        "deliverable",
        "acceptance_criteria",
        "verification_owner",
        "status",
        "change_id",
        "notes",
    ],
}

REQUIRED_MARKDOWN = [
    "templates/project-charter.md",
    "templates/evaluation-plan.md",
    "templates/data-management-plan.md",
    "templates/change-request.md",
    "templates/status-report.md",
    "governance/stage-gates.md",
    "governance/definition-of-done.md",
]


def validate_csv(relative_path: str, expected: list[str]) -> None:
    path = ROOT / relative_path
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.reader(handle)
        actual = next(reader)

    if actual != expected:
        raise ValueError(
            f"{relative_path}: header mismatch. "
            f"Expected {expected!r}; received {actual!r}."
        )
    if len(actual) != len(set(actual)):
        raise ValueError(f"{relative_path}: duplicate column name.")


def validate_markdown(relative_path: str) -> None:
    path = ROOT / relative_path
    content = path.read_text(encoding="utf-8")
    if not content.startswith("# "):
        raise ValueError(f"{relative_path}: must begin with a level-one heading.")
    if len(content.splitlines()) < 8:
        raise ValueError(f"{relative_path}: appears incomplete.")


def main() -> None:
    for relative_path, expected in EXPECTED_HEADERS.items():
        validate_csv(relative_path, expected)

    for relative_path in REQUIRED_MARKDOWN:
        validate_markdown(relative_path)

    print(
        f"Validated {len(EXPECTED_HEADERS)} CSV templates and "
        f"{len(REQUIRED_MARKDOWN)} Markdown templates."
    )


if __name__ == "__main__":
    main()
