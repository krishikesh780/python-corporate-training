"""
Week 5 — Day 3: Regression Validators & Exceptions
====================================================

PYTHON CLASSROOM
----------------
1. Map Validation_Type → Python function
2. validate_primary_key / duplicate / count
3. Custom errors: DatabaseError, QueryError
4. Build results list for reporting
5. Practice P1–P5

PYTHON RECALL
-------------
- Regression = re-run checks after data/code changes.
- Each validator returns a dict for pandas report row.
- Query load + replace: week5/day2.py.
- Full report Excel: week5/day5.py.
- Week3 error handling patterns still apply.
"""

import sys
from pathlib import Path

_PROJECT5 = Path(__file__).resolve().parent / "Project5"
VARS = {"DATE": "2025-08-31", "STATUS": "Alive"}


def _bootstrap() -> None:
    if str(_PROJECT5) not in sys.path:
        sys.path.insert(0, str(_PROJECT5))


def demo_validators() -> None:
    _bootstrap()
    from regression.query_loader import load_queries, replace_variables
    from regression.validator import (
        validate_count,
        validate_duplicate_key,
        validate_primary_key,
    )

    df = load_queries(_PROJECT5 / "data" / "queries.xlsx")
    results = []
    dispatch = {
        "Primary_Key": validate_primary_key,
        "Duplicate_Key": validate_duplicate_key,
        "Count_Check": validate_count,
    }

    for _, row in df.iterrows():
        vtype = row["Validation_Type"]
        handler = dispatch.get(vtype)
        if not handler:
            continue
        sql = replace_variables(row["SQL_Query"], VARS)
        results.append(handler(sql))

    for item in results:
        print(item)


def demo_exceptions_note() -> None:
    _bootstrap()
    from regression.exceptions import DatabaseError, QueryError

    print("QueryError → bad Excel path")
    print("DatabaseError → SQL / connection failure")
    try:
        raise DatabaseError("demo only")
    except DatabaseError as exc:
        print("Caught:", exc)


# PYTHON RECALL — Practice (P1–P5)
# P1: Assert duplicate check finds POL54321 twice.
# P2: Add Premium_Check validator stub in validator.py.
# P3: Fail fast if Validation_Type unknown.
# P4: Wrap run_query in try/except → log message.
# P5: Compare validator output schema for report.xlsx columns.

def run_classroom_demo() -> None:
    demo_exceptions_note()
    demo_validators()


if __name__ == "__main__":
    run_classroom_demo()