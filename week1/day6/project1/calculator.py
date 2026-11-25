def python_calculator():
    user_input = input("Enter the expression: ") # 10+20*30-40+40
    # e.g: 10+20*30-40    
    user_input_list = user_input.split("+") # [10, 20*30-40', 40]
    print(user_input_list)
    user_input_list = [x.strip() for x in user_input_list] # []
    # l2=[10, 20*30-40']
    l2=user_input_list
    s=0
    for i in l2:
        s=s+eval(i) # print(eval("10+10*50"))
    return s


# result = python_calculator()
# print(f'Result is: {result}')
