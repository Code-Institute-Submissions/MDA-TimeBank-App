import os
import json
from flask import Flask, render_template, request, flash, redirect, url_for



app = Flask(__name__)
app.secret_key = "some_secret"


"""
Create list to user store scores as game progresses

"""
user_info = []


"""
Scoring Function - needs developed and tested
"""
def ask_questions(guess, answer):
    score = 0
    if guess is str(guess):
        score = score + 0
    elif guess == answer:
        score = score + 10
    elif ((guess > answer) and (guess < (answer + 10))) or ((guess < answer) and (guess > (answer - 10))):
        score = score + 5
    else:
        score = score + 0
    return score



"""
Add a function to get all of the scores and add them
"""


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_info.append(request.form["username"])
        user_info.append(request.form["email"])
        # with open("data/user_info.json", "w") as user_details:
        #     json.dump(request.form, user_details)
        return redirect('/challenge')
    return render_template("index.html")


@app.route('/challenge', methods=["GET", "POST"])
def challenge():
    print(user_info[0])
    if request.method == "POST":
        with open("data/challenge.json", "r") as json_data:
            data = json.load(json_data)
            """Call Scoring"""
            ask_questions(int(request.form["guess"]), int(data[0]["skill_answer"]))
            flash("You guessed {}!".format(
            request.form["guess"]
            ))
        """Redirect to next page"""
        # return redirect('/')
    """
    Reading data from challenge.json into challenge.html
    """
    data = []
    with open("data/challenge.json", "r") as json_data:
        data = json.load(json_data)
    
    return render_template("challenge_1.html", user = user_info, challenge_data = data)




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