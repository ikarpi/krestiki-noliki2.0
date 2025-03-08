from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def first():
    return render_template("Bootstrap.html")

@app.route("/bombardir/")
def players():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()


