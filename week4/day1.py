"""
Week 4 — Day 1: OOP Foundations
===============================

PYTHON CLASSROOM
----------------
1. class / object / method / self
2. __init__ and instance vs class attributes
3. Inheritance + super()
4. Polymorphism (override in subclass)
5. Practice P1–P5

PYTHON RECALL
-------------
- class = blueprint; object = instance in memory.
- self always first param in instance methods (by convention).
- Class attr shared; instance attrs per object.
- Encapsulation / ABC: week4/day2.py (not repeated here).
- Capstone project OOP: week4/day5.py.
"""


class Employee:
    company = "Infosys"

    def __init__(self, emp_id: int, name: str) -> None:
        self.emp_id = emp_id
        self.name = name

    def show_details(self) -> None:
        print(f"  ID {self.emp_id}, {self.name}, company={Employee.company}")


class Manager(Employee):
    def __init__(self, emp_id: int, name: str, team_size: int) -> None:
        super().__init__(emp_id, name)
        self.team_size = team_size

    def show_manager(self) -> None:
        print(f"  Manager {self.name}, team size={self.team_size}")


class Developer(Employee):
    def show_details(self) -> None:
        print(f"  Developer {self.name} (ID {self.emp_id})")


def demo_class_and_object() -> None:
    print("OOP organizes code as classes + objects.")
    emp1 = Employee(101, "Rahul")
    emp2 = Employee(102, "Anita")
    emp1.show_details()
    emp2.show_details()


def demo_self_note() -> None:
    emp = Employee(103, "Demo")
    print("self = the object that called the method (emp1 vs emp2).")


def demo_inheritance() -> None:
    mgr = Manager(201, "Vikas", 10)
    mgr.show_details()
    mgr.show_manager()


def demo_polymorphism() -> None:
    roster: list[Employee] = [Employee(301, "Ravi"), Developer(401, "Neha")]
    for person in roster:
        person.show_details()


# PYTHON RECALL — Practice (P1–P5)
# P1: Product class with price, qty, line_total() method.
# P2: Student subclass with grade; call super().__init__.
# P3: Two objects; change only one instance attribute.
# P4: Class attribute vs instance — increment counter on class.
# P5: List of mixed subclasses; same method name, different output.

def run_classroom_demo() -> None:
    demo_class_and_object()
    demo_self_note()
    demo_inheritance()
    demo_polymorphism()


if __name__ == "__main__":
    run_classroom_demo()