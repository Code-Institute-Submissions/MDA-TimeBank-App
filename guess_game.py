"""
REGISTER FUNCTION - Validated but simplified with bootstrap
"""
"""
QUESTIONS_ANSWERS FUNCTION
# """
def ask_questions(guess, answer):
    score = 0
    if guess is str(guess):
        score = score + 0
    elif guess == answer:
        score = score + 10
    elif ((guess > answer) and (guess < (answer + 10))) or ((guess < answer) and (guess > (answer - 10))):
        score = score + 5
    else:
        score = score + 0
    return score

  


   
   