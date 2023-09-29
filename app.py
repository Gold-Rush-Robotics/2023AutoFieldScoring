from flask import Flask

app = Flask(__name__)

POINTS = 0
TIME = 0

@app.route("/")
def main_screen():
    return f"""
<div style="text-align:center">
    <h1> FIELD STATUS</h1>
    <h2> Points: {POINTS} </h2>
    <h3> Time remaining: {TIME} </h3>
    <form action="/start">
        <input type="submit"> Start Match
    </fomr>
    
</div>
"""

@app.route("/start")
def start():

    return main_screen()