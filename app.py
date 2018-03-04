import os
import json
from flask import Flask, render_template, request, flash, redirect, url_for


app = Flask(__name__)
app.secret_key = "some_secret"

"""
Scoring Function
"""
def ask_questions(guess, answer):
    # data = []
    with open("data/challenge.json", "r") as json_data:
        data = json.load(json_data)
    guess = request.form["guess"]
    answer = data[0]["skill_answer"]
    if guess is str(guess):
        return 0
    elif guess == answer:
        return 10
    elif ((guess > answer) and (guess < (answer + 10))) or ((guess < answer) and (guess > (answer - 10))):
        return 5
    else:
        return 0

"""
Add a function to get all of the scores and add them
"""


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        flash("Welcome {}!".format(
        request.form["username"]
        ))
        with open("data/user_info.txt", "a") as user_details:
            user_details.write(request.form["username"] + "\n")
            user_details.write(request.form["email"]  + "\n")
        
          
    return render_template("index.html")

@app.route('/challenge', methods=["GET", "POST"])
def challenge():
    if request.method == "POST":
        
        """
        Storing Guesses in user_info.json file
        """
        with open("data/user_info.json", "a") as user_details:
            json.dump(request.form, user_details)
            print(request.form["guess"])
    
    """
    Reading data from challenge.json into challenge.html
    """
    data = []
    with open("data/challenge.json", "r") as json_data:
        data = json.load(json_data)
    
    """
    Use a return redirect to move to the next question
    """
    
    return render_template("challenge_1.html", running_score="Your Score: 15", challenge_data = data)

"""
Do you iterate through html within the same route? _1, _2, _3, etc
"""



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