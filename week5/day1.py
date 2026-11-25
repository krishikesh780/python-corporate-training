"""
Week 5 — Day 1: SQLite Fundamentals
=====================================

PYTHON CLASSROOM
----------------
1. sqlite3.connect — file DB
2. CREATE TABLE / INSERT / SELECT
3. fetchall() and row structure
4. Project DB: Project5/data/sample.db (setup_db.py)
5. Practice P1–P5

PYTHON RECALL
-------------
- SQLite = serverless file database; good for training & tests.
- Always conn.commit() after writes; conn.close() or use context manager.
- ? placeholders for values (avoid f-string SQL injection).
- Excel/SQL regression: week5/day2–day3; capstone: day5.
- OOP CMS (JSON): week5/day4 (not week4 Excel project).
"""

import sqlite3
import sys
from pathlib import Path

_PROJECT5 = Path(__file__).resolve().parent / "Project5"
_LAB_DB = Path(__file__).resolve().parent / "_classroom_lab" / "day1" / "demo.db"


def demo_in_memory_db() -> None:
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    cur.execute("CREATE TABLE items (id INTEGER PRIMARY KEY, name TEXT)")
    cur.executemany("INSERT INTO items VALUES (?, ?)", [(1, "pen"), (2, "book")])
    conn.commit()
    rows = cur.execute("SELECT * FROM items").fetchall()
    print("In-memory rows:", rows)
    conn.close()


def demo_file_db_lab() -> None:
    _LAB_DB.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(_LAB_DB)
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS employees")
    cur.execute(
        "CREATE TABLE employees (id INTEGER PRIMARY KEY, name TEXT, dept TEXT)"
    )
    cur.executemany(
        "INSERT INTO employees VALUES (?, ?, ?)",
        [(1, "Ravi", "IT"), (2, "Anu", "HR")],
    )
    conn.commit()
    for row in cur.execute("SELECT id, name, dept FROM employees WHERE dept = ?", ("IT",)):
        print("IT row:", row)
    conn.close()
    print("Lab DB:", _LAB_DB)


def demo_project5_setup() -> None:
    if str(_PROJECT5) not in sys.path:
        sys.path.insert(0, str(_PROJECT5))
    from setup_db import setup_database

    setup_database()
    db = _PROJECT5 / "data" / "sample.db"
    conn = sqlite3.connect(db)
    count = conn.execute("SELECT COUNT(*) FROM customers").fetchone()[0]
    conn.close()
    print("Project5 customers count:", count)


# PYTHON RECALL — Practice (P1–P5)
# P1: SELECT premium WHERE status = 'Alive'.
# P2: COUNT DISTINCT policy_number.
# P3: Use with sqlite3.connect(...) as conn.
# P4: Explain duplicate row in setup_db sample data.
# P5: Add index on policy_number (why?).

def run_classroom_demo() -> None:
    demo_in_memory_db()
    demo_file_db_lab()
    demo_project5_setup()


if __name__ == "__main__":
    run_classroom_demo()