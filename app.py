import os
import json
from flask import Flask, render_template, request, flash, redirect, url_for, jsonify, session
from operator import itemgetter, attrgetter
from scoring import user_list, score, calc_score, challenge_q_a, display_score
# import scoring (access via 'scoring.user_list')

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
Set default values for starting game. These will be used to initialise the challenge
for the player at Challenge 1
"""

def setup_context(username):
    score = 0
    attempt = 1
    challenge = get_challenge(0)
    context = {
        'challenge_id': 0, 
        'title': challenge['title'],
        'need': challenge['need_amount'],
        'statement': challenge['need_statement'],
        'challenge': challenge['skill_question'],
        'answer': challenge['skill_answer'],
        'username': username,
        'current_score': score,
        'attempt': attempt
    }
    return context


"""
Start Page - Player selects a username which is passed through to the intro function
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
Challenge Pages
"""

"""Challenge Test Page"""
@app.route('/challenge/<username>', methods=["GET", "POST"])
def challenge(username):
    if request.method == 'POST':
        
        form = request.form
        
        """ 
        Form on intro.html passed default context for the first question. If not
        Challenge 1, the function will take the values from the player's submitted form
        (including hidden inputs)
        """
        
        if form.get('first-challenge') == 'true':
            context = setup_context(username)
            return render_template('challenge.html', context=context)
        
        else:
            attempt = int(form.get('attempt'))
            challenge_id = int(form.get('challenge_id'))
            score = int(form.get('current_score'))
            challenge = get_challenge(challenge_id)
            
            guess = int(form.get('guess'))
            answer = int(challenge['skill_answer'])
            correct = guess == answer
            
            while challenge_id < 8:
                if correct:
                    challenge_id += 1
                    score += 10
                    attempt = 1 # set attempt at 1 for next challenge
                    next_challenge = get_challenge(challenge_id)
                    flash('Spot on! Well done.', 'success')
                
                else:
                    if attempt >= 2:
                        challenge_id += 1
                        attempt = 1
                        
                        """
                        Give 5 points to guesses (on the second attempt) that are
                        within a -10 and +10 range of the answer
                        """
                        
                        if (guess > answer) and (guess <= answer + 5) or (guess < answer) and (guess >= answer - 5):
                            score += 5
                            flash('"{}" is close enough! You get 5 points for that one!'.format(answer), 'error')
                            next_challenge = get_challenge(challenge_id)
                        
                        else:    
                            next_challenge = get_challenge(challenge_id)
                            flash('"{}" was your last guess. The answer was "{}". Try another one!'.format(guess, answer), 'error')                        
                    
                    else:
                        attempt += 1
                        next_challenge = get_challenge(challenge_id)
                        if (guess > answer) and (guess < answer + 5) or (guess < answer) and (guess > answer - 5):
                            flash('"{}" is close... Try one more time'.format(guess), 'error')
                        
                        else:
                            flash('"{}" is\'t right. Have another go!'.format(guess), 'error')
               
                """
                Template is now returned with the updated context unless player has
                completed the final challenge, in which case game will move through to 
                final score announcement
                """
                
                if next_challenge is not None:
                    context = {
                        'challenge_id': challenge_id,
                        'title': next_challenge['title'],
                        'challenge': next_challenge['skill_question'],
                        'need': next_challenge['need_amount'],
                        'statement': next_challenge['need_statement'],
                        'answer': next_challenge['skill_answer'],
                        'username': username,
                        'current_score': score,
                        'attempt': attempt
                    }
                    return render_template('challenge.html', context=context)
                else:
                    return "done yet?"
                    
            # CHECK CODE HERE - PUT END RESULT IN END_SCORE FUNCTION Return final score and add the player to the leaderboard
            return render_template("registration.html", score_sub="See how everyone else did & find out more...")    
    return redirect('/')



# OLD FUNCTIONS - KEEP FOR REF
# """Challenge Page 8"""
# @app.route('/challenge_8', methods=["GET", "POST"])
# def challenge_8():

#     challenge_q_a(7)
#     display_score()
#     with open("data/challenge.json", "r") as json_data:
#         data = json.load(json_data)
#     return render_template("challenge_8.html", challenge_data = data)
    

"""
Result & Registration Page
"""
@app.route('/registration', methods=["GET", "POST"])
def registration():

    # Display total score
    flash("You scored {} points!".format(int(sum(score))))

    
    # Sign in & append details to user_info list
    if request.method == "POST":
        name = session["username"]
        email = request.form["email"]
        message = request.form["message"]
        final_score = int(sum(score))
        
        user_list.append({
        "name": name,
        "email": email,
        "message": message,
        "score": final_score,
        })
        
        
        with open('data/user_info.txt', 'w') as outfile:  
            json.dump(user_list, outfile)
            
            return redirect('/message_board')
    
    return render_template("registration.html", score_sub="See how everyone else did & find out more...")
    
    
"""
Message Board Page
"""
@app.route('/message_board', methods=["GET", "POST"])
def message_board():
    
    # remove the username from the session
    session.pop('username', None)
    
    # Display Score Table in descending order
    with open("data/user_info.txt", "r") as json_data:
        data = json.load(json_data)
        
        newlist = sorted(data, key=itemgetter('score'), reverse=True)
    
    # Redirect to Information Page
    if request.method == "POST":
        return redirect('/information')
    
    return render_template("message_board.html", page_title="How did you get on?", score_table = newlist)


"""
More Information Page
"""
@app.route('/information')
def information():
    return render_template("information.html", page_title="Find out more...")


if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
        
        
