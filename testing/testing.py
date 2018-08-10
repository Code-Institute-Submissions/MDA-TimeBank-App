import unittest
import json

"""
Guess range relative to answer
"""
def guess_range(guess, answer):
    if guess < 0:
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
    
"""tests"""
assert guess_range(-5, 4) == True, "Guess is less than 0"
assert guess_range(15, 15) == True, "Guess is equal to answer"
assert guess_range(14, 10) == True, "Guess is within +10 point range of answer"
assert guess_range(6, 10) == True, "Guess is within -10 point range of answer"
assert guess_range(25, 15) == True, "Guess 10 or more greater than answer"
assert guess_range(32, 15) == True, "Guess 10 or more greater than answer"
assert guess_range(5, 15) == True, "Guess 10 or more fewer than answer"
assert guess_range(2, 15) == True, "Guess 10 or more fewer than answer"


"""
Score based on guess range relative to answer
"""
score_list = []

def allocate_points(guess, answer):
    
    # 0 points
    if guess < 0:
        score_list.append(0)
        return int(sum(score_list))
    elif guess >= answer + 10:
        score_list.append(0)
        return int(sum(score_list))    
    elif guess <= answer - 10:
        score_list.append(0)
        return int(sum(score_list))
    
    # 10 points
    elif guess == answer:
        score_list.append(10)
        return int(sum(score_list))

    # 5 points (15 in total)
    elif guess < answer and guess >= answer - 10: 
        score_list.append(5)
        return int(sum(score_list))    
    
    # 5 points (20 in total)
    elif guess > answer and guess <= answer + 10: 
        score_list.append(5)
        return int(sum(score_list))

"""tests"""
assert allocate_points(-5, 8) == 0, "Guess is below 0, score is 0"
assert allocate_points(20, 8) == 0, "Guess 10 or more greater than answer, score is 0"
assert allocate_points(6, 18) == 0, "Guess 10 or more fewer than answer, score is 0"
assert allocate_points(8, 8) == 10, "Guess is equal to answer, score is 10"
assert allocate_points(9, 18) == 15, "Guess is within 10- point range of answer, score is 5"
assert allocate_points(22, 18) == 20, "Guess is within 10+ point range of answer, score is 5"

print("all allocate_points tests passed!")


"""
Refactored code merging above functions
"""
score = []

def calc_score(guess, answer):
    if guess < 0:
        points = 0
    elif guess == answer:
        points = 10
    else:
        if guess > answer + 10:
            points = 0
        elif guess < answer - 10:
            points = 0
        elif guess > answer and guess <= answer + 10:      
            points = 5  
        elif guess < answer and guess >= answer - 10: 
            points = 5
    score.append(points)
    return int(sum(score))

"""tests"""
assert calc_score(-5, 8) == 0, "Guess is below 0, score is 0"
assert calc_score(20, 8) == 0, "Guess 10 or more greater than answer, score is 0"
assert calc_score(6, 18) == 0, "Guess 10 or more fewer than answer, score is 0"
assert calc_score(8, 8) == 10, "Guess is equal to answer, score is 10"
assert calc_score(9, 18) == 15, "Guess is within 10- point range of answer, score is 5"
assert calc_score(22, 18) == 20, "Guess is within 10+ point range of answer, score is 5"

print("all calc_score tests passed!")


"""
Test the registration & storage to .txt file
"""
user_list = []

def registration(name, email, comments, score):
    score = int(sum(score))
    user_list = []

    user_dict = {
        "name": name,
        "email": email,
        "comments": comments,
        "score": score,
    }
    user_list.append(user_dict)
    
    # store list to .txt file and check it manually
    with open('testing/test_user_data.txt', 'w') as outfile:  
        json.dump(user_list, outfile)
    return user_list

"""tests"""
assert registration("martin", "me@me.com", "yeeha", score) == [{'name': 'martin', 'email': 'me@me.com', 'comments': 'yeeha', "score": 20}]
print("registration tests passed!")

# state that test suite is passing
print("All tests passed... Nice one!")