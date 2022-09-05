from datetime import datetime
import locale
locale.setlocale(locale.LC_ALL, 'fr_FR.utf-8')
from flask import Flask, render_template, request, session, make_response
from . import app
from .api import getnotes, getplanning, CalcMoyenne,CalcMoyenneV2, validelogs, parse, getabs
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
@app.route("/notee/")
def notee():
    if ("email" in session):
        return render_template(
            "notee.html",
            notes=getnotes.main(session["email"],session["password"]),
        )
    else:
        return render_template(
        "login.html",
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
        "login.html",
    )
@app.route("/moyennes/")
def moyennes():
    if ("email" in session):
        result = getnotes.main(session["email"],session["password"])
        return render_template(
            "moyennes.html",
            moyennes = CalcMoyenne.main(result),  #,session["stocknote"]
            moyennes2 = CalcMoyenneV2.main(result)  #,session["stocknote"]
        )
    else:
        return render_template(
        "login.html",
    )
        
@app.route("/plan/")
def plan():
    if ("email" in session):
        session["upPlan"] = 0
        return render_template(
            "plan.html",
        )
    else:
        return render_template(
        "login.html",
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
        "login.html",
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
        "login.html",
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
        "login.html",
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


@app.route('/ics', methods=['GET', 'POST'])
def return_cal():
    # Exporte les 6 prochains mois 
    ajd=datetime.now()
    start = datetime.strftime(ajd, '%Y-%m')
    start = start+"-01"

    end = datetime.strptime(str(start),'%Y-%m-%d')
    end = int(end.timestamp())
    end += 6*30*24*60*60
    end = datetime.fromtimestamp(end)
    end = datetime.strftime(end, '%Y-%m-%d')

    #Semaine : 2022-03-21T13:30:00+0100
    #Mois : 2022-09-11
    cal=getplanning.main(start,end,session["email"],session["password"])
    # Retour à améliorer ...
    return parse.main(cal)




@app.route('/login', methods=['GET', 'POST'])
def login():
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
                "login.html",error=error
            )
        
        
        resp = make_response(render_template("home.html"))
        resp.set_cookie('email', session["email"])
        resp.set_cookie('password', session["password"])
        return resp
                
    # otherwise handle the GET request
    return render_template(
        "login.html",
    )
    

@app.route('/log', methods=['GET', 'POST'])
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
    

@app.route("/moy")
def moy():
    if ("email" in session):
        result = getnotes.main(session["email"],session["password"])
        return render_template(
            "moy.html",
            # moyennes = CalcMoyenne.main(result),  #,session["stocknote"]
            moyennes2 = CalcMoyenneV2.main(result)  #,session["stocknote"]
        )
    else:
        return render_template(
        "login.html",
    )