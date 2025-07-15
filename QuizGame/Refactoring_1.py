import random
from termcolor import cprint
score = 0

########### Replacing magic strings ###########

# Defining Constants to follow DRY principle (Don't repeat yourself)
QUESTION = 'question'
OPTIONS = 'options'
ANSWER = 'answer'
# Renameing keys made easier as ^^ only place needed to modify

# cltr + D : for next selection

# Define QUESTIONs, OPTIONS ans ANSWERs
quiz = [
    {
        'QUESTION': "What is the capital of India?",
        'OPTIONS': ['A) New Delhi', 'B) Mumbai', 'C) Kolkata', 'D) Chennai'],
        'ANSWER': 'A'
    },      ### Shift + Alt + down arrow:  to duplicate selected line of code
    {
        'QUESTION': "What is the largest planet in our solar system?",
        'OPTIONS': ['A) Saturn', 'B) Jupiter', 'C) Earth', 'D) Mars'],
        'ANSWER': 'B'
    },
    {
        'QUESTION': "What is the chemical symbol for water?",
        'OPTIONS': ['A) NaCl', 'B) O2', 'C) CO2', 'D) H2O'],
        'ANSWER': 'D'
    }
]

# Shuffle the QUESTIONs
random.shuffle(quiz)

# Loop through the QUESTIONs
for index, item in enumerate(quiz, 1):  ## To start with index 1 we mentioned it in (quiz,1)
    print(f"Question {index+1}: {item['QUESTION']}")# Print the question and OPTIONS
    for option in item['OPTIONS']:
        print(option)
    # User input
    answer = input("Your answer: ").upper().strip() # To ignore whitespaces with inputs

    if answer.upper() == item['ANSWER']:
        score+=1
        cprint("Correct!", "green")
    else: cprint(f"Incorrect. The correct answer is {item['ANSWER']}", "red")

    print() # empty line for clear code

# Print final score
print(f'Your final score: {score}/{len(quiz)}')
