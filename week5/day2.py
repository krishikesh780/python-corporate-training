"""
Week 5 — Day 2: SQL Templates & Excel Query Loader
====================================================

PYTHON CLASSROOM
----------------
1. Store SQL in Excel (Validation_Type, SQL_Query)
2. load_queries() with pandas
3. replace_variables({DATE}, {STATUS})
4. Execute loaded query on sample.db
5. Practice P1–P5

PYTHON RECALL
-------------
- Never trust raw string SQL from users — parameterize where possible.
- Placeholder style here: {DATE} text replace for training sheets.
- SQLite connect: week5/day1.py.
- Validators map query → business rule: week5/day3.py.
"""

import sqlite3
import sys
from pathlib import Path

_PROJECT5 = Path(__file__).resolve().parent / "Project5"


def _ensure_project5_path() -> None:
    if str(_PROJECT5) not in sys.path:
        sys.path.insert(0, str(_PROJECT5))


def demo_replace_variables() -> None:
    _ensure_project5_path()
    from regression.query_loader import replace_variables

    sql = "SELECT * FROM customers WHERE date = '{DATE}' AND status = '{STATUS}'"
    out = replace_variables(sql, {"DATE": "2025-08-31", "STATUS": "Alive"})
    print("Replaced SQL:\n ", out)


def demo_load_excel_queries() -> None:
    _ensure_project5_path()
    from regression.query_loader import load_queries

    path = _PROJECT5 / "data" / "queries.xlsx"
    df = load_queries(path)
    print("Query rows:", len(df))
    print(df[["Validation_Type"]].head())


def demo_run_one_query() -> None:
    _ensure_project5_path()
    from regression.db_utils import run_query
    from regression.query_loader import load_queries, replace_variables

    df = load_queries(_PROJECT5 / "data" / "queries.xlsx")
    row = df.iloc[0]
    query = replace_variables(row["SQL_Query"], {"DATE": "2025-08-31", "STATUS": "Alive"})
    print("Type:", row["Validation_Type"])
    print("Result:", run_query(query))


# PYTHON RECALL — Practice (P1–P5)
# P1: Add {MIN_PREMIUM} placeholder to a premium filter query.
# P2: Load sheet_name if queries.xlsx has multiple tabs.
# P3: Validate required columns exist before iterating rows.
# P4: Log final SQL before execute (debug practice).
# P5: Handle missing placeholder with clear QueryError.

def run_classroom_demo() -> None:
    demo_replace_variables()
    demo_load_excel_queries()
    demo_run_one_query()


if __name__ == "__main__":
    run_classroom_demo()