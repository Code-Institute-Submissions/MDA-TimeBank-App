"""
REGISTER FUNCTION - Validated but simplified with bootstrap
"""
"""
QUESTIONS_ANSWERS FUNCTION
# """
def ask_questions(guess, answer):
    if guess is str(guess):
        return 0
    elif guess == answer:
        return 10
    elif ((guess > answer) and (guess < (answer + 10))) or ((guess < answer) and (guess > (answer - 10))):
        return 5
    else:
        return 0
   
   