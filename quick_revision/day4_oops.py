"""
Quick Revision — Day 4: OOP
===========================
class/object, static/class methods, inheritance, polymorphism, encapsulation, ABC.
Full course: ../week4/day1–2
"""

from abc import ABC, abstractmethod


class Person:
    species = "Human"

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def intro(self) -> str:
        return f"{self.name}, {self.age}"


class Employee(Person):
    def __init__(self, name: str, age: int, emp_id: int):
        super().__init__(name, age)
        self.emp_id = emp_id


class Payment(ABC):
    @abstractmethod
    def pay(self, amount: float) -> None:
        pass


class UPI(Payment):
    def pay(self, amount: float) -> None:
        print(f"UPI ₹{amount}")


class BankAccount:
    def __init__(self, balance: float):
        self.__balance = balance

    def deposit(self, amount: float) -> None:
        self.__balance += amount

    def get_balance(self) -> float:
        return self.__balance


class Company:
    name = "Training Corp"

    @classmethod
    def rename(cls, new_name: str) -> None:
        cls.name = new_name

    @staticmethod
    def policy() -> str:
        return "Quality first"


def demo_class_and_inherit() -> None:
    e = Employee("Rohit", 25, 101)
    print("Employee:", e.intro(), e.emp_id)


def demo_polymorphism() -> None:
    methods: list[Payment] = [UPI()]
    for m in methods:
        m.pay(500)


def demo_encapsulation() -> None:
    acc = BankAccount(1000)
    acc.deposit(250)
    print("balance:", acc.get_balance())


def demo_class_static() -> None:
    print("company:", Company.name)
    Company.rename("Rev Corp")
    print("static:", Company.policy(), "|", Company.name)


def run_revision() -> None:
    demo_class_and_inherit()
    demo_polymorphism()
    demo_encapsulation()
    demo_class_static()


if __name__ == "__main__":
    run_revision()