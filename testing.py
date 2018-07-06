import unittest


"""
Guess range relative to answer
"""
def guess_range(guess, answer):
    if guess <= 0:
        return True
    elif guess == answer:
        return True
    elif guess > answer and guess <= answer + 10:
        return True    
    elif guess < answer and guess >= answer - 10:
        return True
    elif guess >= answer + 10:
        return True
    elif guess <= answer - 10:
        return True
    
    # return False catches all guesses not targeted
    return False

assert guess_range(0, 4) == True, "Guess is 0"
# assert guess_range(1, 4) == False, "Guess is 0"
assert guess_range(-5, 4) == True, "Guess is less than 0"
# assert guess_range(6, 4) == False, "Guess is less than 0"
assert guess_range(15, 15) == True, "Guess is equal to answer"
assert guess_range(14, 10) == True, "Guess is within 10+ point range of answer"
assert guess_range(6, 10) == True, "Guess is within 10- point range of answer"
# assert guess_range(25, 15) == False, "Guess is equal to answer"
assert guess_range(25, 15) == True, "Guess 10 or more greater than answer"
assert guess_range(32, 15) == True, "Guess 10 or more greater than answer"
# assert guess_range(20, 15) == False, "Guess 10 or more greater than answer"
assert guess_range(5, 15) == True, "Guess 10 or more fewer than answer"
assert guess_range(2, 15) == True, "Guess 10 or more fewer than answer"
# assert guess_range(12, 15) == False, "Guess 10 or more fewer than answer"


"""
Score based on guess range relative to answer
"""
score = []

def allocate_points(guess, answer):
    
    # 0 points
    if guess <= 0:
        score.append(0)
        return int(sum(score))
    if guess >= answer + 10:
        score.append(0)
        return int(sum(score))    
    if guess <= answer - 10:
        score.append(0)
        return int(sum(score))
    
    # 10 points
    if guess == answer:
        score.append(10)
        return int(sum(score))

    # 5 points
    if guess <= answer - 10:
        score.append(5)
        return int(sum(score))



assert allocate_points(0, 8) == 0, "Guess is 0, score is 0"
assert allocate_points(-5, 8) == 0, "Guess is below 0, score is 0"
assert allocate_points(20, 8) == 0, "Guess 10 or more greater than answer, score is 0"
assert allocate_points(6, 18) == 0, "Guess 10 or more fewer than answer, score is 0"
assert allocate_points(8, 8) == 10, "Guess is equal to answer, score is 10"
assert allocate_points(8, 8) == 5, "Guess is equal to answer, score is 10"




print("All tests passed")