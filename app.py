import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", page_title="Welcome")

@app.route('/challenge')
def challenge():
    return render_template("challenge.html", page_title="Take the timeBank Challenge")
    
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