import os
import json
from flask import Flask, render_template, request, flash, redirect, url_for, jsonify, session
from operator import itemgetter, attrgetter
import types
from types import NoneType


app = Flask(__name__)
app.secret_key = "some_secret"


"""
Get challenge information from json file to loop through the questions and answers
"""

def get_challenge(index):
    with open("data/challenge.json", "r") as json_data:
        data = json.load(json_data)
        return data[index] if index <= 7 else None # Catches IndexError if there are no more challenges


"""
Add and sort players to the results table
"""

results_list = []

def results_table(username, result):
    results_list.append({
        'name': username,
        'score': result,
    })
    
    with open('data/results.json', 'w') as outfile:
        json.dump(results_list, outfile)


"""
Set default values for starting game. These will be used to initialise the challenge
for the player at Challenge 1
"""

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
        'current_score': score,
        'attempt': attempt,
        'image': challenge['image'],
    }
    return context


"""
Start Page - Player selects a username which is passed through to the intro 
function
"""

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template("index.html" )

    
"""
Introduction Page
"""

@app.route('/intro/', methods=["GET", "POST"])
def intro():
    if request.method == 'POST':
        form = request.form
        user = form['username']
        return render_template("intro.html", username=user)
    
    return redirect('/')


"""
Challenge loop
"""

@app.route('/challenge/<username>', methods=["GET", "POST"])
def challenge(username):
    
    
    if request.method == 'POST':
        
        form = request.form
        
        """ 
        The form on intro.html passes the data for the context for the Challenge 1 
        - keeping track of player activity and the progress of the challenges
        """
        
        if form.get('first-challenge') == 'true':
            context = setup_context(username)
            return render_template('challenge.html', context=context)
        
        else:
            attempt = int(form.get('attempt'))
            challenge_id = int(form.get('challenge_id'))
            score = int(form.get('current_score'))
            challenge = get_challenge(challenge_id)
            challenge_plus = get_challenge(challenge_id + 1)
            
            guess = int(form.get('guess'))
            answer = int(challenge['skill_answer'])
            correct = guess == answer
            
            while challenge_id <= 7:  # executes while there is another challenge
                
                if correct: # catches if the guess is correct on first or second attempt
                    challenge_id += 1 # if so, moves to next challenge_id
                    score += 10 # gives 10 points for correct guess
                    attempt = 1 # set attempt at 1 for next challenge
                    next_challenge = get_challenge(challenge_id) # uses challenge_id as param to get next challenge
                    flash('"{}" was correct - 10 points!'.format(guess))
                
                    if challenge_id < 7: # stop message from flahsing if on last challenge
                        flash('Try the next challenge about {}'.format(challenge_plus['title']))
                
                else:
                    if attempt >= 2: # checks if there have been 2 or more attempts
                        challenge_id += 1 # moves to next challenge_id if true
                        attempt = 1 # sets 1st attempt again
                        
                        """
                        Give 5 points to guesses (on the second attempt) that are
                        within a -5 and +5 range of the answer
                        """
                        
                        if (guess > answer) and (guess <= answer + 5) or (guess < answer) and (guess >= answer - 5):
                            score += 5 # if guess is not correct but is +/-5, give 5 points
                            flash('The answer was "{}", but "{}" is close enough - 5 points!'.format(answer, guess))
                            next_challenge = get_challenge(challenge_id) # uses challenge_id as param to get next challenge
                            
                            if challenge_id < 7: # stop message from flahsing if on last challenge
                                flash('Try the next challenge about {}'.format(challenge_plus['title']))
                        
                        else: # if guess is not correct or within +/-5 range of answer     
                            next_challenge = get_challenge(challenge_id)  # uses challenge_id as param to get next challenge
                            flash('You guessed "{}". The answer was "{}".'.format(guess, answer))
                            
                            if challenge_id < 7: # stop message from flahsing if on last challenge
                                flash('Try the next challenge about {}'.format(challenge_plus['title']))
                    else: # if there has only been one attempt
                        attempt += 1 # move to second attempt
                        next_challenge = get_challenge(challenge_id) # use same challenge_id param
                        
                        if (guess > answer) and (guess < answer + 5) or (guess < answer) and (guess > answer - 5):
                            # if guess is not correct but is +/-5, notify player that guess is close to answer
                            flash('{} is close... Try again'.format(guess))
                        else:
                            flash('{} is not right. Try again!'.format(guess))
               
                """
                Template is now returned with the updated context unless player has
                completed the final challenge, in which case game will move through to 
                results table
                """
                
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
                    return render_template('challenge.html', context=context)

            results_table(username, score) # call function to store results list to results.json

            return redirect("/results_table")    
    
    return redirect('/')


"""
Results and information page
"""

@app.route('/results_table', methods=["GET", "POST"])
def results_board():
     
    with open("data/results.json", "r") as json_data:
        data = json.load(json_data)
        newlist = sorted(data, key=itemgetter('score'), reverse=True) # Display results table from highest score down
    
    return render_template("results_table.html", page_title="Timebanking", score_table = newlist)



if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
        
        




