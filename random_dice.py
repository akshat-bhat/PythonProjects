import random

while True:
    # Ask the user if they want to roll the die
    choice = input("Roll the Die (y/n)?: ").lower()

    if choice == 'y':
        die1 = random.randint(1, 6)  # Roll the die
        die2 = random.randint(1, 6)  # Roll the die
        print(f"you rolled ({die1}, {die2})")

    elif choice == 'n':
        print("Thanks for playing!")
        break

    else:
        print('invalid choice!')