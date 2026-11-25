# Curriculum — all days & projects

Each **day file** layout:

- Docstring: **PYTHON CLASSROOM** (order) + **PYTHON RECALL** (hooks)  
- Demo functions + `run_classroom_demo()`  
- **P1–P5** practice comments  

Command pattern (from repo root, venv active):

```bat
python weekN\dayM.py
```

---

## Week 1 — Python foundations

| Day | File | Topics |
|-----|------|--------|
| 1 | `week1/day1.py` | print, types, casting, input, operators, even/odd |
| 2 | `week1/day2.py` | if/for/while, break/continue, order mini-project |
| 3 | `week1/day3.py` | strings, slicing, methods, formatting |
| 4 | `week1/day4.py` | list, tuple, set, dict, comprehensions |
| 5 | `week1/day5.py` | `enumerate`, list methods, nested dict |
| Bonus | `week1/day6/project1/calculator.py` | small calculator project |

---

## Week 2 — Functions & modules

| Day | File | Topics |
|-----|------|--------|
| 1 | `week2/day1.py` | functions, `*args`, `**kwargs`, higher-order |
| 2 | `week2/day2.py` | lambda, map, filter, reduce, zip |
| 3 | `week2/day3.py` | imports, `mymodule.py` |
| 4 | `week2/day4.py` | packages, pip, venv, `__main__` |
| 5 | `week2/day5.py` | JSON compare capstone |
| Project | `week2/day5/project2/insurance.py` | compare_customers |

---

## Week 3 — Files, errors, pandas

| Day | File | Topics |
|-----|------|--------|
| 1 | `week3/day1.py` | try/except, finally, raise, assert, logging |
| 2 | `week3/day2.py` | paths, `os.path`, organize by extension |
| 3 | `week3/day3.py` | text I/O, UTF-8, EDI intro |
| 4 | `week3/day4.py` | pandas in-memory (`training_data.py`) |
| 5 | `week3/day5.py` | CSV / Excel / JSON export |

Shared data: `week3/training_data.py`

---

## Week 4 — OOP & Git

| Day | File | Topics |
|-----|------|--------|
| 1 | `week4/day1.py` | class, inherit, polymorphism |
| 2 | `week4/day2.py` | encapsulation, ABC, MI, class/static |
| 3 | `week4/day3.py` | CLI & git basics (cheatsheet) |
| 4 | `week4/day4.py` | gitignore, secrets, GitHub CI intro |
| 5 | `week4/day5.py` | OOP Excel insurance |
| Project | `week4/day5/project3/` | `main.py`, `insurance/` package, `docs.md` |

---

## Week 5 — DB, CMS, regression

| Day | File | Topics |
|-----|------|--------|
| 1 | `week5/day1.py` | SQLite basics, `setup_db.py` |
| 2 | `week5/day2.py` | SQL from Excel, placeholders |
| 3 | `week5/day3.py` | regression validators |
| 4 | `week5/day4.py` | JSON CMS (`project4`) |
| 5 | `week5/day5.py` | SQL regression report |
| Project A | `week5/project4/` | CustomerManager + `customers.json` |
| Project B | `week5/Project5/` | `queries.xlsx` → `sample.db` → `report.xlsx` |

Assessment: `week5/Assessment.txt`

---

## Quick revision (parallel track)

`quick_revision/day1_core_python.py` → … → `day6_fastapi.py`  
See [quick_revision/README.md](../quick_revision/README.md)

---

## Week 6 — AI & cloud career track (optional)

**Not classroom days** — hands-on portfolio for AI / GCP / automation interviews.

| Track | Path |
|-------|------|
| Hub | `week6/README.txt` |
| Interview Q | `week6/INTERVIEW.txt` |
| 1 GenAI RAG | `week6/project1_gemini_rag/` |
| 2 Chat API | `week6/project2_fastapi_chat/` |
| 3 BigQuery | `week6/project3_bigquery_etl/` |
| 4 n8n | `week6/project4_n8n_ai_workflow/` |
| 5 Core drill | `week6/project5_interview_core/` |
| 6 Schedule / CI | `week6/project6_schedule_triggers/` + `.github/workflows/scheduled-automation.yml` |

---

## Generated folders (ignore / delete anytime)

- `week*/_classroom_lab/` — demo outputs  
- `quick_revision/_lab/`  