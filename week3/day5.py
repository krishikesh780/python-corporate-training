"""
Week 3 — Day 5: Pandas — Read / Write Files
===========================================

PYTHON CLASSROOM
----------------
1. to_csv / read_csv
2. to_excel / read_excel (needs openpyxl)
3. Update cells (e.g. IT salary +10%)
4. concat new rows → save final
5. to_json / filters → export subsets
6. Practice P1–P5

PYTHON RECALL
-------------
- index=False avoids unnamed index column in CSV/Excel.
- orient='records' for JSON list-of-objects.
- In-memory analysis (groupby, loc): week3/day4.py.
- Sample rows: training_data.py (not redefined here).
- Plain text / EDI: week3/day3.py.
- Output: _classroom_lab/day5/
"""

import sys
from pathlib import Path

import pandas as pd

_WEEK3 = Path(__file__).resolve().parent
if str(_WEEK3) not in sys.path:
    sys.path.insert(0, str(_WEEK3))

from training_data import EMPLOYEE_ROWS, make_employee_df  # noqa: E402

_OUT = _WEEK3 / "_classroom_lab" / "day5"


def _out_dir() -> Path:
    _OUT.mkdir(parents=True, exist_ok=True)
    return _OUT


def demo_csv_roundtrip() -> Path:
    out = _out_dir()
    path = out / "employees.csv"
    df = make_employee_df()
    df.to_csv(path, index=False)
    loaded = pd.read_csv(path)
    print("CSV round-trip:\n", loaded.head())
    return path


def demo_excel_update() -> pd.DataFrame:
    out = _out_dir()
    base = out / "employees.xlsx"
    updated = out / "employees_updated.xlsx"
    make_employee_df().to_excel(base, index=False)

    df_x = pd.read_excel(base)
    df_x["Salary"] = df_x["Salary"].astype(float)
    mask = df_x["Dept"] == "IT"
    df_x.loc[mask, "Salary"] = df_x.loc[mask, "Salary"] * 1.1
    df_x.to_excel(updated, index=False)
    print("\nAfter IT +10% (file workflow, not day4 in-memory hike):\n", df_x)
    return df_x


def demo_append_and_final(df_x: pd.DataFrame) -> Path:
    out = _out_dir()
    final_path = out / "employees_final.xlsx"
    new_row = pd.DataFrame(
        {"Name": ["Kiran"], "Dept": ["Finance"], "Salary": [55000], "Age": [30]}
    )
    combined = pd.concat([df_x, new_row], ignore_index=True)
    combined.to_excel(final_path, index=False)
    print("\nAppended:\n", combined)
    return final_path


def demo_json_export(final_path: Path) -> None:
    out = _out_dir()
    final_df = pd.read_excel(final_path)
    json_path = out / "employees.json"
    final_df.to_json(json_path, orient="records", indent=2)
    print("JSON written:", json_path)

    it_dept = final_df[final_df["Dept"] == "IT"]
    it_path = out / "employees_IT.xlsx"
    it_dept.to_excel(it_path, index=False)
    print("IT subset:", len(it_dept), "rows →", it_path)

    above30 = final_df[final_df["Age"] > 30]
    above30.to_excel(out / "employees_above30.xlsx", index=False)
    print("Mean salary:", final_df["Salary"].mean())


# PYTHON RECALL — Practice (P1–P5)
# P1: Read employees.csv with dtypes={"Salary": int}.
# P2: Export only Name, Salary to slim.csv.
# P3: Read JSON back with pd.read_json.
# P4: Multi-sheet Excel with ExcelWriter (one sheet per Dept).
# P5: One pipeline function: load → filter → save.

def run_classroom_demo() -> None:
    print("Schema:", list(EMPLOYEE_ROWS.keys()))
    demo_csv_roundtrip()
    df_updated = demo_excel_update()
    final = demo_append_and_final(df_updated)
    demo_json_export(final)


if __name__ == "__main__":
    run_classroom_demo()