try: 
    year = int(input("Which year do you want to check? "))
    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                print(f"{year} is a Leap year.")
            else:
                print(f"{year} is not Leap year.")
        else:
            print(f"{year} is a Leap year.")
    else:
        print(f"{year} is not Leap year.")
except ValueError: 
    print("You have entered wrong input value")