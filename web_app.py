"""
This file is my Flask application. It is still in development.

Current as of 4-23-24
"""

from flask import Flask, render_template, url_for, request, redirect, flash

app = Flask(__name__)

messages = [{"title": "Message one", "content": "Message one content"},
            {"title": "Message two", "content": "Message two content"},
            {"title": "Message three", "content": "Message three content"},
            ]


@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/test")
def test():
    return render_template("test.html")


@app.route("/contact")
def contact():
    return render_template("test.html", messages=messages)


def post(self):
    pass


if __name__ == "__main__":
    app.run(debug=True)
