"""Insurance DB comparison — used by week2/day5.py classroom demo."""

import json

INSURANCE_DATA = {
    "old_database": {
        "customers": [
            {"id": 1, "name": "Alice", "policy_number": "POL12345", "policy_type": "Health", "premium": 1200},
            {"id": 2, "name": "Bob", "policy_number": "POL54321", "policy_type": "Life", "premium": 1500},
            {"id": 3, "name": "Charlie", "policy_number": "POL67890", "policy_type": "Health", "premium": 1800},
        ]
    },
    "new_database": {
        "customers": [
            {"id": 1, "name": "Alice", "policy_number": "POL12345", "policy_type": "Health", "premium": 1200},
            {"id": 2, "name": "Bob+Family", "policy_number": "POL54321", "policy_type": "Life+Vehicle", "premium": 2000},
            {"id": 4, "name": "David", "policy_number": "POL11111", "policy_type": "Health", "premium": 1300},
        ]
    },
}


def compare_customers(old: list, new: list) -> dict:
    old_dict = {c["policy_number"]: c for c in old}
    new_dict = {c["policy_number"]: c for c in new}

    report = {
        "unchanged": [],
        "changed": [],
        "name_updated": [],
        "new": [],
        "removed": [],
    }

    for pol_no, old_c in old_dict.items():
        if pol_no in new_dict:
            new_c = new_dict[pol_no]
            if old_c["name"] != new_c["name"]:
                report["name_updated"].append(
                    {
                        "policy_number": pol_no,
                        "old_name": old_c["name"],
                        "new_name": new_c["name"],
                    }
                )
            if (
                old_c["policy_type"] == new_c["policy_type"]
                and old_c["premium"] == new_c["premium"]
            ):
                report["unchanged"].append(new_c)
            else:
                report["changed"].append(
                    {
                        "policy_number": pol_no,
                        "name": new_c["name"],
                        "old": {"policy_type": old_c["policy_type"], "premium": old_c["premium"]},
                        "new": {"policy_type": new_c["policy_type"], "premium": new_c["premium"]},
                    }
                )
        else:
            report["removed"].append(old_c)

    for pol_no, new_c in new_dict.items():
        if pol_no not in old_dict:
            report["new"].append(new_c)

    return report


def run_comparison(data: dict | None = None) -> dict:
    data = data or INSURANCE_DATA
    old = data["old_database"]["customers"]
    new = data["new_database"]["customers"]
    return compare_customers(old, new)


if __name__ == "__main__":
    print(json.dumps(run_comparison(), indent=2))