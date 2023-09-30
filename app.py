from flask import Flask
from flask import render_template
from time import perf_time


app = Flask(__name__)

start_time = 0

@app.route("/")
def main_screen(points=None):
    if points:
        return render_template('mainscreen.jinja', points=points)
    return render_template('mainscreen.jinja')

@app.route("/match")
def during_match():
    global start_time
    pass

def post_match():
    global start_time
    pass

@app.route("/start")
def start():
    global start_time
    start_time = perf_counter()
    return during_match()