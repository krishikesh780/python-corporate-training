"""
Week 2 — Day 5: Capstone — JSON & Data Comparison
==================================================

PYTHON CLASSROOM
----------------
1. Nested dict / list (records)
2. Dict comprehension for lookup by key
3. compare_customers(old, new) algorithm
4. json.dumps for readable report
5. Project file: day5/project2/insurance.py
6. Practice P1–P5

PYTHON RECALL
-------------
- JSON keys must be strings; Python dict keys can be any hashable type.
- Build index: {row["id"]: row for row in rows} for O(1) lookup.
- Separate "name change" vs "policy change" in reports.
- Reuse functions + modules from Days 1–4 (no duplicate lessons).
"""

import json
import sys
from pathlib import Path

_PROJECT_DIR = Path(__file__).resolve().parent / "day5" / "project2"
if str(_PROJECT_DIR) not in sys.path:
    sys.path.insert(0, str(_PROJECT_DIR))

import insurance  # noqa: E402


def demo_nested_records() -> None:
    sample = insurance.INSURANCE_DATA["old_database"]["customers"][0]
    print("Single record keys:", list(sample.keys()))
    print("Sample:", sample)


def demo_index_pattern() -> None:
    customers = insurance.INSURANCE_DATA["old_database"]["customers"]
    by_policy = {c["policy_number"]: c["name"] for c in customers}
    print("Policy → name index:", by_policy)


def demo_compare_report() -> None:
    report = insurance.run_comparison()
    print("Report summary:")
    for section, rows in report.items():
        print(f"  {section}: {len(rows)}")
    print("\nFull JSON:")
    print(json.dumps(report, indent=2))


# P1: Count total premium in old vs new DB (sum in a function).
# P2: List only Health policies in new DB (filter).
# P3: Export report to report.json (open, write, json.dump).
# P4: Add validate_customer(record) for required keys.
# P5: Unit-test compare_customers with 2-row toy data.

def run_classroom_demo() -> None:
    demo_nested_records()
    demo_index_pattern()
    demo_compare_report()


if __name__ == "__main__":
    run_classroom_demo()