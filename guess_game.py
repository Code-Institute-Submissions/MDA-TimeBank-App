"""
REGISTER FUNCTION - Validated but simplified with bootstrap
"""
"""
QUESTIONS_ANSWERS FUNCTION - Validated and defined& called on view page
"""
"""
LIMIT # OF QUESTIONS TO 2
"""
"""
UNTESTED! Refactor of limit_number_questions code
"""
def limit_number_questions(guess, answer):
    if guess <= 0:
      return 0
    elif guess == answer:
      return 10
    else:
      if guess > answer + 10:
        return 0
      elif guess < answer - 10:
        return 0
      elif guess > answer and guess <= answer + 10:      
        return 5
      elif guess < answer and guess >= answer - 10: 
        return 5 


        


   
   