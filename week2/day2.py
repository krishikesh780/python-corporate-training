"""
Week 2 — Day 2: Functions (Advanced)
====================================

PYTHON CLASSROOM
----------------
1. lambda — one-line anonymous functions
2. map — transform each item
3. filter — keep items that match a condition
4. reduce — fold iterable to one value
5. zip — pair-wise combine iterables
6. Payroll mini-project (map + filter + reduce)
7. Practice P1–P5

PYTHON RECALL
-------------
- map: every element transformed; filter: subset only.
- filter(func, seq) needs func(x) → True/False (not map with %).
- reduce needs: from functools import reduce.
- list(map(...)) consumes iterator — map alone is lazy.
- Function basics: week2/day1.py.
"""

from functools import reduce


def demo_lambda() -> None:
    square = lambda n: n * n
    print("Square of 7:", square(7))
    parity = lambda x: "Even" if x % 2 == 0 else "Odd"
    print("Parity of 11:", parity(11))


def demo_map() -> None:
    numbers = [1, 2, 3, 4, 5]
    squared = list(map(lambda x: x**2, numbers))
    print("Squares:", squared)

    words = ["hello", "python", "map"]
    print("Upper:", list(map(str.upper, words)))

    print("Add 10:", list(map(lambda x: x + 10, numbers)))


def demo_filter() -> None:
    numbers = [12, 5, 30, 7, 18]
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    print("Evens:", evens)
    gt_10 = list(filter(lambda x: x > 10, numbers))
    print("Greater than 10:", gt_10)


def demo_reduce() -> None:
    numbers = [1, 2, 3, 4]
    print("Sum:", reduce(lambda x, y: x + y, numbers))
    print("Product:", reduce(lambda x, y: x * y, numbers))
    print("Sum with init 10:", reduce(lambda x, y: x + y, numbers, 10))


def demo_zip_pairs() -> None:
    names = ["Ravi", "Anu", "Sita"]
    scores = [90, 85, 88]
    for name, score in zip(names, scores):
        print(f"  {name}: {score}")
    print("As dict:", dict(zip(names, scores)))


def payroll_example() -> None:
    employees = [
        {"name": "Ravi", "salary": 50000},
        {"name": "Anu", "salary": 65000},
        {"name": "Sita", "salary": 40000},
        {"name": "Vikram", "salary": 80000},
    ]
    updated = list(map(lambda e: {**e, "salary": round(e["salary"] * 1.1, 2)}, employees))
    high = list(filter(lambda e: e["salary"] > 60000, updated))
    total = reduce(lambda acc, e: acc + e["salary"], updated, 0)
    print("Updated salaries:", updated)
    print("High earners (>60k):", [e["name"] for e in high])
    print("Total payroll:", total)


# P1: map str.strip on list of messy strings.
# P2: filter salaries > 50k from a list.
# P3: reduce to find max in list (no built-in max).
# P4: zip two lists into dict comprehension.
# P5: payroll: add 5% bonus only for dept=="IT" (dict field).

def run_classroom_demo() -> None:
    demo_lambda()
    demo_map()
    demo_filter()
    demo_reduce()
    demo_zip_pairs()
    payroll_example()


if __name__ == "__main__":
    run_classroom_demo()