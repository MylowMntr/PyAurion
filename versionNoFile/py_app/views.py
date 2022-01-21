from datetime import datetime
import locale
locale.setlocale(locale.LC_ALL, 'fr_FR.utf8')
from flask import Flask, render_template, request, session
from . import app
from .api import getnotes, getplanning, CalcMoyenne
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
    if ("email" in session):
        return render_template(
            "notes.html",
            notes=getnotes.main(session["email"],session["password"]),
        )
    else:
        return render_template(
        "login.html",
    )
        
@app.route("/moyennes/")
def moyennes():
    if ("email" in session):
        return render_template(
            "moyennes.html",
            moyennes = CalcMoyenne.main(session["email"],session["password"])
        )
    else:
        return render_template(
        "login.html",
    )
        
@app.route("/plan/")
def plan():
    if ("email" in session):
        return render_template(
            "plan.html",
        )
    else:
        return render_template(
        "login.html",
    )

@app.route('/data')
def return_data():
    return getplanning.main(0,session["email"],session["password"])


@app.route('/login', methods=['GET', 'POST'])
def form_example():
    # handle the POST request
    if request.method == 'POST':
        session["email"] = request.form.get('email')
        session["password"] = request.form.get('password')
        return render_template(
            "home.html"
        )
            
    # otherwise handle the GET request
    return render_template(
        "login.html",
    )
    
