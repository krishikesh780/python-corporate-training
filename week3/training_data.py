"""Shared sample data for Week 3 Days 4–5 (single source — no duplicate dicts)."""

import pandas as pd

EMPLOYEE_ROWS = {
    "Name": ["Ravi", "Anu", "Sita", "Vikram"],
    "Dept": ["IT", "HR", "Finance", "IT"],
    "Salary": [50000, 60000, 45000, 70000],
    "Age": [28, 32, 29, 35],
}


def make_employee_df() -> pd.DataFrame:
    return pd.DataFrame(EMPLOYEE_ROWS)