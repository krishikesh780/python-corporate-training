def calculate_salary(basic, hra=0.2, da=0.1):
    return basic + hra*basic + da*basic


def bonus_salary(basic, bonus=0.05):
    return basic * bonus
