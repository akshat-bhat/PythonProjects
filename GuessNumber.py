
import random


number_to_guess = random.randint(1, 100)  # This is the number the user has to guess

while True:
    try:
        guess = int(input("Guess a number between 1 and 100: "))  # Get the user's guess

        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print("Congratulations! You've guessed the number.")
            break

    except ValueError:
        print("Please enter a valid integer.") 

