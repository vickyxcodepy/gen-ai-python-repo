def guess_num():
    import random
    print("welcome to the number guessing game")
    print("enter the number 1-100")
    
    secret_num = random.randint(1,100)
    
    for i in range (0,7):
        try:
            user_input = int(input("enter the number"))
            if secret_num < 1 or secret_num > 100:
                print("invalid number")
            elif secret_num > user_input:
                print("lesser")
            elif secret_num < user_input:
                print("higher")
            else:
                print("right")
                break
        except ValueError:
            print("this is not an integer ,enter number 1-100")
    
    if secret_num == user_input:
        print(f"correct number is {secret_num} in {i} attempt")
    else:
        print("limit over,try again")
