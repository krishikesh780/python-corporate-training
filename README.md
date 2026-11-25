# Python Corporate Training

**5-week** Python curriculum + optional **Week 6** AI/cloud project track for interviews.  
Code-first: open a day file → read **CLASSROOM / RECALL** → run demos → do **P1–P5**.

---

## Start here (reading path)

1. **[docs/HOW_TO_STUDY.md](docs/HOW_TO_STUDY.md)** — how to read & practise daily  
2. **[docs/CURRICULUM.md](docs/CURRICULUM.md)** — every day file & project  
3. **Setup** below — then `python week1/day1.py`  

Optional: `python main.py` prints week folders at a glance.

---

## Repo layout

```
python_corporate_training/
├── week1 … week5/     # day1.py … day5.py (+ projects)
├── quick_revision/      # interview cram (6 files)
├── exercises/           # extra .txt question banks
├── docs/                # HOW_TO_STUDY, CURRICULUM
├── scripts/setup.bat    # venv + pip install
├── requirements.txt
├── main.py              # curriculum launcher
└── archive/             # old backups (not for class)
```

---

## Day file pattern

Every `dayN.py` includes:

| Section | Purpose |
|---------|---------|
| **PYTHON CLASSROOM** | Teaching order for that session |
| **PYTHON RECALL** | Short memory hooks |
| Demo functions | Runnable examples |
| **P1–P5** | Practice (bottom of file) |
| `run_classroom_demo()` | Runs when you `python dayN.py` |

Outputs from path/file demos go under `week*/_classroom_lab/` (safe to delete).

---

## Weeks at a glance

| Week | Focus | Capstone |
|------|--------|----------|
| **1** | Basics, control flow, strings, collections | `week1/day6/project1` (calculator) |
| **2** | Functions, modules, packages | `week2/day5/project2` (insurance JSON) |
| **3** | Errors, paths, I/O, pandas | Excel/CSV via `week3/day5.py` |
| **4** | OOP, Git, CI intro | `week4/day5/project3` (Excel CMS) |
| **5** | SQLite, regression, JSON CMS | `project4` + `Project5` |

Week guides: `week1/README.md` … `week5/README.md`

---

## Setup (one time)

**Windows:**

```bat
cd python_corporate_training
scripts\setup.bat
```

**Activate each new terminal:**

```bat
.venv\Scripts\activate
```

**Manual:**

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows
pip install -r requirements.txt
```

Dependencies: `pandas`, `openpyxl`, `python-dotenv`, `requests`  
Optional (FastAPI revision): see commented lines in `requirements.txt`

---

## Run examples

```bat
python week1\day1.py
python week3\day4.py
python week5\day5.py

cd week5\Project5 && python main.py
cd week5\project4 && python main.py
cd week4\day5\project3 && python main.py
```

---

## Extras

| Path | Purpose |
|------|---------|
| [quick_revision/](quick_revision/README.md) | Runnable revision scripts |
| [interview_prep/](interview_prep/README.txt) | **Short interview crib sheets** (plain `.txt`) |
| [exercises/](exercises/README.md) | Extra question banks |
| [docs/](docs/README.md) | Study guide & full curriculum |
| [archive/](archive/README.md) | Archived material only |

---

## Week 6 — AI jobs (hands-on, optional)

Priority: **Gemini/RAG** → **FastAPI chat** → **BigQuery** → **n8n** → **Docker/Git/SQL**

Start: `week6/README.txt` · Interview: `week6/INTERVIEW.txt`

---

## Week 5 assessment

After Week 5: review topics using [CURRICULUM.md](docs/CURRICULUM.md), complete **P1–P5** across weeks, run both Week 5 projects, then use [week5/Assessment.txt](week5/Assessment.txt) for feedback session.