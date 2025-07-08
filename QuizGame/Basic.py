from termcolor import colored
score = 0

answer1 = input("What is the capital of India?\nA) New Delhi\nB) Mumbai\nC) Kolkata\nD) Chennai\nYour answer(A/B/C/D): ")
# Check the answer
if answer1.upper() == "A":
    print(colored("Correct!", "green"))
    score += 1
else:
    print(colored("Incorrect. The capital of India is New Delhi.", "red"))

answer2 = input("What is the largest planet in our solar system?\nA) Earth\nB) Jupiter\nC) Saturn\nD) Mars\nYour answer(A/B/C/D): ")
# Check the answer
if answer2.upper() == "B":
    print(colored("Correct!", "green"))
    score += 1
else:
    print(colored("Incorrect. The largest planet in our solar system is Jupiter.", "red"))

answer3 = input("What is the chemical symbol for water?\nA) CO2\nB) H2O\nC) O2\nD) NaCl\nYour answer(A/B/C/D): ")
# Check the answer
if answer3.upper() == "B":
    print(colored("Correct!", "green"))
    score += 1
else:
    print(colored("Incorrect. The chemical symbol for water is H2O.", "red"))

print(f"Your total score is: {score}/3")