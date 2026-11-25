"""
Quick Revision — Day 5: Pandas
==============================
Series, DataFrame, filter, groupby, merge, read/write patterns (in-memory).
Full course: ../week3/day4–5, ../week3/training_data.py
"""

from pathlib import Path

import pandas as pd

_LAB = Path(__file__).resolve().parent / "_lab"


def _sample_df() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "Name": ["Amit", "Ravi", "Neha", "Pooja"],
            "Age": [25, 28, 22, 24],
            "City": ["Delhi", "Mumbai", "Pune", "Delhi"],
            "Salary": [50000, 60000, 45000, 52000],
        }
    )


def demo_inspect() -> None:
    df = _sample_df()
    print("shape:", df.shape)
    print(df.head(2))
    print(df.describe())


def demo_select_filter() -> None:
    df = _sample_df()
    print("Salary>50k:\n", df[df["Salary"] > 50000])
    print("iloc[0]:", df.iloc[0]["Name"])


def demo_missing_and_columns() -> None:
    df = _sample_df().copy()
    df.loc[1, "Age"] = None
    print("null count:", df["Age"].isnull().sum())
    df["Age"] = df["Age"].fillna(df["Age"].mean())
    df["Bonus"] = df["Salary"] * 0.1
    print(df[["Name", "Age", "Bonus"]])


def demo_groupby() -> None:
    df = _sample_df()
    print(df.groupby("City")["Salary"].agg(["mean", "max", "count"]))


def demo_merge() -> None:
    df = _sample_df()
    dept = pd.DataFrame({"Name": df["Name"], "Dept": ["IT", "HR", "IT", "Finance"]})
    print(pd.merge(df, dept, on="Name", how="inner").head())


def demo_read_write_lab() -> None:
    _LAB.mkdir(parents=True, exist_ok=True)
    df = _sample_df()
    csv_path = _LAB / "rev.csv"
    df.to_csv(csv_path, index=False)
    loaded = pd.read_csv(csv_path)
    print("round-trip rows:", len(loaded))


def run_revision() -> None:
    print("pandas", pd.__version__)
    demo_inspect()
    demo_select_filter()
    demo_missing_and_columns()
    demo_groupby()
    demo_merge()
    demo_read_write_lab()


if __name__ == "__main__":
    run_revision()