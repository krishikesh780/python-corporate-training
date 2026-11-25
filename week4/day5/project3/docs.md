# Insurance CMS Project 

---

# 1. Business Requirements

## Project Name
**Insurance Policy Master – Excel Data Compare**

**Domain:** Insurance (can adapt for Banking/KYC as well)  
**Primary Key:** `Policy_No`  

**Files:**  
- `old_master.xlsx` – Previous policy master snapshot  
- `new_master.xlsx` – Latest policy master snapshot  
- `Insurance_ExcelDiff_Sample.xlsx` – Diff report with three sheets: **Added, Removed, Changed**

### Business Rules
- **Added:** Policies present in *new* but not in *old*.  
- **Removed:** Policies present in *old* but not in *new*.  
- **Changed:** Cell-level differences across fields:  
  - `Customer_Name`, `Product`, `Sum_Insured`, `Annual_Premium`, `Policy_Status`, `Email`, `Phone`, `Address`  
- Numeric fields (`Sum_Insured`, `Annual_Premium`) compared exactly (tolerance can be added if required).

### How to Use
1. Replace sample masters with your real exports (keep the same headers).  
2. Run the compare tool with key = `Policy_No`.  
3. Review the `Changed` sheet – **Old** values highlighted in red, **New** values in green.  
4. Optional: Add thresholds/tolerances for premium changes and ignore-case for addresses.

### Extension Ideas
- Add `Effective_Date` and show change history per policy.  
- Export summary KPIs: total added/removed/changed, sum of premium delta.  
- Banking variant: compare *Customer Master* or *Transactions* on `Account_No` and show amount/date changes.  

*Generated on: 2025-08-25*

---

# 2. Project Directory

insurance_project/
│── main.py
│── data/
│ └── customers.json
│── insurance/
│ ├── init.py
│ ├── customer.py
│ ├── manager.py
│ ├── utils.py
│ └── exceptions.py



---

# 3. Customer Data (Sample JSON)

```json
[
    {
        "id": 1,
        "name": "Alice",
        "policy_number": "POL12345",
        "policy_type": "Health",
        "premium": 1200,
        "status": "Alive"
    },
    {
        "id": 2,
        "name": "Bob",
        "policy_number": "POL54321",
        "policy_type": "Life",
        "premium": 1500,
        "status": "Alive"
    }
]

# Program Flow

         ┌───────────────┐
         │   Main Menu   │
         └───────┬───────┘
                 │
     ┌───────────┼───────────┐
     ▼           ▼           ▼
  Add Customer  View/Search  Update Customer
     │           │           │
     ▼           ▼           ▼
 Save File   Show Records   Save Changes
     │           │           │
     ▼           ▼           ▼
   ┌───────────────────────────┐
   │      Delete Customer      │
   └─────────────┬─────────────┘
                 ▼
             Save File

# 5. Future Scope

Database integration (SQLite / PostgreSQL).

Multiple policies per customer.

Nominee and claim settlement handling.

Premium due date tracking.

CLI menu / Web interface.

