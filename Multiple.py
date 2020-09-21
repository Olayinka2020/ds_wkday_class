from Question import Question

question_prompts = [
    "Which team won the 2015 champions league?\n(a) Manchester United\n(b) Barcelona\n(c) Juventus\n\n",
    "First african artist to reach a billion views on spotify?\n(a) Davido\n(b) Burna Boy\n(c) Wizkid\n\n",
    "Who is Tiwa Savage?\n(a) Hair Dresser\n(b) Tailor\n(c) Artist\n\n",
]

# we need to keep track of what we want to ask and what the answer is

questions = [
    Question(question_prompts[0], "b"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "c")
]

# write a function that will run the test everytimee the user answers a question right, and also increment the users score

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correctly")
    
    
run_test(questions)