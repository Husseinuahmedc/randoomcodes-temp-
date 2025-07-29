user = int(input("enter number"))
if user < 3:
    num_list = list(range(0, user + 6))
    con = user + 5
    print(f"this is the list guess the logic of the list ,{num_list}")
elif user == 3:
    num_list = list(range(3, user + 4))
    con = user + 2
    print(f"this is the list guess the logic of the list ,{num_list}")
elif user > 3:
    num_list = list(range(-3, user + 3))
    con = user + 2
    print(f"this is the list guess the logic of the list ,{num_list}")
user_guess = int(input("think and enter the logic of the list: "))
if user_guess == con :
    print("You win !!")
else:
    print("try again , hint the list depands on ur input , there are 3 possible con,. , goodluck")

