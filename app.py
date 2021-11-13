from flask import Flask, render_template

app = Flask(__name__)

nordic_animals = ["los", "sob", "tučňák", "vlk", "lední medvěd"]


@app.route("/")
def index():
    return render_template("index.html", age=3)


@app.route("/cool_animals_list")
def cool_animals_list():
    return render_template("cool_animals.html", animals=nordic_animals)


@app.route("/memes")
def memes():
    return render_template("memes.html")

if __name__ == '__main__':
    app.run(threaded=True, port=5000)
