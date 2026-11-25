"""
Week 2 — Day 3: Modules (Basics)
=================================

PYTHON CLASSROOM
----------------
1. import module — use math, random, os
2. from module import name
3. import … as alias
4. Built-in modules in one script (grouped demos)
5. User module: mymodule.py (same folder)
6. Practice P1–P5

PYTHON RECALL
-------------
- Module = one .py file; name is filename (without .py).
- import loads once per session (cached in sys.modules).
- from x import y brings y into current namespace — may shadow names.
- Packages (folders): week2/day4.py.
- Run this file from week2: python day3.py
"""

import math
import os
import random
import random as rnd

import mymodule
from mymodule import greet as greet_user


def demo_math_import() -> None:
    print("sqrt(16):", math.sqrt(16))
    print("pi:", math.pi)


def demo_from_import() -> None:
    from math import factorial, sqrt

    print("sqrt(25):", sqrt(25))
    print("factorial(5):", factorial(5))


def demo_alias() -> None:
    print("randint:", rnd.randint(1, 100))
    print("choice:", rnd.choice(["apple", "banana", "mango"]))


def demo_os() -> None:
    print("cwd:", os.getcwd())
    here = os.path.dirname(os.path.abspath(__file__))
    print("this folder:", os.path.basename(here))


def demo_user_module() -> None:
    print(mymodule.greet("Ravi"))
    print("10 + 20 =", mymodule.add(10, 20))
    print(greet_user("Anu"))

    import mymodule as mm

    print(mm.greet("Sita"))
    print("Sum via alias:", mm.add(50, 70))


# P1: import datetime; print today's date.
# P2: from math import ceil, floor; demo on 3.7.
# P3: Add multiply(a,b) to mymodule.py; call it here.
# P4: random.sample from a list of 10 names (pick 3).
# P5: os.path.join to build a path string.

def run_classroom_demo() -> None:
    demo_math_import()
    demo_from_import()
    demo_alias()
    demo_os()
    demo_user_module()


if __name__ == "__main__":
    run_classroom_demo()