"""
Week 4 — Day 5: Capstone — Insurance OOP Package
=================================================

PYTHON CLASSROOM
----------------
1. Package layout: insurance/ (models, manager, utils)
2. Customer class + CRUD via CustomerManager
3. Custom exceptions
4. Excel load + compare (reuses pandas pattern from week3/day5)
5. Run project: day5/project3/main.py
6. Practice P1–P5

PYTHON RECALL
-------------
- Relative imports inside package: from .customer import Customer
- Business compare logic: utils.compare_customers (not week3 day5 script).
- OOP building blocks: week4/day1–day2.
- Git / CI for this repo: week4/day3–day4.
"""

import json
import sys
from pathlib import Path

_PROJECT3 = Path(__file__).resolve().parent / "day5" / "project3"
_DATA = _PROJECT3 / "data"


def demo_package_layout() -> None:
    print("Package root:", _PROJECT3)
    files = [
        "insurance/customer.py",
        "insurance/manager.py",
        "insurance/utils.py",
        "insurance/exceptions.py",
        "data/old_customers.xlsx",
        "data/new_customers.xlsx",
    ]
    for label in files:
        path = _PROJECT3.joinpath(*label.split("/"))
        print(f"  {'OK' if path.exists() else '—'} {label}")


def _import_project3():
    if str(_PROJECT3) not in sys.path:
        sys.path.insert(0, str(_PROJECT3))
    from insurance.customer import Customer
    from insurance.manager import CustomerManager
    from insurance.utils import compare_customers, load_customers

    return Customer, CustomerManager, compare_customers, load_customers


def demo_customer_oop() -> None:
    Customer, _, _, _ = _import_project3()
    c = Customer(1, "Alice", "POL12345", "Health", 1200)
    print(c)
    c.update_premium(1500)
    print("After update:", c.to_dict())


def demo_manager_crud() -> None:
    _, CustomerManager, _, _ = _import_project3()
    manager = CustomerManager()
    print("Loaded customers:", len(manager.customers))
    manager.list_customers()


def demo_excel_compare() -> None:
    _, _, compare_customers, load_customers = _import_project3()
    old_path = _DATA / "old_customers.xlsx"
    new_path = _DATA / "new_customers.xlsx"
    if not old_path.exists() or not new_path.exists():
        print("Excel samples missing under project3/data/")
        return
    old_df = load_customers(old_path)
    new_df = load_customers(new_path)
    report = compare_customers(old_df, new_df)
    print("Compare summary:")
    for key, rows in report.items():
        print(f"  {key}: {len(rows)}")
    print(json.dumps({k: v[:1] for k, v in report.items() if v}, indent=2, default=str))


# PYTHON RECALL — Practice (P1–P5)
# P1: add_customer() with duplicate policy guard.
# P2: Custom exception when Excel column missing.
# P3: Export compare report to report.json.
# P4: Wire CustomerManager.save() after update.
# P5: Push project3 to GitHub using day3–day4 steps.

def run_classroom_demo() -> None:
    demo_package_layout()
    demo_customer_oop()
    try:
        demo_manager_crud()
    except Exception as exc:
        print("Manager demo skipped:", exc)
    demo_excel_compare()
    print("\nFull pipeline: cd day5/project3 && python main.py")


if __name__ == "__main__":
    run_classroom_demo()