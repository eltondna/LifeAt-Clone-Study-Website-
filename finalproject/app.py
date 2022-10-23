from flask import Flask, flash, redirect, render_template, request
import os


app= Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"]


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=['GET','POST'])
def index():
    return render_template("index.html")


@app.route("/hero")
def hero():
    return render_template("hero.html")
    
    
@app.route("/demon")
def demon():
    return render_template("demon.html")

@app.route("/ania")
def ania():
    return render_template('ania.html')

@app.route("/rengoku")
def rengoku():
    return render_template('rengoku.html')


@app.route("/tinytan")
def tinytan():
    return render_template('tinytan.html')








