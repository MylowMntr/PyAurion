from datetime import datetime
import locale
locale.setlocale(locale.LC_ALL, 'fr_FR.utf8')
from flask import Flask, render_template, request, session, redirect, url_for
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
        
@app.route("/moyennes/<username>-<password>")
def moyennes(username,password):
    if (username != ""):
        return render_template(
            "moyennes.html",
            moyennes = CalcMoyenne.main(username=username,password=password)
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
def login():
    # handle the POST request
    if request.method == 'POST':
        username = request.form.get('email')
        password = request.form.get('password')
        return redirect(url_for('moyennes', username = username, password=password))
        
            
    # otherwise handle the GET request
    return render_template(
        "login.html",
    )
    
