import unittest
import json
    
"""
Game scoring logic
"""

"""Setting guess range relative to answer"""
def guess_range(guess, answer):
    if guess < 0:
        return True
    elif guess == answer:
        return True
    elif guess > answer and guess <= answer + 5:
        return True    
    elif guess < answer and guess >= answer - 5:
        return True
    elif guess >= answer + 5:
        return True
    elif guess <= answer - 5:
        return True
    
# tests
assert guess_range(-5, 4) == True, "Guess is less than 0"
assert guess_range(15, 15) == True, "Guess is equal to answer"
assert guess_range(14, 10) == True, "Guess is within +5 point range of answer"
assert guess_range(6, 10) == True, "Guess is within -5 point range of answer"
assert guess_range(25, 15) == True, "Guess 5 or more greater than answer"
assert guess_range(32, 15) == True, "Guess 5 or more greater than answer"
assert guess_range(5, 15) == True, "Guess 5 or more fewer than answer"
assert guess_range(2, 15) == True, "Guess 5 or more fewer than answer"

print("all guess_range tests passed!")

"""Score based on accuracy of guess"""
def allocate_points(guess, answer):
    score = 0 
    
    # 0 points
    if guess < 0:
        score += 0;
        return score
    elif guess >= answer + 5:
        score += 0
        return score    
    elif guess <= answer - 5:
        score += 0
        return score
    
    # 10 points
    elif guess == answer:
        score += 10
        return score

    # 5 points
    elif guess < answer and guess >= answer - 5: 
        score += 5
        return score    
    
    # 5 points
    elif guess > answer and guess <= answer + 5: 
        score += 5
        return score

# tests
assert allocate_points(-5, 8) == 0, "Guess is below 0, score is 0"
assert allocate_points(20, 8) == 0, "Guess 5 or more greater than answer, score is 0"
assert allocate_points(6, 18) == 0, "Guess 5 or more fewer than answer, score is 0"
assert allocate_points(8, 8) == 10, "Guess is equal to answer, score is 10"
assert allocate_points(14, 18) == 5, "Guess is within -5 point range of answer, score is 5"
assert allocate_points(22, 18) == 5, "Guess is within +5 point range of answer, score is 5"

print("all allocate_points tests passed!")


"""
Refactor code merging guess range and allocate_points functions
"""
def calc_score(guess, answer):
    score = 0    
    
    if guess < 0:
        score += 0
    elif guess == answer:
        score += 10
    else:
        if guess > answer + 10 or guess < answer - 10:
            score = 0
        else:      
            score += 5  
    return score

# tests
assert calc_score(-5, 8) == 0, "Guess is below 0, score is 0"
assert calc_score(20, 8) == 0, "Guess 5 or more greater than answer, score is 0"
assert calc_score(6, 18) == 0, "Guess 5 or more fewer than answer, score is 0"
assert calc_score(8, 8) == 10, "Guess is equal to answer, score is 10"
assert calc_score(15, 18) == 5, "Guess is within -5 point range of answer, score is 5"
assert calc_score(22, 18) == 5, "Guess is within +5 point range of answer, score is 5"

print("all calc_score tests passed!")


"""
Setting game context
"""

"""test accessing data through index"""
def get_challenge(index):
    with open("data/challenge.json", "r") as json_data:
        data = json.load(json_data)
        return data[index] if index <= 7 else None # Catches IndexError if there are no more challenges

assert get_challenge(0)['title'] == 'Computers', "The title is correct" 
assert get_challenge(0)['need_amount'] == 58, "The need amount is correct"
assert get_challenge(0)['skill_answer'] == 78, "The skills answer is correct" 
assert get_challenge(7)['title'] == 'Home Repairs', "The title is correct" 
assert get_challenge(7)['need_amount'] == 23, "The need amount is correct" 
assert get_challenge(7)['skill_answer'] == 18, "The skills answer is correct" 

print("all get_challenge tests passed!")


"""Use get_challenge function to create context for storing values during the challenge"""
def setup_context(username):
    score = 0
    attempt = 1
    challenge = get_challenge(0) # start challenge on index 0 - default
    context = {
        'challenge_id': 0, 
        'title': challenge['title'],
        'need': challenge['need_amount'],
        'statement': challenge['need_statement'],
        'challenge': challenge['skill_question'],
        'answer': challenge['skill_answer'],
        'username': username,
        'attempt': attempt,
        'current_score': score,
        'image': challenge['image'],
    }
    return context

test_context = setup_context("mary")

# tests
assert test_context.get('username', None) == "mary" # player defined value
assert test_context.get('answer', None) == 78 # .json file defined value
assert test_context.get('challenge_id', None) == 0 # .json file defined value
assert test_context.get('current_score', None) == 0 # default value defined in function
assert test_context.get('attempt', None) == 1 # default value defined in function
assert test_context.get('wednesday', None) == None # key does not exist in context

print("all setup_context tests passed!")


"""
Refactor function calc_score (game scoring logic) to execute while there is another challenge
"""
def challenge_run(username, guess):
    test_context = setup_context(username) # entered by player
    challenge_id = test_context['challenge_id']
    attempt = test_context['attempt'] 
    score = test_context['current_score']
    answer = test_context['answer']
    correct = guess == answer
    
    while challenge_id <= 7: # executes while there is another challenge
        if correct: # catches if the guess is correct on first or second attempt
            challenge_id += 1 # if so, moves to next challenge_id
            score += 10 # gives 10 points for correct guess
            attempt = 1 # sets attempt at 1 for next challenge
            next_challenge = get_challenge(challenge_id) # uses challenge_id as param to get next challenge
        
        else:
            if attempt >=2: # checks if there have been 2 or more attempts
                challenge_id += 1 # moves to next challenge_id if true
                attempt = 1 # sets 1st attempt again
            
                if (guess > answer) and (guess <= answer + 5) or (guess < answer) and (guess >= answer - 5):
                    score += 5 # if guess is not correct but is +/-5, give 5 points
                    next_challenge = get_challenge(challenge_id) # uses challenge_id as param to get next challenge
                    
                else: # if guess is not correct or within +/-5 range of answer    
                    next_challenge = get_challenge(challenge_id) # uses challenge_id as param to get next challenge

            else: # if there has only been one attempt
                attempt += 1 # move to second attempt
                next_challenge = get_challenge(challenge_id) # use same challenge_id param
        
        if next_challenge is not None: # if there is another challenge
            context = { # use variables created/updated to update context
                'challenge_id': challenge_id,
                'title': next_challenge['title'],
                'challenge': next_challenge['skill_question'],
                'need': next_challenge['need_amount'],
                'statement': next_challenge['need_statement'],
                'answer': next_challenge['skill_answer'],
                'image': next_challenge['image'],                
                'username': username,
                'current_score': score,
                'attempt': attempt,
            }
            return context  
        
        else: # if there are no more challenges
            return score # return the score


challenge_test = challenge_run("bob505", 78) # set up a correct guess

# will produce the context for the next challenge
assert challenge_test.get("username", None) == "bob505"
assert challenge_test.get("challenge_id", None) == 1
assert challenge_test.get("attempt", None) == 1
assert challenge_test.get("current_score", None) == 10
assert challenge_test.get("answer", None) == 6
assert challenge_test.get("title", None) != "Computers"
assert challenge_test.get("statement", None) == "had bicycles and would benefit from someone carrying out"


challenge_test = challenge_run("bob505", 74) # an incorrect guess (not catching +/-5 on first attempt)

# will only update the current context's attempt to 2
assert challenge_test.get("username", None) == "bob505"
assert challenge_test.get("challenge_id", None) == 0
assert challenge_test.get("attempt", None) == 2
assert challenge_test.get("current_score", None) == 0
assert challenge_test.get("answer", None) == 78
assert challenge_test.get("title", None) != "Bike Repairs"
assert challenge_test.get("statement", None) == "needed support and assistance to be able to confidently use"

print("all scoring & context tests passed!")
    

def count_attempts(guess, answer):
    attempt = 1 # keep attempt at 1 to start on first guess
    score = 0    
    correct = guess == answer
    
    if correct and attempt == 1:
        return "Correct guess in {} attempt".format(attempt)
    else:
        attempt += 1
        return "Guess again. This is attempt #{}".format(attempt)

# tests
assert count_attempts(6, 6) == "Correct guess in 1 attempt"
assert count_attempts(4, 9) == "Guess again. This is attempt #2"

print("all limit_two_attempts tests passed!")
    

print("All tests passed... Nice one!")