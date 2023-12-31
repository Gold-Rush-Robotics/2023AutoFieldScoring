from flask import Flask
from flask import render_template
import time
from field import Field

app = Flask(__name__)

start_time = 0
field = Field()

@app.route("/")
def main_screen(points=None):
    if points:
        return render_template('mainscreen.jinja', points=points)
    return render_template('mainscreen.jinja')

@app.route("/match")
def during_match():
    global start_time
    return render_template('match.jinja', start_time=start_time)
    

def post_match():
    global start_time
    pass

@app.route("/get_score")
def get_score():
    global field
    return {"score":field.score}

@app.route("/start")
def start():
    global start_time
    start_time = time.time_ns()
    return during_match()