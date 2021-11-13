from flask import Flask, render_template

app = Flask(__name__)

nordic_animals = ["los", "sob", "tučňák", "vlk", "lední medvěd"]


@app.route("/")
def index():
    return "<p>Ahoj robo</p>"
