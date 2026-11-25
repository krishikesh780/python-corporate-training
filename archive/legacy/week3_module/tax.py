def calculate_tax(income, rate=0.5): # income=50k
    return income * rate

def tax_bracket(income):
    if income < 30000:
        return 0.05
    elif income < 100000:
        return 0.1
    else:
        return 0.2