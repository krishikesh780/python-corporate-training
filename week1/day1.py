"""
Week 1 — Day 1: Introduction to Python
======================================

PYTHON CLASSROOM (Today's flow)
-------------------------------
1. Setup: Python + VS Code
2. print(), comments (# and \"\"\" \"\"\")
3. Indentation (if / for / while / def / class)
4. Variable naming rules
5. Data types: int, float, str, bool
6. Type casting: int(), float(), str(), bool()
7. input() and formatted output (f-strings)
8. Operators (arithmetic, assignment, comparison, logical)
9. Example: even / odd
10. Practice P1–P5 (bottom of file)

PYTHON RECALL (memory hooks)
----------------------------
- Python is interpreted; run line-by-line or via scripts.
- Indentation = blocks (no { } braces).
- Names: start with letter or _ ; use snake_case for variables.
- Dynamic typing: type can change; use type() to check.
- input() always returns str — cast before math.
- // floor div, % remainder, ** power.
- == compare values, = assign.
"""

# -----------------------------------------------------------------------------
# 1. Printing & comments
# -----------------------------------------------------------------------------

def demo_printing(msg: str = "Hello, World!") -> None:
  # Shortcut to comment: Ctrl + /
  print(msg)
  # This is a single-line comment.

  """
  Triple quotes: docstring or multi-line comment (not executed as code).
  """


# -----------------------------------------------------------------------------
# 2. Indentation
# -----------------------------------------------------------------------------

def demo_indentation() -> None:
    if True:
        print("Hello")
        print("to Python")
    for i in range(3):
        print("Inside loop:", i)
    print("Done")

    x = 5
    if x > 10:
        print("Greater")
    else:
        print("Smaller or equal")


def demo_indentation_sum() -> int:
    """Shows indented body inside a function."""
    a = 10
    b = 20
    name = "Delhi"
    result = a + b
    print(f"{name}: {a} + {b} = {result}")
    return result


# -----------------------------------------------------------------------------
# 3. Variable naming
# -----------------------------------------------------------------------------

def demo_variable_naming() -> None:
    user_count = 10       # valid — snake_case
    _private = 20           # valid — leading underscore
    score1 = 30.5           # valid — digit after first char
    city = "Delhi"

    # Invalid examples (uncomment only to see SyntaxError):
    # 1a = 40                 # cannot start with a digit
    # user name = 50          # spaces not allowed
    # my-var = 60             # hyphen is minus, not part of name

    print(user_count, _private, score1, city)


# -----------------------------------------------------------------------------
# 4. Variables & basic data types
# -----------------------------------------------------------------------------

def demo_variables(a: int = 0, pi: float = 3.14, name: str = "Ravi", flag: bool = True) -> None:
    print("Values:", a, pi, name, flag)
    print("Types:", type(a), type(pi), type(name), type(flag))


# -----------------------------------------------------------------------------
# 5. Type casting
# -----------------------------------------------------------------------------

def demo_casting() -> None:
    x = "5"
    print("Before cast:", x, type(x))

    x = int(x)
    print("After int():", x, type(x))

    x = float(x)
    print("After float():", x, type(x))

    y = 0
    print("bool(0):", bool(y), "| bool(5):", bool(5))

    z = str(42)
    print("str(42):", z, type(z))


# -----------------------------------------------------------------------------
# 6. Input / output
# -----------------------------------------------------------------------------

def demo_input() -> None:
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    # age is str — cast for numeric use
    print(f"Hello {name}, you entered age {age}.")
    if age.isdigit():
        print(f"In 5 years you will be {int(age) + 5}.")


# -----------------------------------------------------------------------------
# 7. Operators (Day 1 set)
# -----------------------------------------------------------------------------

def python_operators() -> None:
    """Run in class to recall all basic operators."""
    print("=== Python Operators ===\n")

    x, y = 10, 5
    print("1. Arithmetic:")
    print(f"  +  {x + y}  -  {x - y}  *  {x * y}  /  {x / y}")
    print(f"  %  {x % y}  // {x // y}  ** {x ** y}")

    print("\n2. Assignment:")
    a = 10
    a += 3
    print(f"  a += 3 -> {a}")

    print("\n3. Comparison:")
    print(f"  {x} == {y} -> {x == y}  |  {x} != {y} -> {x != y}")
    print(f"  {x} > {y} -> {x > y}  |  {x} < {y} -> {x < y}")

    print("\n4. Logical:")
    print(f"  (5 < 10) and (5 > 0) -> {5 < 10 and 5 > 0}")
    print(f"  (5 < 10) or (5 > 10) -> {5 < 10 or 5 > 10}")
    print(f"  not (5 < 10) -> {not (5 < 10)}")


# -----------------------------------------------------------------------------
# 8. Example program: even / odd
# -----------------------------------------------------------------------------

def even_odd(n: int = 1) -> None:
    if n % 2 == 0:
        print(f"{n} is even")
    else:
        print(f"{n} is odd")


# -----------------------------------------------------------------------------
# PYTHON RECALL — Practice (P1–P5)
# -----------------------------------------------------------------------------
# P1: Print your name and course in one line using f-string.
# P2: Store age as str from input(); print age + 1 after int() cast.
# P3: Show valid vs invalid variable names (write 3 each as comments).
# P4: Compute area of circle: pi=3.14, r from input, area = pi * r ** 2.
# P5: Check if a number is positive, negative, or zero using if / elif / else.

def run_classroom_demo() -> None:
    """Uncomment one line at a time while teaching, or call from REPL."""
    demo_printing()
    demo_printing("Welcome to Python Programming!")
    demo_indentation()
    demo_indentation_sum()
    demo_variable_naming()
    demo_variables(a=10, pi=1.15, name="Delhi", flag=False)
    demo_casting()
    python_operators()
    even_odd(4)
    even_odd(7)
    # demo_input()  # interactive — run when students are ready


if __name__ == "__main__":
    run_classroom_demo()