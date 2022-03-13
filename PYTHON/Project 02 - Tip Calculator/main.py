
print("Welcome to 'Bill Distributor'")
# Collecting Data 
total_bill = float(input("What was the total bill in Dollars? $"))
people = int(input("How many people to split the bill? "))
percentage_distribution = float(input("What percentage tip would you like to give? (5, 10, 12, 15) "))

# Calculations 
bill_with_tip = total_bill + ((percentage_distribution/100)*total_bill)
bill_per_person = float(bill_with_tip/people)

# Output:
print(f"Each person should pay: ${bill_per_person}")
