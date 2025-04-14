from flask import Flask, redirect, url_for
from flask import render_template, request, session


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/admin")
def admin():
    return redirect(url_for("home"))


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        session["user"] = user
        return redirect(url_for("user"))
    else:
        return render_template("login.html")


@app.route("/profile")
def profile():
    return render_template("profile.html")


@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"


if __name__ == "__main__":
    app.run(debug=True)
