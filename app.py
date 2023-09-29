from flask import Flask

app = Flask(__name__)

POINTS = 0
TIME = 0

@app.route("/")
def main_screen():
    pass

@app.route("/start")
def start():

    return main_screen()