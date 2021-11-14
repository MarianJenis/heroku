from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/<name>")
def hello_there(name: str = "Robo"):
    return f"<p>Nazdar, {name}!</p>", 200

@app.route("/ksi/<challenge>")
def challange():
    return f"<p>Challange passed</p>, 200

if __name__ == '__main__':
    app.run(threaded=True, port=5000)
