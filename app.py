import os
import json
from flask import Flask, render_template, request, flash, redirect, url_for, jsonify




app = Flask(__name__)
app.secret_key = "some_secret"

"""
Create list to user store user details and scores as game progresses

"""

user_dict = {}

def store_user_info(username, email, guess=0):
    user_dict = {"username": username, "email": email, "score": [guess]}
    print(user_dict)
    
    #Write user details to user_info.txt file
    # with open("data/user_info.txt", "a") as user_details:
    #     user_details.writelines("{0}\n{1}\n{2}\n".format(
    #         user_dict["username"],
    #         user_dict["email"],
    #         user_dict["score"])) 
        
        #json.dumps dict 
    # json_user = json.dumps(user_dict)
    # f = open("data/user_info.json", "a")
    # f.write(json_user)
    # f.close
        



"""
List to handle scores - CURRENTLY ADDING ALL SCORES TOGETHER - NOT BY USERNAME
"""
score = []
total_score = sum(score)


"""
Scoring Function
"""


# Testing with score variable
def limit_number_questions(guess, answer):
    if guess <= 0:
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
    
    print(points)
    score.append(points)
        


"""
Challenge Q&A function
"""
def challenge_q_a(num):
    if request.method == "POST":
        print(request.form)
        with open("data/challenge.json", "r") as json_data:
            data = json.load(json_data)
                
            """Call Scoring Function"""
            print(data[num]["skill_answer"])
            limit_number_questions(int(request.form["guess"]), int(data[num]["skill_answer"]))
                
            print(score)
            print(sum(score))
                #"""Display guess to user - LOADS ON REFRESH - NEED AJAX - JSONIFY?"""
                # flash("You guessed {}!".format(
                # request.form["guess"]
                # ))
                
    
"""
Sign-in Page
"""

@app.route('/', methods=["GET", "POST"])
def index():
    """
    Sign in & add details to user_info list
    """
    if request.method == "POST":
        store_user_info(request.form["username"], request.form["email"])
        return redirect('/challenge_1')
    return render_template("index.html")


"""
Challenge Pages
"""

@app.route('/challenge_1', methods=["GET", "POST"])
def challenge_1():
    challenge_q_a(0)
    
    """
    Reading data from challenge.json into challenge.html
    """
    data = []
    with open("data/challenge.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("challenge_1.html", challenge_data = data)



@app.route('/challenge_2', methods=["GET", "POST"])
def challenge_2():
    challenge_q_a(1)

    data = []
    with open("data/challenge.json", "r") as json_data:
        data = json.load(json_data)
    
    return render_template("challenge_2.html", challenge_data = data)
    


@app.route('/challenge_3', methods=["GET", "POST"])
def challenge_3():
    challenge_q_a(2)

    data = []
    with open("data/challenge.json", "r") as json_data:
        data = json.load(json_data)
    
    return render_template("challenge_3.html", challenge_data = data)

@app.route('/challenge_4', methods=["GET", "POST"])
def challenge_4():
    challenge_q_a(3)

    data = []
    with open("data/challenge.json", "r") as json_data:
        data = json.load(json_data)
    
    return render_template("challenge_4.html", challenge_data = data)

@app.route('/challenge_5', methods=["GET", "POST"])
def challenge_5():
    challenge_q_a(4)

    data = []
    with open("data/challenge.json", "r") as json_data:
        data = json.load(json_data)
    
    return render_template("challenge_5.html", challenge_data = data)

@app.route('/challenge_6', methods=["GET", "POST"])
def challenge_6():
    challenge_q_a(5)

    data = []
    with open("data/challenge.json", "r") as json_data:
        data = json.load(json_data)
    
    return render_template("challenge_6.html", challenge_data = data)

@app.route('/challenge_7', methods=["GET", "POST"])
def challenge_7():
    challenge_q_a(6)

    data = []
    with open("data/challenge.json", "r") as json_data:
        data = json.load(json_data)
    
    return render_template("challenge_7.html", challenge_data = data)

@app.route('/challenge_8', methods=["GET", "POST"])
def challenge_8():
    challenge_q_a(7)

    data = []
    with open("data/challenge.json", "r") as json_data:
        data = json.load(json_data)
    
    return render_template("challenge_8.html", challenge_data = data)
"""
Table Page
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
        
        
