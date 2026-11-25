"""
Week 4 — Day 2: OOP Advanced
==============================

PYTHON CLASSROOM
----------------
1. Encapsulation (__private, getters)
2. Abstraction (ABC, @abstractmethod)
3. Method overriding
4. Multiple inheritance
5. @classmethod vs @staticmethod
6. Practice P1–P5

PYTHON RECALL
-------------
- __name mangles to _Class__name — convention, not true security.
- ABC cannot be instantiated until abstract methods implemented.
- MRO resolves multiple inheritance order (search order).
- Basics (class/self/inherit): week4/day1.py.
"""

from abc import ABC, abstractmethod


class BankAccount:
    def __init__(self, acc_no: str, balance: float) -> None:
        self.acc_no = acc_no
        self.__balance = balance

    def deposit(self, amount: float) -> None:
        self.__balance += amount

    def get_balance(self) -> float:
        return self.__balance


class Vehicle(ABC):
    @abstractmethod
    def start(self) -> None:
        pass


class Car(Vehicle):
    def start(self) -> None:
        print("  Car engine started.")


class Bike(Vehicle):
    def start(self) -> None:
        print("  Bike engine started.")


class Animal:
    def sound(self) -> None:
        print("  Animal sound")


class Dog(Animal):
    def sound(self) -> None:
        print("  Dog barks")


class Cat(Animal):
    def sound(self) -> None:
        print("  Cat meows")


class Teacher:
    def teach(self) -> None:
        print("  Teaching...")


class SportsCoach:
    def train(self) -> None:
        print("  Training...")


class SportsTeacher(Teacher, SportsCoach):
    pass


class Company:
    company_name = "Infosys"

    def __init__(self, emp_name: str) -> None:
        self.emp_name = emp_name

    @classmethod
    def rename(cls, new_name: str) -> None:
        cls.company_name = new_name

    @staticmethod
    def policy() -> None:
        print("  Policy: quality first.")


def demo_encapsulation() -> None:
    acc = BankAccount("12345", 1000)
    acc.deposit(500)
    print("  Balance via method:", acc.get_balance())


def demo_abstraction() -> None:
    for v in (Car(), Bike()):
        v.start()


def demo_overriding() -> None:
    for a in (Animal(), Dog(), Cat()):
        a.sound()


def demo_multiple_inheritance() -> None:
    st = SportsTeacher()
    st.teach()
    st.train()


def demo_class_and_static() -> None:
    print("  Company:", Company.company_name)
    Company.rename("TCS")
    print("  Renamed:", Company.company_name)
    Company.policy()


# PYTHON RECALL — Practice (P1–P5)
# P1: BankAccount with withdraw() that blocks negative balance.
# P2: Shape ABC with Circle.area() implementation.
# P3: Override __str__ on Customer (day5 project style).
# P4: @classmethod alternate constructor from dict.
# P5: Explain MRO for SportsTeacher with print(SportsTeacher.mro()).

def run_classroom_demo() -> None:
    demo_encapsulation()
    demo_abstraction()
    demo_overriding()
    demo_multiple_inheritance()
    demo_class_and_static()


if __name__ == "__main__":
    run_classroom_demo()