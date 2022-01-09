from datetime import datetime
import locale
locale.setlocale(locale.LC_ALL, 'fr_FR.utf8')
from flask import Flask, render_template, request
from . import app
from .api import getnotes, getplanning
import json
from pathlib import Path

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/lay/")
def shesh():
    return render_template("layout.html")


@app.route("/notes/")
def notes():
    my_file = Path("py_app/static/user.json")
    if my_file.is_file():
        return render_template(
            "notes.html",
            notes=getnotes.main(),
        )
    else:
        return render_template(
        "login.html",
    )
    
@app.route("/plan/")
def plan():
    my_file = Path("py_app/static/user.json")
    if my_file.is_file():
        plan=getplanning.main(1)
        return render_template(
            "plan.html",
        )
    else:
        return render_template(
        "login.html",
    )

@app.route('/data')
def return_data():
    return app.send_static_file("data.json")


@app.route('/login', methods=['GET', 'POST'])
def form_example():
    # handle the POST request
    if request.method == 'POST':
        user = {"email" : request.form.get('email'),"password" : request.form.get('password')}
        with open('py_app/static/user.json', 'w') as f:
            json.dump(user, f)
            
    # otherwise handle the GET request
    return render_template(
        "login.html",
    )