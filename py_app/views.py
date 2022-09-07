from datetime import datetime
import locale
locale.setlocale(locale.LC_ALL, 'fr_FR.utf-8')
from flask import Flask, render_template, request, session, make_response
from . import app
from .api import getnotes, getplanning, validelogs, getabs
import json
from pathlib import Path
import urllib.parse

@app.route("/", methods=['GET', 'POST'])
def home():
    if 'email' in request.cookies:
        session["email"] = request.cookies.get('email')
        session["password"] = request.cookies.get('password')
        return render_template(
            "ome.html"
        )
    return render_template("log.html")


@app.route("/notee/")
def notee():
    if ("email" in session):
        return render_template(
            "notee.html",
            notes=getnotes.main(session["email"],session["password"]),
        )
    else:
        return render_template(
        "log.html",
    )
@app.route("/abs/")
def abs():
    if ("email" in session):
        return render_template(
            "abs.html",
            abs=getabs.main(session["email"],session["password"]),
        )
    else:
        return render_template(
        "log.html",
    )
        
@app.route("/plann/")
def plann():
    if ("email" in session):
        session["upPlan"] = 0
        return render_template(
            "plann.html",
        )
    else:
        return render_template(
        "log.html",
    )

@app.route("/ome/")
def ome():
    if ("email" in session):
        session["upPlan"] = 0
        return render_template(
            "ome.html",
        )
    else:
        return render_template(
        "log.html",
    )
@app.route("/links/")
def links():
    if ("email" in session):
        session["upPlan"] = 0
        return render_template(
            "links.html",
        )
    else:
        return render_template(
        "log.html",
    )
        
@app.route("/custom/")
def custom():
    if ("email" in session):
        session["upPlan"] = 0
        return render_template(
            "custom.html",
        )
    else:
        return render_template(
        "log.html",
    )
     
        
@app.route('/data', methods=['GET', 'POST'])
def return_data():
    start = request.args.get('start')
    end = request.args.get('end')
    # print(start,end)
    
    if ("data" not in session or session["data"] == "[]" or session["upPlan"] == 0):
        session["data"] = getplanning.main(start,end,session["email"],session["password"])
        session["upPlan"] = 1
        
    # print(session["data"])
    return session["data"]


@app.route('/log/', methods=['GET', 'POST'])
def log():
    # handle the POST request
    if request.method == 'POST':
        session["email"] = request.form.get('email')
        session["email"] = urllib.parse.quote(session["email"])
        
        session["password"] = request.form.get('password')
        session["password"] = urllib.parse.quote(session["password"])
        
        # session["stocknote"] = request.form.getlist('note')
        # if (session["stocknote"] != []):
        #     session["stocknote"] = True
        # else:
        #     session["stocknote"] = False
        # print(session["stocknote"])
        if (validelogs.main(0, session["email"], session["password"]) != True):
            error = "Identifiants invalides ! Réessaye"
            return render_template(
                "log.html",error=error
            )
        
        
        resp = make_response(render_template("ome.html"))
        resp.set_cookie('email', session["email"], max_age=378432000)
        resp.set_cookie('password', session["password"], max_age=378432000)
        return resp
                
    # otherwise handle the GET request
    return render_template(
        "log.html",
    )
    