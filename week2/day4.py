"""
Week 2 — Day 4: Modules & Packages (Advanced)
=============================================

PYTHON CLASSROOM
----------------
1. Package = folder + modules (+ optional __init__.py)
2. Import paths: package.module.function
3. pip install / show / uninstall
4. venv — isolate dependencies (terminal steps)
5. __name__ == "__main__" guard
6. Practice P1–P5

PYTHON RECALL
-------------
- pip installs into active environment (system or venv).
- Always activate venv before pip install in projects.
- __name__ is "__main__" only when file run directly.
- Relative imports work inside packages, not from loose scripts.
- Built-in import patterns: week2/day3.py.
"""

from pathlib import Path


def demo_package_layout() -> None:
    """Explains finance/ package — create in lab if needed."""
    layout = """
    finance/
        __init__.py
        salary.py    → calculate_salary(basic, hra=0.2, da=0.1)
        tax.py       → calculate_tax(income, rate=0.1)

    # from finance.salary import calculate_salary
    # from finance.tax import calculate_tax
    """
    print("Package layout (reference):")
    print(layout.strip())


def demo_pip_requests() -> None:
    print("pip cheatsheet:")
    print("  pip install requests")
    print("  pip show requests")
    print("  pip uninstall requests")
    try:
        import requests

        response = requests.get("https://httpbin.org/get", timeout=5)
        print("requests OK, status:", response.status_code)
    except ImportError:
        print("requests not installed — skip live call in class or: pip install requests")
    except OSError as exc:
        print("Network skipped:", exc)


def demo_venv_steps() -> None:
    root = Path(__file__).resolve().parent
    print("venv steps (run in terminal, not in Python):")
    print(f"  cd {root}")
    print("  python -m venv myenv")
    print("  myenv\\Scripts\\activate        # Windows")
    print("  source myenv/bin/activate      # Linux / Mac")
    print("  pip install requests")
    print("  pip list")
    print("  deactivate")


def demo_main_guard() -> None:
    print("__name__ in this file:", __name__)
    if __name__ == "__main__":
        print("This block runs only when day4.py is executed directly.")


# P1: Sketch a package hr/ with leave.py and payroll.py imports.
# P2: Write module_demo.py with hello() + __main__ guard.
# P3: pip freeze > requirements.txt — what is it for?
# P4: Why use venv instead of system Python?
# P5: ImportError vs ModuleNotFoundError — when each appears?

def run_classroom_demo() -> None:
    demo_package_layout()
    demo_pip_requests()
    demo_venv_steps()
    demo_main_guard()


if __name__ == "__main__":
    run_classroom_demo()