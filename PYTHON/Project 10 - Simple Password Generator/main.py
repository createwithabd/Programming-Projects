from variables import *
import random

print("Welcome to Password Generator")

try:
    letters = int(input("How many letters you want in your password? Enter number between 0 and 52 \n"))
    numbers = int(input("How many numbers you want in your password? Enter number between 0 and 10\n"))
    symbols = int(input("How many symbols you want in your password? Enter number between 0 and 9\n"))
except ValueError:
    print("You have entered a wrong input")

password_list = []

for n in range(0, letters):
    password_letters = random.choice(LETTERS)
    password_list.append(password_letters)

for n in range(0, numbers):
    password_numbers = random.choice(NUMBERS)
    password_list.append(password_numbers)

for n in range(0, symbols):
    password_symbols = random.choice(SYMBOLS)
    password_list.append(password_symbols)


random.shuffle(password_list)
password = "".join(password_list)

print(f"Here is your Generated Password: {password}")
