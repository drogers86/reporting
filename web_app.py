"""
This file is my Flask application. It is still in development.

Current as of 5-6-24
"""

from flask import Flask, render_template, url_for, request, redirect, flash
from funcs import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'


@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/programs")
def programs():
    return render_template("programs.html")


@app.route("/sh_hourly")
def sh_hourly():
    # form = CourseForm()
    # course_id = request.form.getlist('CID')
    # reports = login(course_id)
    # make_it_rain(course_id, master_report, reports)
    return render_template("sh_hourly.html")


@app.route("/sh_mgr")
def sh_mgr():
    course_id = request.form.getlist('CID')
    reports = login(course_id)
    make_it_rain(course_id, master_report, reports)
    return render_template("sh_hourly.html", course_id=course_id)


@app.route("/food_safety")
def food_safety():
    course_id = ['653818']
    reports = login(course_id)
    make_it_rain(course_id, master_report, reports)
    return render_template("courses.html", course_id=course_id)


@app.route("/cc_safety")
def cc_safety():
    course_id = ['428369']
    reports = login(course_id)
    make_it_rain(course_id, master_report, reports)
    return render_template("courses.html", course_id=course_id)


@app.route("/alcohol")
def alcohol():
    course_id = ['597103']
    reports = login(course_id)
    make_it_rain(course_id, master_report, reports)
    return render_template("courses.html", course_id=course_id)


@app.route("/menu_update")
def menu_update():
    course_id = ['7437580', '7437443']
    reports = login(course_id)
    make_it_rain(course_id, master_report, reports)
    return render_template("courses.html", course_id=course_id)


@app.route('/courses', methods=('GET', 'POST'))
def courses():
    course_id = request.form.getlist('CID')
    reports = login(course_id)
    make_it_rain(course_id, master_report, reports)

    return render_template('courses.html', course_id=course_id)


if __name__ == "__main__":
    app.run(debug=True)
