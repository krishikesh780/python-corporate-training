import json
from insurance.utils import load_customers, compare_customers, OLD_DATA, NEW_DATA

def main():
    print("📊 Loading data...")
    old_df = load_customers(OLD_DATA)
    new_df = load_customers(NEW_DATA)

    print("🔎 Comparing records...")
    report = compare_customers(old_df, new_df)

    print("\n✅ Comparison Report:")
    print(json.dumps(report, indent=4, default=str))

if __name__ == "__main__":
    main()
