import os
import json
from flask import Flask, render_template, request, flash, redirect, url_for, jsonify, session
from operator import itemgetter, attrgetter
from scoring import user_list, score, calc_score, challenge_q_a, display_score
# import scoring (access via 'scoring.user_list')

app = Flask(__name__)
app.secret_key = "some_secret"


"""
Start Page
"""
@app.route('/', methods=["GET", "POST"])
def index():
    
    # Trigger start of new game
    if request.method == "POST":
        
        # Register new player and store their information and score in 
        # Flask Session
        session['username'] = request.form['username']
        
        # Clear scoring list for new player
        score[:]=[]
        return redirect('/challenge_1')
    return render_template("index.html")


"""
Challenge Pages
"""

"""Challenge Page 1"""
@app.route('/challenge_1', methods=["GET", "POST"])
def challenge_1():
    
    # Q & A and Scoring Function (repeated each Challenge)
    challenge_q_a(0)
    
    # Read challenge.js data for rendering (repeated each Challenge Page)
    with open("data/challenge.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("challenge_1.html", challenge_data = data)

# """Challenge Page 2"""
# @app.route('/challenge_2', methods=["GET", "POST"])
# def challenge_2():
#     challenge_q_a(1)
#     display_score()
#     with open("data/challenge.json", "r") as json_data:
#         data = json.load(json_data)
#     return render_template("challenge_2.html", challenge_data = data)
    
# """Challenge Page 3"""
# @app.route('/challenge_3', methods=["GET", "POST"])
# def challenge_3():
#     challenge_q_a(2)
#     display_score()   
#     with open("data/challenge.json", "r") as json_data:
#         data = json.load(json_data)
#     return render_template("challenge_3.html", challenge_data = data)

# """Challenge Page 4"""
# @app.route('/challenge_4', methods=["GET", "POST"])
# def challenge_4():
#     challenge_q_a(3)
#     display_score()
#     with open("data/challenge.json", "r") as json_data:
#         data = json.load(json_data)
#     return render_template("challenge_4.html", challenge_data = data)

# """Challenge Page 5"""
# @app.route('/challenge_5', methods=["GET", "POST"])
# def challenge_5():
#     challenge_q_a(4)
#     display_score()
#     with open("data/challenge.json", "r") as json_data:
#         data = json.load(json_data)
#     return render_template("challenge_5.html", challenge_data = data)

# """Challenge Page 6"""
# @app.route('/challenge_6', methods=["GET", "POST"])
# def challenge_6():
#     challenge_q_a(5)
#     display_score()
#     with open("data/challenge.json", "r") as json_data:
#         data = json.load(json_data)
#     return render_template("challenge_6.html", challenge_data = data)

# """Challenge Page 7"""
# @app.route('/challenge_7', methods=["GET", "POST"])
# def challenge_7():
#     challenge_q_a(6)
#     display_score()
#     with open("data/challenge.json", "r") as json_data:
#         data = json.load(json_data)
#     return render_template("challenge_7.html", challenge_data = data)

"""Challenge Page 8"""
@app.route('/challenge_8', methods=["GET", "POST"])
def challenge_8():
    challenge_q_a(7)
    display_score()
    with open("data/challenge.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("challenge_8.html", challenge_data = data)
    

"""
Result & Registration Page
"""
@app.route('/registration', methods=["GET", "POST"])
def registration():
    
    # Display total score
    flash("You scored {} points!".format(int(sum(score))))

    
    # Sign in & append details to user_info list
    # if request.method == "POST":
    #     name = request.form["username"]
    #     email = request.form["email"]
    #     message = request.form["message"]
    #     final_score = int(sum(score))
        
    #     user_list.append({
    #     "name": name,
    #     "email": email,
    #     "message": message,
    #     "score": final_score,
    #     })
        
    with open('data/user_info.txt', 'w') as outfile:  
        json.dump(user_list, outfile)

    # remove the username from the session
    session.pop('username', None)
    # return redirect("/message_board") 
    return render_template("registration.html", score_sub="See how everyone else did & find out more...")
    
    
"""
Message Board Page
"""
@app.route('/message_board', methods=["GET", "POST"])
def message_board():
    
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
        
        
