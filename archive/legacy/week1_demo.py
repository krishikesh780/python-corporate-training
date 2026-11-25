def demo_continue():
    for i in range(1, 6): # 1,2,3,4,5
        if i == 3:  #i==3
            print("Skipping")
            continue 
        print("Value:", i)


demo_continue()