import os
import json
from flask import Flask, render_template, request, flash, redirect, url_for


app = Flask(__name__)
app.secret_key = "some_secret"


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        flash("Welcome {}!".format(
        request.form["username"]
        ))
        with open("data/user_info.txt", "a") as user_details:
            user_details.write(request.form["username"] + "\n")
            user_details.write(request.form["email"]  + "\n")
        print request.form["username"]
    return render_template("index.html")

@app.route('/challenge')
def challenge():
    data = []
    with open("data/challenge.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("challenge.html", running_score="Your Score: 15", challenge_data = data)
    
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