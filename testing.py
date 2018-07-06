import unittest

def calc_score(guess, answer):
    if guess <= 0:
        score == 0
        return True
    if guess == answer:
        return True
    if guess >= answer + 10:
        return True
    if guess <= answer - 10:
        return True
    else: 
        # return False catches all guesses not targeted
        return False

# Guess range relative to answer
assert calc_score(0, 4) == True, "Guess is 0"
assert calc_score(1, 4) == False, "Guess is 0"
assert calc_score(-5, 4) == True, "Guess is less than 0"
assert calc_score(6, 4) == False, "Guess is less than 0"
assert calc_score(15, 15) == True, "Guess is equal to answer"
# assert calc_score(25, 15) == False, "Guess is equal to answer"
assert calc_score(25, 15) == True, "Guess 10 or more greater than answer"
assert calc_score(32, 15) == True, "Guess 10 or more greater than answer"
assert calc_score(20, 15) == False, "Guess 10 or more greater than answer"
assert calc_score(5, 15) == True, "Guess 10 or more fewer than answer"
assert calc_score(2, 15) == True, "Guess 10 or more fewer than answer"
assert calc_score(12, 15) == False, "Guess 10 or more fewer than answer"


# Score based on guess range relative to answer
assert calc_score(0, 6) == True, score == 0, "Score is 0"


print("All tests passed")