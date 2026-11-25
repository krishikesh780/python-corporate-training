# 8. Function as Argument
# -------------------------------
def apply_function(func, value):
    """Takes another function as input""" #
    return func(value) # double(5) # 10

def double(n):
    return n * 2

print("Apply function:", apply_function(double, 5))
# print("Apply lambda:", apply_function(lambda x: x + 100, 50))
