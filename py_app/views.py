from datetime import datetime
from dateutil.relativedelta import relativedelta
import locale
locale.setlocale(locale.LC_ALL, 'fr_FR.utf-8')
from flask import Flask, render_template, request, session
from . import app
from .api import getnotes, getplanning, CalcMoyenne,CalcMoyenneV2, validelogs, parse
import json
from pathlib import Path
import urllib.parse

@app.route("/", methods=['GET', 'POST'])
def home():
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
        return render_template(
            "plan.html",
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
    return getplanning.main(start,end,session["email"],session["password"])


@app.route('/ics', methods=['GET', 'POST'])
def return_cal():
    # Exporte les 7 prochains mois 
    ajd=datetime.now()
    start = datetime.strftime(ajd, '%Y-%m')
    start = start+"-01"

    end = (ajd + relativedelta(months = 7))
    end=datetime.strftime(end, '%Y-%m')
    end=end+"-28"

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
        
        return render_template(
            "home.html"
        )
            
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
        
        return render_template(
            "ome.html"
        )
            
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