from datetime import datetime
import locale
locale.setlocale(locale.LC_ALL, 'fr_FR.utf8')
from flask import Flask, render_template
from . import app
from .api import getnotes, getplanning

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/lay/")
def shesh():
    return render_template("layout.html")

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now(),
    )



@app.route("/notes/")
def notes():
        return render_template(
        "notes.html",
        notes=getnotes.main(),
    )

@app.route("/plan/")
def plan():
        return render_template(
        "plan.html",
        plan=getplanning.main(),
        datetime=datetime,
    )
        
        
@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")
