# functions assoc with scoring
import os
import json
from flask import Flask, request, flash



"""
List to store user details
"""
user_list = []
   

"""
List to handle scores as game progresses
"""
score = []


"""
Scoring Function
"""
# Testing with score variable
def calc_score(guess, answer):
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
    score.append(points)

    
"""
Challenge Q&A function
"""
def challenge_q_a(num):
    if request.method == "POST":
        with open("data/challenge.json", "r") as json_data:
            data = json.load(json_data)
                
            # Call Scoring Function
            calc_score(int(request.form["guess"]), int(data[num]["skill_answer"]))


"""
Display Score Tally
"""
def display_score(): 
    flash('Your Score = {}'.format(int(sum(score))))
    

