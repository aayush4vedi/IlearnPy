import math

while True:
    print("\n Choose one:\n 0 - Add \n 1 - Subtract \n 2 - Multiply \n 3 - Divide\n")
    op = input("Your input: ")
    # do the maths
    if(op == "0"):
        x = float(input("Enter first number: \n"))
        y = float(input("Enter second number: \n"))
        print("Answer is: ", str(x+y), "\n")
        choice = input("do you want to continue playing? y/n \n")
        if(choice == "y"):
            continue
        else:
            break;
    elif(op == "1"):
        x = float(input("Enter first number: \n"))
        y = float(input("Enter second number: \n"))
        print("Answer is: ",str( x-y), "\n")
        choice = input("do you want to continue playing? y/n \n")
        if(choice == "y"):
            continue
        else:
            break;
    elif(op == "2"):
        x = float(input("Enter first number: \n"))
        y = float(input("Enter second number: \n"))
        print("Answer is: ",str( x*y), "\n")
        choice = input("do you want to continue playing? y/n \n")
        if(choice == "y"):
            continue
        else:
            break;
    elif(op == "3"):
        x = float(input("Enter first number: \n"))
        y = float(input("Enter second number: \n"))
        print("Answer is: ", str(x/y), "\n")
        choice = input("do you want to continue playing? y/n \n")
        if(choice == "y"):
            continue
        else:
            break;
    else:
        print("Wrong choice, choose again")

