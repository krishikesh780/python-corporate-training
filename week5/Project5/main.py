from pathlib import Path

import pandas as pd

from regression.query_loader import load_queries, replace_variables
from regression.validator import validate_count, validate_duplicate_key, validate_primary_key

_ROOT = Path(__file__).resolve().parent
DEFAULT_VARS = {"DATE": "2025-08-31", "STATUS": "Alive"}


def run_regression_report(
    variables: dict | None = None,
    queries_path: Path | None = None,
    report_path: Path | None = None,
) -> Path:
    variables = variables or DEFAULT_VARS
    queries_path = queries_path or _ROOT / "data" / "queries.xlsx"
    report_path = report_path or _ROOT / "data" / "report.xlsx"

    df = load_queries(queries_path)
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
        query = replace_variables(row["SQL_Query"], variables)
        results.append(handler(query))

    report_df = pd.DataFrame(results)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_df.to_excel(report_path, index=False)
    return report_path


def main() -> None:
    print("Loading queries...")
    out = run_regression_report()
    print("Report generated:", out)


if __name__ == "__main__":
    main()