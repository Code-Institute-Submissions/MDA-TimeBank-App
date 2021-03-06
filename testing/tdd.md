## Testing

A **Test Driven Development** approach was used to develop the application using the folllowing steps:

1. **Identify the functionality that needs to be built and write pseudocode**
2. **Write a test for this feature**
3. **Write the code and test it**
4. **Refactor code, merging with previous functions where possible**
5. **Move to next piece of required functionality - start from step 1**


#### 1. Identify the functionality that needs to be built and write pseudocode
The follow functionality was identified as being necessary for the application:

* determine **accuracy of player's guess** in relation to the answer (``guess_range(guess, answer)``)
* **allocate points** based on the accuracy of the guess (``allocate_points(guess, answer)``)
* **retrieve challenge information** (including answer) from .json file (``get_challenge(index)``)
* **create and update a context** of game information to persist until final question completed (``setup_context(username)``)
* limit player to **two guesses per question** (``count_attempts(guess, answer)``)

Here is an example of the pseudocode written for allocating points based on guess:

    "guess is below 0"
    "guess is equal to answer"
    "guess is within +5 point range of answer"
    "guess is within -5 point range of answer"
    "guess is 5 or more greater than answer"
    "guess is 5 or more fewer than answer"

Based on these requirements, a function with two parameters was created:
    ``def guess_range(guess, answer)``

#### 2. Write tests for this feature
Tests were the developed which were capable assessing whther the function was producing the expected outcome:

    assert guess_range(-5, 4) == True, "Guess is less than 0"
    assert guess_range(15, 15) == True, "Guess is equal to answer"
    assert guess_range(14, 10) == True, "Guess is within +5 point range of answer"
    assert guess_range(6, 10) == True, "Guess is within -5 point range of answer"
    assert guess_range(25, 15) == True, "Guess 5 or more greater than answer"
    assert guess_range(32, 15) == True, "Guess 5 or more greater than answer"
    assert guess_range(5, 15) == True, "Guess 5 or more fewer than answer"
    assert guess_range(2, 15) == True, "Guess 5 or more fewer than answer"

#### 3. Write the code and test it
Code was written to then meet the required functionality (including deliberately failing tests):

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

#### 4. Refactor code, merging with previous functions where possible
The code for the ``guess_range(guess, answer)`` function was then refactored to merge scoring function ``allocate_points(guess, answer)``. This new function was called ``calc_score(guess, answer)``:

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

and tested to ensure it produced the anticipated results:

    assert calc_score(-5, 8) == 0, "Guess is below 0, score is 0"
    assert calc_score(20, 8) == 0, "Guess 5 or more greater than answer, score is 0"
    assert calc_score(6, 18) == 0, "Guess 5 or more fewer than answer, score is 0"
    assert calc_score(8, 8) == 10, "Guess is equal to answer, score is 10"
    assert calc_score(15, 18) == 5, "Guess is within -5 point range of answer, score is 5"
    assert calc_score(22, 18) == 5, "Guess is within +5 point range of answer, score is 5


#### 5. Move to next piece of required functionality
These steps were repeated until all tests were passing and the code was refactored.

For example, in the test suite, the ``calc_score(guess, answer)`` function was further refactored with the ``get_challenge(index)`` and ``setup_context(username)``functions to create the ``challenge_run(username, guess)`` function.

The testing suite can be found [here](testing.py) 


### Manual tests
The following aspects of the code were tested manually:
* **data processed through HTML forms**. Flash messages were used to test that the player's guesses were processed correctly. For example:
    * username was entered on index.html
    * the 'welcome' card on intro.html was viewed to ensure that the username was stored in the context

* **routes** were tested through live testing of the challenges. For example:
    * there is only one 'path' through the challenge (other than the 'Start Again' button on the navbar) and this was tested numerous times by completing the challenge

* the **persistence of the context data** was tested by checking that the information was accurantely written to the results.json file when the challenge had been completed
    * player score, which is stored in the context, was tested by doing multiple 'walk-throughs' of the challenge, providing different answers for each challenge
    * the score was tallied manually and compared with the results produced at the end of the challenge
    
* **.json data rendering onto the templates** was tested by manually matching the results.json data with the rendered templates
    * the game follows a strict chronological sequence. The challenge progression outlined in the challenge.json file was matched to the template progression (including titles, numbers, etc) and tested to ensure they matched
    
* **simultaneous players and separate contexts** were tested by checking if both usernames & results displayed on the results table at the end of the challenge

* **JQuery events** all take place on the Challenge pages. These were tested by executing the event, refreshing the page and testing again 

* As the live code involved passing the original context data through hidden names in the HTML form, the second attempt was not simulated in the tests or refactored with the ``challenge_run(username, guess)``. Instead the 'loop' to the second guess or progression to next question was tested manually by providing a range of responses to the question to see what response the code would produce:
    * a correct answer should have progressed to the following challenge (unless it was the last challenge)
    * an incorrect answer should have repeated the challenge one more time, and then progressed to the next challenge

* **Broswer compatibility**. The above features were tested in each of the following browsers:
  - Google Chrome
  - Opera
  - Microsoft Edge
  - Mozilla Firefox
  - Safari

An **unresolved bug** was found when testing the application on Microsoft Edge. The JQuery fadeIn() method, unlike each of the other browsers, was 'jumpy'  and not smooth. After looking for different fixes, I decided to leave it as it was as it was not too distracting, and the Market Development Association will have relative control over what browser the application is used on at community events.

