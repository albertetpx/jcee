"""
JCEE App for handling DUAL/FCT schedules
Author: A.Guardiola
Versión: Beta (calendar updates for schoolyear 2526)
Date: September 25
"""

import db.db as db
from flask import Flask, render_template, request, jsonify
import os

# Secuencia principal
app = Flask(__name__)

# Database initialization
db.initBD()
db.defaultHolidays()

@app.route("/")
def root():
    currentYear=["Setembre 25","Octubre 25","Novembre 25","Desembre 25","Gener 26","Febrer 26",
        "Març 26","Abril 26","Maig 26","Juny 26","Juliol 26","Agost 26"]
    nextYear=["Setembre 26","Octubre 26","Novembre 26","Desembre 26","Gener 27","Febrer 27",
        "Març 27","Abril 27","Maig 27","Juny 27","Juliol 27","Agost 27"]
    holidays =  db.consultarFestivos()
    schoolYear = ('2025-09-01','2026-07-31')
    xmas = ('2025-12-22','2026-01-07')
    easter = ('2026-03-30','2026-04-06')
    return render_template("index.html", periode=(currentYear,nextYear),holidays=holidays,
        schoolYear=schoolYear,xmas=xmas,easter=easter)

@app.route("/crearFestivo", methods=['POST'])
def crearFestivo():
    if request.method == 'POST':
        name = request.form.get("name")
        date = request.form.get("date")
        type = request.form.get("type")
        try:
            db.crearFestivo(date,name,type)
            holidays  = db.consultarFestivos()
            print(holidays)
            return jsonify(holidays)
        except Exception as e:
            print(e)
            return "Holiday could not be created."
        
@app.route("/eliminarFestivo", methods=['POST'])
def eliminarFestivo():
    if request.method == 'POST':
        name = request.form.get("name")
        date = request.form.get("date")
        try:
            db.eliminarFestivo(date,name)
            holidays  = db.consultarFestivos()
            print(holidays)
            return jsonify(holidays)
        except Exception as e:
            print(e)
            return "Holiday could not be removed."

# app.config['JSON_AS_ASCII'] = False
# app.config['DEBUG'] = not(os.getenv('RENDER'))
# app.config['TEMPLATES_AUTO_RELOAD'] = True
# app.run()
