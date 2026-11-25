
# 1.# Regression Testing Automation – Business Requirements

## Project Name
**Insurance Policy Master – Excel & SQL Based Regression Validation**

## Domain
Insurance (can extend to Banking / KYC / Finance).

## Primary Key
`policy_number`

## Input Files
- `old_master.xlsx` → Old policy master snapshot  
- `new_master.xlsx` → New policy master snapshot  
- `queries.xlsx` → SQL queries for validation (with placeholders)

## Business Validations
1. **Primary Key Validation**  
   - Check unique policy numbers (no missing or duplicates).
2. **Duplicate Key Validation**  
   - Identify policies with duplicate `policy_number`.
3. **Count Validation**  
   - Compare counts for specific conditions (e.g. status, premium).
4. **Field Change Detection**  
   - Detect differences in customer attributes across snapshots.

## Process Flow
1. Read queries from Excel.  
2. Replace placeholders `{DATE}`, `{STATUS}`, `{NAME}` with runtime values.  
3. Execute queries on `sample.db`.  
4. Store results in `report.xlsx` (Added / Removed / Changed).  

## Future Enhancements
- Integration with PostgreSQL / MySQL.  
- CI/CD pipeline with GitHub Actions.  
- Configurable tolerances for numeric fields.  
- Export reports in HTML/CSV dashboards.  

# 2.
regression_test_project/
│── main.py                 
│── setup_db.py              # Create & populate SQLite database
│── .env
│── .gitignore
│── requirements.txt
│── data/
│   ├── queries.xlsx         # SQL queries with placeholders
│   ├── sample.db            # SQLite DB (auto-generated via setup_db.py)
│   └── report.xlsx          # Validation report (output)
│── regression/
│   ├── __init__.py
│   ├── db_utils.py          # DB connection & query execution
│   ├── query_loader.py      # Read Excel queries & replace variables
│   ├── validator.py         # Business validation logic
│   └── exceptions.py        # Custom errors
│── docs/
│   └── Business_Requirements.md


# 3. 
Excel Queries (queries.xlsx)
        │
        ▼
Load Queries in Python → Replace Variables (DATE, STATUS)
        │
        ▼
Execute SQL Queries on sample.db
        │
        ▼
Validation Results (Primary, Duplicate, Count)
        │
        ▼
Save Report to report.xlsx

# 4 Quey Explaination:
🔎 Explanation

Primary_Key

Checks how many distinct policy_number exist for a given {DATE}.
Example result: 3

Duplicate_Key

Finds if any policy_number has duplicate entries.
Example result: POL54321 appears 2 times.

Count_Check

Count of all policies with a given {STATUS} (e.g., Alive, Deceased).

Premium_Check

Finds policies where premium is greater than a dynamic variable {MIN_PREMIUM}.
Example: {MIN_PREMIUM}=1000 → All policies above 1000 premium.

Alive_List

Returns list of customers alive on {DATE}.