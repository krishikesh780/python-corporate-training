"""
Week 5 — Day 4: JSON CMS (project4)
=====================================

PYTHON CLASSROOM
----------------
1. CRUD with Customer + CustomerManager
2. Persistence: data/customers.json
3. Custom exceptions (not found, file errors)
4. Demo read-only + one safe update in lab copy
5. Practice P1–P5

PYTHON RECALL
-------------
- JSON CMS here; week4/day5 used Excel + OOP package (different persistence).
- save() after mutations — in-memory list syncs to file.
- Error handling: week3/day1; OOP: week4/day1–day2.
- SQL regression project: Project5 (day5).
"""

import json
import shutil
import sys
from pathlib import Path

_PROJECT4 = Path(__file__).resolve().parent / "project4"
_LAB = Path(__file__).resolve().parent / "_classroom_lab" / "day4"


def _import_project4():
    if str(_PROJECT4) not in sys.path:
        sys.path.insert(0, str(_PROJECT4))
    from insurance.customer import Customer
    from insurance.manager import CustomerManager

    return Customer, CustomerManager


def demo_customer_model() -> None:
    Customer, _ = _import_project4()
    c = Customer(1, "Alice", "POL12345", "Health", 1200)
    print(c)
    print("as dict:", c.to_dict())


def demo_json_storage_layout() -> None:
    data_file = _PROJECT4 / "data" / "customers.json"
    print("JSON path:", data_file)
    if data_file.exists():
        rows = json.loads(data_file.read_text(encoding="utf-8"))
        print("Records on disk:", len(rows))


def demo_manager_readonly() -> None:
    """Uses isolated lab JSON so classroom demo does not corrupt project data."""
    src = _PROJECT4 / "data" / "customers.json"
    _LAB.mkdir(parents=True, exist_ok=True)
    lab_json = _LAB / "customers.json"
    if src.exists():
        shutil.copy(src, lab_json)
    else:
        lab_json.write_text(
            json.dumps(
                [
                    {
                        "id": 1,
                        "name": "Alice",
                        "policy_number": "POL12345",
                        "policy_type": "Health",
                        "premium": 1200,
                        "status": "Alive",
                    }
                ],
                indent=2,
            ),
            encoding="utf-8",
        )

    if str(_PROJECT4) not in sys.path:
        sys.path.insert(0, str(_PROJECT4))
    import insurance.utils as utils

    utils.DATA_FILE = lab_json
    from insurance.manager import CustomerManager
    mgr = CustomerManager()
    print("Loaded:", len(mgr.customers))
    mgr.list_customers()


# PYTHON RECALL — Practice (P1–P5)
# P1: find_customer() for missing policy → CustomerNotFoundError.
# P2: Reject duplicate policy on add.
# P3: Valid status enum Alive / Deceased / Claimed.
# P4: run project4/main.py end-to-end once in lab folder.
# P5: diff JSON CMS vs week4 Excel compare use case.

def run_classroom_demo() -> None:
    demo_customer_model()
    demo_json_storage_layout()
    demo_manager_readonly()
    print("\nFull CRUD demo: cd project4 && python main.py")


if __name__ == "__main__":
    run_classroom_demo()