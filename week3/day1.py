"""
Week 3 — Day 1: Error Handling & Logging
========================================

PYTHON CLASSROOM
----------------
1. Why handle errors?
2. try / except (single type)
3. Multiple except blocks
4. finally — cleanup always runs
5. raise — business rule violations
6. assert — dev-time checks
7. logging levels + file handler (corporate pattern)
8. Practice P1–P5

PYTHON RECALL
-------------
- Catch specific exceptions first, then Exception as fallback.
- except catches only in the try block — not the whole function body.
- finally runs even if return/break in try/except.
- assert is off with python -O — don't use for production validation only.
- Logs: week3/day1 → _classroom_lab/day1/training.log
- Week map: D1 errors → D2 paths → D3 text I/O → D4 pandas → D5 export.
- Real file paths / read-write: day2–day3 (not repeated here).
"""

import logging
from pathlib import Path

_LOG_DIR = Path(__file__).resolve().parent / "_classroom_lab" / "day1"


def setup_logging() -> Path:
    _LOG_DIR.mkdir(parents=True, exist_ok=True)
    log_file = _LOG_DIR / "training.log"
    logging.basicConfig(
        filename=log_file,
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)s - %(message)s",
        force=True,
    )
    return log_file


def demo_why_handling() -> None:
    print("Without handling: int('100a') would crash the script.")
    print("With handling: catch, log, continue.")


def demo_try_except() -> None:
    try:
        int("100a")
    except ValueError as exc:
        print("ValueError caught:", exc)
        logging.error("ValueError in demo_try_except: %s", exc)


def demo_try_else() -> None:
    try:
        value = int("42")
    except ValueError:
        print("This branch should not run.")
    else:
        print("else: no exception — parsed value:", value)


def demo_multiple_except() -> None:
    try:
        _ = 10 / 0
    except ZeroDivisionError:
        print("ZeroDivisionError: cannot divide by zero.")
    except ArithmeticError as exc:
        print("Other arithmetic error:", exc)


def demo_finally() -> None:
    """File missing on purpose — shows FileNotFoundError; full I/O is day3."""
    try:
        open(_LOG_DIR / "does_not_exist.txt", "r", encoding="utf-8")
    except FileNotFoundError:
        print("FileNotFoundError handled (see day3 for safe read patterns).")
    finally:
        print("finally: cleanup / release runs regardless.")


def withdraw(amount: float, limit: float = 1000) -> None:
    if amount > limit:
        raise ValueError(f"Withdraw limit exceeded (max {limit}).")
    print(f"Withdraw {amount} successful.")


def demo_raise() -> None:
    try:
        withdraw(1500)
    except ValueError as exc:
        print("Raised:", exc)
        logging.warning("Withdraw rejected: %s", exc)
    withdraw(500)


def check_age(age: int) -> None:
    assert age >= 18, "Age must be 18 or older"
    print(f"Age {age} verified.")


def demo_assert() -> None:
    check_age(25)
    try:
        check_age(15)
    except AssertionError as exc:
        print("Assertion failed:", exc)
        logging.error("Assertion in check_age: %s", exc)


def process_employee(emp_id: int, name: str, age: int | str) -> None:
    try:
        assert isinstance(age, int), "Age must be integer"
        if age < 18:
            raise ValueError("Employee underage")
        logging.info("Processed employee %s id=%s age=%s", name, emp_id, age)
        print(f"OK: {name}")
    except (AssertionError, ValueError, TypeError) as exc:
        logging.error("Failed %s: %s", name, exc)
        print(f"FAIL: {name} — {exc}")


def demo_logging_corporate() -> None:
    process_employee(101, "Rahul", 25)
    process_employee(102, "Anita", 16)
    process_employee(103, "Vikas", "abc")


# PYTHON RECALL — Practice (P1–P5)
# P1: try/except around int(input()) for age.
# P2: Custom exception class InsufficientFundsError + raise.
# P3: try/except/else — see demo_try_else().
# P4: Log to console AND file (StreamHandler + FileHandler).
# P5: Wrap a day3 file read in try/except/finally.

def run_classroom_demo() -> None:
    log_path = setup_logging()
    demo_why_handling()
    demo_try_except()
    demo_try_else()
    demo_multiple_except()
    demo_finally()
    demo_raise()
    demo_assert()
    demo_logging_corporate()
    print("\nLog file:", log_path)


if __name__ == "__main__":
    run_classroom_demo()