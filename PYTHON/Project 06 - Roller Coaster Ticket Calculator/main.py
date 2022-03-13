try:
    height = int(input("Enter your height in cm: "))
    total_bill = 0

    if height > 120:
        print("You can ride the Roller Coaster.")
        age = int(input("Kindly, Enter your age: "))
        if age <12:
            print("Your Ticket costs 5$")
            total_bill += 5
        elif age <=18:
            print("Your ticket cost 7$ ")
            total_bill += 12
        else:
            print("Your Ticket cost 12$")
            total_bill += 12

        photo = input("Do you want photo? yes/no: ").title()
        if photo == "No":
            print(f"Total Bill = {total_bill}")
        else:
            print("Your ticket will cost extra 3$ for photos.")
            proceed = input("Do you want to proceed? yes/no: ").title()
            if proceed == "Yes":  
                total_bill += 3
                print(f"Total Bill = {total_bill}")
            else: 
                print(f"Total Bill = {total_bill}")
    else:
        print("We are Sorry!. You can't ride.")
except ValueError:
    print("Wrong Input")