# Ask rps?
# check for valid input
# Compare with comps random rps
# Determine winner
# if invalid input, ask again
import random

choices = ('r', 'p', 's')
emojies = {'r' : '🪨', 'p' : '📄', 's' : '✂️'}

while True:
    user_choice = input("Rock, Paper, or Scissors? (r/p/s): ").lower()
    if user_choice not in choices:
        print("Invalid choice!")
        continue #-------------------##IMPORTANT to jump back to the start###

    computer_choice = random.choice(choices)

    print (f"You chose {emojies[user_choice]}\nComputer chose {emojies[computer_choice]}")

    if user_choice == computer_choice:
        print("Tie!")
    elif(
        (user_choice == 'r' and computer_choice == 's') or
        (user_choice == 'p' and computer_choice == 'r') or
        (user_choice == 's' and computer_choice == 'p')):
        print("You win!")
    else: print("You lose!")

    should_continue = input("Continue? (y/n)").lower()
    if should_continue == 'n':
        break
    elif should_continue == 'y':
        continue
    else:
        print("Invalid Input so we continue ;)")
