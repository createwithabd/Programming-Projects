try:
    height = float(input("Enter your height in cm: ")) /100
    weight = float(input("Enter your weight in Kg: "))
    bmi = round(weight/height**2, 2)

    # Conditional Output 

    if bmi <= 18.5: 
        print(f"your BMI is {bmi}, and you are Under Weight")
    elif bmi >18.5 and bmi < 25:
        print(f"your BMI is {bmi}, and you are Normal Weight")
    elif bmi >25 and bmi < 35:
        print(f"your BMI is {bmi}, and you are Obese Weight")
    else:
        print(f"your BMI is {bmi}, and you are Clinically Obese")
except ValueError:
    print("you have entered wrong input value")