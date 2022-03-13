import random
from hangman_art import stages, logo
from game_words import word_list

print(logo)
random_word = random.choice(word_list)
length = len(random_word)
display = []

for n in range(length):
    display += "_"

lives = len(stages) -1
game_ends = False
while not game_ends:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You have already guessed '{guess}' ")
    

    for position in range(length):
        letter = random_word[position]
        if guess == letter:
            display[position] = letter
    print(f"{' '.join(display)} ")

    if guess not in random_word:
        print(f"You guessed '{guess}' is wrong . You lose a life.")
        lives -= 1
        if lives == 0:
            game_ends = True
            print(f"You Lose 😞. Word was '{random_word}'")

    if "_" not in display:
        print("You won! 🎉 Here is your Medal 🏅")
        game_ends = True
    
    print(stages[lives])


    


