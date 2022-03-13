from ascii import game_list
import random

print("Welcome to ROCK, PAPER, SCISSOR GAME")


user_number = int(input("What do you choose? Enter 0 for Rock, 1 for Paper, 2 for Scissor: "))
computer_number = random.randint(0, len(game_list)-1)
computer_choose = game_list[computer_number]

if user_number > 2: 
    print("You have entered a wrong input!")
else:
    user_choice = game_list[user_number]
    print(f"User Choose:\n{user_choice}")
    print(f"Computer Choose:\n{computer_choose}")
    if user_number == computer_number:
        print("Game Draw. Try Ag")
    elif user_number == 0 and computer_number == 2:
        print("Congratulations! You Win 🎉")
    elif user_number == 1 and computer_number == 0:
        print("Congratulations! You Win 🎉")
    elif user_number ==2 and computer_number == 1:
        print("Congratulations! You Win 🎉")
    else: 
        print("Computer Wins.") 
