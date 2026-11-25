# insurance CMS Project 

# 1. Business_Requirements:

# 📑 Insurance Customer Management System – Business Requirements

## 1. Customer Records
- Each customer must have a **unique** `policy_number`.  
- Details include:  
  - `id`  
  - `name`  
  - `policy_number`  
  - `policy_type`  
  - `premium`  
  - `status`  

---

## 2. CRUD Operations
- **Create** → Add a new customer.  
- **Read** → List all customers or search for a specific customer (by `policy_number`).  
- **Update** → Update `premium`, `policy_type`, and `status` (e.g., Alive → Deceased).  
- **Delete** → Remove a customer from the system.  

---

## 3. Business Rules
- `policy_number` will never change (it is the unique identifier).  
- `premium` and `policy_type` can be updated.  
- Valid `status` values:  
  - `Alive`  
  - `Deceased`  
  - `Claimed`  
- `name` can only be changed for legal reasons (marriage, correction, court order).  

---

## 4. File Handling (Persistence)
- Data will be stored in the `data/customers.json` file.  
- After every CRUD operation, changes must be saved to the file.  

---

## 5. Error Handling
- If `policy_number` is not found → **CustomerNotFoundError**.  
- If a duplicate `policy_number` is added → reject the entry.  
- If the file is missing/invalid → **FileReadError** / **FileWriteError**.  

---


# 2. Project directory


insurance_project/
│── main.py                 
│── data/
│   └── customers.json      
│── insurance/
│   ├── __init__.py
│   ├── customer.py         
│   ├── manager.py          
│   ├── utils.py            
│   └── exceptions.py       



# 3. Custer_Data:
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



# 4. Porgram_flow:
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


# 6. Future Scope
- Database integration (SQLite / PostgreSQL).  
- Multiple policies per customer.  
- Nominee and claim settlement handling.  
- Premium due date tracking.  
- CLI menu / Web interface.  