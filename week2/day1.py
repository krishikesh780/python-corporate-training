"""
Week 2 — Day 1: Functions (Basics)
==================================

PYTHON CLASSROOM
----------------
1. Local vs global scope
2. def, docstring, call
3. Parameters & return (single / multiple)
4. Positional vs keyword arguments
5. Default parameters
6. *args and **kwargs
7. Passing list / tuple / dict into functions
8. Function as argument (first-class functions)
9. Practice P1–P5

PYTHON RECALL
-------------
- return ends the function — code after return never runs.
- Default args evaluated once at def time — avoid mutable defaults.
- *args → tuple; **kwargs → dict.
- Lambda / map / filter: week2/day2.py (not repeated here).
"""

GLOBAL_X = 100


def demo_scope() -> None:
    global GLOBAL_X
    local_x = 50
    print("Inside function, local:", local_x)
    print("Inside function, global name read:", GLOBAL_X)


def greet() -> None:
    """No parameters, no return — side effect only."""
    print("Hello, Welcome to Python Corporate Training!")


def add_three(a: int, b: int, c: int) -> tuple[int, int, int, int]:
    """Returns all inputs plus their sum."""
    total = a + b + c
    return a, b, c, total


def employee_info(name: str, dept: str, salary: int) -> None:
    print(f"Name: {name}, Department: {dept}, Salary: {salary}")


def demo_arguments() -> None:
    employee_info("Ravi", "IT", 50000)
    employee_info(dept="HR", name="Anu", salary=60000)
    employee_info(name="Sita", salary=70000, dept="Finance")


def connect_db(host: str = "localhost", port: int = 3306) -> None:
    print(f"Connecting to {host}:{port}")


def demo_defaults() -> None:
    connect_db()
    connect_db("db.company.com", 5432)


def calculate_total(*numbers: int) -> int:
    print("Args received (tuple):", numbers)
    return sum(numbers)


def employee_details(**fields: str | int) -> None:
    print("Kwargs received (dict):", fields)
    for key, value in fields.items():
        print(f"  {key}: {value}")


def show_collection(data: list | tuple | dict) -> None:
    print("Collection received:", data)


def apply_function(func, value):
    return func(value)


def double(n: int) -> int:
    return n * 2


# P1: Function area_of_circle(r) with default pi=3.14.
# P2: *args average of n numbers.
# P3: **kwargs print student profile from keys.
# P4: Return min and max from a list (one function).
# P5: apply_function with your own squaring lambda.

def run_classroom_demo() -> None:
    demo_scope()
    print("Outside function, global:", GLOBAL_X)

    greet()
    print("add_three:", add_three(10, 20, 50))

    demo_arguments()
    demo_defaults()
    print("Total:", calculate_total(10, 20, 30, 40))
    employee_details(name="Ravi", dept="IT", salary=50000, location="Pune")

    show_collection([10, 20, 30])
    show_collection(("apple", "banana", "mango"))
    show_collection({"id": 101, "name": "Ravi"})

    print("apply double:", apply_function(double, 5))
    print("apply lambda:", apply_function(lambda x: x + 100, 50))


if __name__ == "__main__":
    run_classroom_demo()