try:
    number = int(input("Which whole number do you want to check? "))
    if number % 2 == 0: 
        print(f"You enter {number}, which is an Even number.")
    else:
        print(f"You enter {number}, which is an Odd number.")
except ValueError:
    print("You have entered Wrong Input")



