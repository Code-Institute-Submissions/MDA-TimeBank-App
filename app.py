import os
import json
from flask import Flask, render_template, request, flash, redirect, url_for



app = Flask(__name__)
app.secret_key = "some_secret"

"""
Create list to user store user detail and scores as game progresses

"""
user_info = []

"""
Handle list appendages
"""
def list_append(type):
    user_info.append(type)
    

"""
Scoring Function
"""
def challenge_scoring(guess, answer):
    score = 0
    if guess is str(guess):
        score = score + 0
    elif guess == answer:
        score = score + 10
    elif ((guess > answer) and (guess < (answer + 10))) or ((guess < answer) and (guess > (answer - 10))):
        score = score + 5
    else:
        score = score + 0
    list_append(score)
    return score
    
"""
Challenge Q&A function
"""
def challenge_q_a(num):
    if request.method == "POST":
            with open("data/challenge.json", "r") as json_data:
                data = json.load(json_data)
                
                """Call Scoring Function"""
                challenge_scoring(int(request.form["guess"]), int(data[num]["skill_answer"]))
                
                
                """Display guess to user"""
                flash("You guessed {}!".format(
                request.form["guess"]
                ))
                print(user_info)
            """Redirect to next page"""
            # return redirect('/challenge')






@app.route('/', methods=["GET", "POST"])
def index():
    """
    Sign in & add details to user_info list
    """
    if request.method == "POST":
        list_append(request.form["username"])
        list_append(request.form["email"])
        print(user_info)
        return redirect('/challenge_1')
    return render_template("index.html")



@app.route('/challenge_1', methods=["GET", "POST"])
def challenge_1():
    challenge_q_a(0)
    """
    Reading data from challenge.json into challenge.html
    """
    data = []
    with open("data/challenge.json", "r") as json_data:
        data = json.load(json_data)
    
    return render_template("challenge_1.html", user = user_info, challenge_data = data)


@app.route('/challenge_2', methods=["GET", "POST"])
def challenge_2():
    challenge_q_a(1)
    """
    Reading data from challenge.json into challenge.html
    """
    data = []
    with open("data/challenge.json", "r") as json_data:
        data = json.load(json_data)
    
    return render_template("challenge_2.html", user = user_info, challenge_data = data)





@app.route('/information')
def information():
    return render_template("information.html", page_title="Find out more...")

    
@app.route('/message_board')
def message_board():
    return render_template("message_board.html", page_title="What do you think? Leave a message")
    
if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
        
        
# """
# Final ScoreBoard
# """
# scoreboard = []

# def final_score(username, total_score):
#     scoreboard.append("{}: {}".format(username, total_score))
    

# """
# Show ScoreBoard
# """
# def show_scoreboard():
#     """Group messages & separate them by a `br` - need descending order"""
#     return "<br>".join(scoreboard)

# """
# Add a function to get all of the scores and add them
# """