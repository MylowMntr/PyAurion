from datetime import datetime
import locale

locale.setlocale(locale.LC_ALL, "fr_FR.utf-8")
from flask import Flask, render_template, request, session, make_response
from . import app
from .api import getnotes, getallnotes, getplanning, validelogs, getabs, compress, uncompress, encrypt, deencrypt
import json
from pathlib import Path
import urllib.parse


@app.route("/", methods=["GET", "POST"])
def home():
    if "a" in request.cookies:
        session["a"] = deencrypt.main(request.cookies.get("a"))
        session["b"] = deencrypt.main(request.cookies.get("b"))
        return render_template("ome.html")
    return alerte()


@app.route("/notee/")
def notee():
    if "a" in session:
        return render_template(
            "notee.html",
            notes=getnotes.main(session["a"], session["b"]),
        )
    else:
        return render_template(
            "log.html",
        )

@app.route("/notees/")
def notees():
    if "a" in session:
        return render_template(
            "notees.html",
            notes=getallnotes.main(session["a"], session["b"]),
        )
    else:
        return render_template(
            "log.html",
        )



@app.route("/abs/")
def abs():
    if "a" in session:
        return render_template(
            "abs.html",
            abs=getabs.main(session["a"], session["b"]),
        )
    else:
        return render_template(
            "log.html",
        )


@app.route("/plann/")
def plann():
    if "a" in session:
        return render_template(
            "plann.html",
        )
    else:
        return render_template(
            "log.html",
        )


@app.route("/ome/")
def ome():
    if "a" in session:
        if "z" not in request.cookies:
            return render_template(
                "alerte.html",
            )
        else:
            return render_template(
                "ome.html",
            )
    else:
        return render_template(
            "log.html",
        )


@app.route("/links/")
def links():
    if "a" in session:
        return render_template(
            "links.html",
        )
    else:
        return render_template(
            "log.html",
        )


@app.route("/custom/")
def custom():
    if "a" in session:
        return render_template(
            "custom.html",
        )
    else:
        return render_template(
            "log.html",
        )


@app.route("/data", methods=["GET", "POST"])
def return_data():
    start = request.args.get("start")
    end = request.args.get("end")

    if "c" not in request.cookies:
        CalData = compress.main(start, end, session["a"], session["b"])
        resp = make_response(CalData)
        resp.set_cookie("c", CalData, max_age=378432000)
        # final = uncompress.main(CalData)
        return resp

    datacompress = request.cookies.get("c")
    datacompress = uncompress.main(datacompress)
    return datacompress


@app.route("/reload", methods=["GET", "POST"])
def reload():
    resp = make_response(render_template("plann.html"))
    resp.set_cookie("c", "", expires=0)
    return resp


@app.route("/alerte/", methods=["GET", "POST"])
def alerte():
    if "z" in request.cookies:
        if "a" in session:
            return render_template(
                "ome.html",
            )
        else:
            return render_template(
                "log.html",
            )
    else:
        return render_template(
            "alerte.html",
        )
        
        
@app.route("/ok/", methods=["GET","POST"])
def ok():
    if "z" not in request.cookies:
        if "a" in session:
            resp = make_response(render_template("ome.html",))
        else:
            resp = make_response(render_template("log.html",))
        resp.set_cookie("z", "1", max_age=378432000)
        return resp

    else:
        if "a" in session:
            return render_template(
                "ome.html",
            )
        else:
            return render_template(
                "log.html",
            )


@app.route("/log/", methods=["GET", "POST"])
def log():
    # handle the POST request
    if request.method == "POST":
        session["a"] = request.form.get("a")
        session["a"] = urllib.parse.quote(session["a"])

        session["b"] = request.form.get("b")
        session["b"] = urllib.parse.quote(session["b"])

        if validelogs.main(0, session["a"], session["b"]) != True:
            error = "Identifiants invalides ! Réessaye"
            return render_template("log.html", error=error)

        if "z" in request.cookies:
            resp = make_response(render_template("ome.html"))
        else:
            resp = make_response(render_template("alerte.html"))
                
        resp.set_cookie("a", encrypt.main(session["a"]), max_age=378432000, samesite="Strict", secure=True)
        resp.set_cookie("b", encrypt.main(session["b"]), max_age=378432000, samesite="Strict", secure=True)
        return resp

    # otherwise handle the GET request
    if "z" in request.cookies:
        return render_template(
            "log.html",
        )
    else:
        return render_template(
            "alerte.html",
        )
        