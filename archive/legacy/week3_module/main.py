# Method1: When both files are in same package (folder with __init__.py)
# from . import calculator  # This works only if run as package (python -m week2.finance.main)
# from salary import calculate_salary
# from tax import calculate_tax

# from module_name import function_name
# from salary import calculate_salary, bonus_salary

from salary import * # imports all functions from salary.py
from tax import calculate_tax
import sys
import os

#Method2: When files are in different packages (folders with __init__.py)
# sys.path.append(r"D:\python_corporate_training")  # <-- add project ROOT
# current_dir = os.getcwd()
# print("Current Directory:", current_dir)
# print("Current Directory:", current_dir)
# print(f"sys.path: {sys.path}")
# sys.path.append(current_dir)  # <-- add folder that contains calculator.py
# print(f"sys.path: {sys.path}")


current_dir = os.getcwd()
sys.path.append(current_dir)  # <-- add folder that contains calculator.
# print(f"sys.path: {sys.path}")
from week1.day6.project1 import calculator

# Method3: Conditional imports (works in both cases, but not very clean)
# try:
#     # Preferred when package is used (python -m week2.finance.main)
#     from .salary import calculate_salary
#     from .tax import calculate_tax
# except Exception:
#     # Fallback when running the file directly (python main.py)
#     # or when relative imports are not available
#     from salary import calculate_salary
#     from tax import calculate_tax


def main():
    # print("Salary:", calculate_salary(50000))# basic + hra*basic + da*basic
    # print(F"Bonus: {bonus_salary(1000)}")
    # print("Tax:", calculate_tax(50000)) #income * rate =50000*0.1=5000
    print("Calculator Result:", calculator.python_calculator())
    # print("dummy o/p:" , dummy.add())
    

if __name__ == "__main__":
    main()
