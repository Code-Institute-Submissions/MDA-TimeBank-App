import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/challenge')
def challenge():
    return render_template("challenge.html")
    
@app.route('/information')
def information():
    return render_template("information.html")
    
@app.route('/message_board')
def message_board():
    return render_template("message_board.html")
    
if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)