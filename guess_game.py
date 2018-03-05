"""
REGISTER FUNCTION - Validated but simplified with bootstrap
"""
"""
QUESTIONS_ANSWERS FUNCTION - Validated and defined& called on view page
"""


"""
LIMIT # OF QUESTIONS TO 2
"""
def limit_number_questions(guess_1, guess_2, answer):
    if guess_1 == answer:
        return 10
    else:
        if guess_2 == answer:
            return 8
        elif ((guess_2 > answer) and (guess_2 < (answer + 10))) or ((guess_2 < answer) and (guess_2 > (answer - 10))):
            return 5
        else:
            return 0
        


   
   