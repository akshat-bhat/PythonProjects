# Ask rps?
# check for valid input
# Compare with comps random rps
# Determine winner
# if invalid input, ask again
import random

#Declaring constants to avoid mistakes
ROCK = 'r'
PAPER = 'p'
SCISSOR = 's'

emojies = {'ROCK' : '🪨', 'PAPER' : '📄', 'SCISSOR' : '✂️'} #------##DICTIONARY###


choices = tuple(emojies.keys())

def get_user_choice():
    while True:
        user_choice = input("Rock, Paper, or Scissors? (r/p/s): ").lower()
        if user_choice not in choices:
            print("Invalid choice!")
            continue #-------------------##IMPORTANT to jump back to the start###
        else:
            return user_choice
    
def display_choices(user_choice, computer_choice):
    print (f"You chose {emojies[user_choice]}\nComputer chose {emojies[computer_choice]}")

def determining_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("Tie!")
    elif(
        (user_choice == 'ROCK' and computer_choice == 'SCISSOR') or
        (user_choice == 'PAPER' and computer_choice == 'ROCK') or
        (user_choice == 'SCISSOR' and computer_choice == 'PAPER')):
        print("You win!")
    else: print("You lose!")

def play_game():
    while True:
        user_choice = get_user_choice()

        computer_choice = random.choice(choices)

        display_choices(user_choice, computer_choice)

        determining_winner(user_choice, computer_choice)

        should_continue = input("Continue? (y/n) ").lower()
        if should_continue == 'n':
            break
        elif should_continue == 'y':
            continue
        else:
            print("Invalid Input so we continue ;)")
 
play_game()