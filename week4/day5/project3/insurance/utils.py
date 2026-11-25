import os
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv
from .exceptions import FileReadError, FileWriteError

_PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(_PROJECT_ROOT / ".env")

OLD_DATA = os.getenv("OLD_CUSTOMERS", "data/old_customers.xlsx")
NEW_DATA = os.getenv("NEW_CUSTOMERS", "data/new_customers.xlsx")


def _resolve_data_path(file_path: str | Path) -> Path:
    path = Path(file_path)
    if not path.is_absolute():
        path = _PROJECT_ROOT / path
    return path


def load_customers(file_path):
    """Load customers from Excel file"""
    path = _resolve_data_path(file_path)
    try:
        return pd.read_excel(path)
    except Exception as e:
        raise FileReadError(f"❌ Error reading {path}: {e}")

def compare_customers(old_df, new_df):
    """Compare old vs new customer data"""
    report = {
        "unchanged": [],
        "changed": [],
        "name_updated": [],
        "new": [],
        "removed": []
    }

    # Index by policy_number
    old_dict = old_df.set_index("policy_number").to_dict("index")
    new_dict = new_df.set_index("policy_number").to_dict("index")

    for pol, old in old_dict.items():
        if pol in new_dict:
            new = new_dict[pol]

            if old["name"] != new["name"]:
                report["name_updated"].append({
                    "policy_number": pol,
                    "old_name": old["name"],
                    "new_name": new["name"]
                })

            if old["policy_type"] == new["policy_type"] and old["premium"] == new["premium"] and old["status"] == new["status"]:
                report["unchanged"].append(new)
            else:
                report["changed"].append({
                    "policy_number": pol,
                    "name": new["name"],
                    "old": {k: old[k] for k in ["policy_type", "premium", "status"]},
                    "new": {k: new[k] for k in ["policy_type", "premium", "status"]}
                })
        else:
            report["removed"].append(old)

    for pol, new in new_dict.items():
        if pol not in old_dict:
            report["new"].append(new)

    return report


def read_customers(file_path: str | None = None) -> list[dict]:
    """Load customer records as list of dicts (for CustomerManager)."""
    path = file_path or OLD_DATA
    df = load_customers(path)
    return df.to_dict(orient="records")


def write_customers(records: list[dict], file_path: str | None = None) -> None:
    path = _resolve_data_path(file_path or NEW_DATA)
    try:
        pd.DataFrame(records).to_excel(path, index=False)
    except Exception as e:
        raise FileWriteError(f"Error writing {path}: {e}") from e
