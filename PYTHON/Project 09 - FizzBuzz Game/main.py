print("Welcome to Fizz Buzz Game")

game_on = True
while game_on:
    try:
        number = int(input("Enter an whole number: "))
        if number%3 == 0 and number%5 ==0: 
            print("Fuzz Buzz")
        elif number%3 == 0:
            print("Fuzz")
        elif number%5 ==0:
            print("Buzz")
        else:
            print("You lose! Game Over")
            game_on = False
    except ValueError:
        print("You have entered an invalid input")
