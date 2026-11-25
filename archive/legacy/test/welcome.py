def welcome():
    print("Welcome to test")

# Due to this when you import it in any place then it will not direclty call welcome() while without it it call automatically in import place
if __name__=="__main__": 
    welcome()