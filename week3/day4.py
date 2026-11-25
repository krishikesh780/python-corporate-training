"""
Week 3 — Day 4: Pandas — Analysis (In-Memory)
=============================================

PYTHON CLASSROOM
----------------
1. Series & DataFrame
2. shape, head, describe
3. iloc / loc, boolean filter
4. Add / update columns
5. sort_values, rank
6. groupby & agg
7. Missing data: fillna, dropna
8. merge & concat
9. Practice P1–P5

PYTHON RECALL
-------------
- iloc = integer position; loc = label-based.
- df[df["Salary"] > 50000] — boolean masking.
- groupby(...).agg(...) for summaries.
- Sample data: training_data.py (shared with day5).
- Export to CSV/Excel: week3/day5.py only.
- Raw file I/O: week3/day3.py.
- Errors on bad input: week3/day1.py.
"""

import pandas as pd

from training_data import make_employee_df


def demo_series_and_frame() -> None:
    s = pd.Series([10, 20, 30], index=["a", "b", "c"])
    print("Series:\n", s)
    df = make_employee_df()
    print("\nDataFrame:\n", df)
    print("Shape:", df.shape)
    print("Describe:\n", df.describe())


def demo_selection() -> None:
    df = make_employee_df()
    print("Column Name:\n", df["Name"])
    print("\niloc row 0:\n", df.iloc[0])
    print("\nloc row 0 Name+Salary:\n", df.loc[0, ["Name", "Salary"]])
    print("\nSalary > 50k:\n", df[df["Salary"] > 50000])


def demo_columns_sort() -> None:
    df = make_employee_df().copy()
    df["Bonus"] = df["Salary"] * 0.1
    print("With bonus:\n", df)
    df.loc[df["Dept"] == "IT", "Salary"] += 5000
    print("\nIT hike (+5000 in-memory demo):\n", df)
    print("\nSort by Salary:\n", df.sort_values("Salary", ascending=False))


def demo_groupby() -> None:
    df = make_employee_df()
    print("Mean salary by Dept:\n", df.groupby("Dept")["Salary"].mean())
    print(
        "\nMulti-agg:\n",
        df.groupby("Dept").agg({"Salary": ["mean", "max"], "Age": "median"}),
    )


def demo_missing_data() -> None:
    df = pd.DataFrame({"Name": ["Ravi", "Anu", "Sita"], "Salary": [50000, None, 45000]})
    print("With NA:\n", df)
    print("\nfillna(0):\n", df.fillna(0))
    print("\ndropna:\n", df.dropna())


def demo_merge_concat() -> None:
    df = make_employee_df()
    left = pd.DataFrame({"ID": [1, 2], "Name": ["Ravi", "Anu"]})
    right = pd.DataFrame({"ID": [1, 2], "Salary": [50000, 60000]})
    print("Merge:\n", pd.merge(left, right, on="ID"))
    extra = pd.DataFrame({"Name": ["Kiran"], "Salary": [55000]})
    print("\nConcat sample:\n", pd.concat([df.head(2), extra], ignore_index=True))


def demo_insights() -> None:
    df = make_employee_df()
    top = df.loc[df["Salary"].idxmax()]
    print("Highest paid:\n", top)
    senior = df[(df["Age"] > 30) & (df["Salary"] > 50000)]
    print("\nSenior filter:\n", senior)


# PYTHON RECALL — Practice (P1–P5)
# P1: New column Experience_Level from Age buckets.
# P2: Dept-wise count with groupby().size().
# P3: Rank salaries within each Dept.
# P4: Replace HR dept rows with copy + modified Salary.
# P5: merge employee df with a Dept→Manager lookup table.

def run_classroom_demo() -> None:
    print("Pandas:", pd.__version__)
    demo_series_and_frame()
    demo_selection()
    demo_columns_sort()
    demo_groupby()
    demo_missing_data()
    demo_merge_concat()
    demo_insights()


if __name__ == "__main__":
    run_classroom_demo()