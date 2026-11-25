"""
Week 5 — Day 5: Capstone — SQL Regression Report
================================================

PYTHON CLASSROOM
----------------
1. Flow: queries.xlsx → SQL → sample.db → validators
2. Write data/report.xlsx
3. setup_db.py seeds intentional duplicate row
4. Tie-in: GitHub CI (week4/day4) + assessment
5. Practice P1–P5

PYTHON RECALL
-------------
- Week map: D1 SQLite → D2 loader → D3 validators → D4 JSON CMS → D5 report.
- Do not confuse project4 (JSON) with Project5 (SQL regression).
- pandas Excel: week3/day5 patterns for reports only.
"""

import subprocess
import sys
from pathlib import Path

_PROJECT5 = Path(__file__).resolve().parent / "Project5"


def demo_pipeline_overview() -> None:
    print("1. setup_db.py → data/sample.db")
    print("2. load queries.xlsx + replace {DATE}, {STATUS}")
    print("3. validators → DataFrame → data/report.xlsx")


def demo_run_regression() -> Path | None:
    if str(_PROJECT5) not in sys.path:
        sys.path.insert(0, str(_PROJECT5))

    from setup_db import setup_database

    setup_database()

    from main import run_regression_report

    report = run_regression_report()
    print("Report saved:", report)
    return report


# PYTHON RECALL — Practice (P1–P5)
# P1: Add Alive_List query to queries.xlsx and handler.
# P2: Export report to CSV as well.
# P3: Hook pytest to assert duplicate count > 0.
# P4: Move DB path to .env (Project5/.env).
# P5: Assessment review — week5/Assessment.txt feedback session.

def run_classroom_demo() -> None:
    demo_pipeline_overview()
    try:
        demo_run_regression()
    except ImportError:
        print("Using Project5/main.py fallback...")
        subprocess.run([sys.executable, "main.py"], cwd=_PROJECT5, check=False)
    print("\nAssessment notes: week5/Assessment.txt")


if __name__ == "__main__":
    run_classroom_demo()