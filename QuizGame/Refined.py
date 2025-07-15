import random
from termcolor import cprint
score = 0

# Define questions, options ans answers
quiz = [
    {
        'question': "What is the capital of India?",
        'options': ['A) New Delhi', 'B) Mumbai', 'C) Kolkata', 'D) Chennai'],
        'answer': 'A'
    },      ### Shift + Alt + down arrow:  to duplicate selected line of code
    {
        'question': "What is the largest planet in our solar system?",
        'options': ['A) Saturn', 'B) Jupiter', 'C) Earth', 'D) Mars'],
        'answer': 'B'
    },
    {
        'question': "What is the chemical symbol for water?",
        'options': ['A) NaCl', 'B) O2', 'C) CO2', 'D) H2O'],
        'answer': 'D'
    }
]

# Shuffle the questions
random.shuffle(quiz)

# Loop through the questions
for index, item in enumerate(quiz, 1):  ## To start with index 1 we mentioned it in (quiz,1)
    print(f"Question {index+1}: {item['question']}")# Print the question and options
    for option in item['options']:
        print(option)
    # User input
    answer = input("Your answer: ").upper().strip() # To ignore whitespaces with inputs

    if answer.upper() == item['answer']:
        score+=1
        cprint("Correct!", "green")
    else: cprint(f"Incorrect. The correct answer is {item['answer']}", "red")

    print() # empty line for clear code

# Print final score
print(f'Your final score: {score}/{len(quiz)}')
