"""
JCEE App for handling DUAL/FCT schedules
Author: A.Guardiola
Versión: Beta (calendar updates for schoolyear 2324)
Date: September 23
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
    currentYear=["Setembre 23","Octubre 23","Novembre 23","Desembre 23","Gener 24","Febrer 24",
        "Març 24","Abril 24","Maig 24","Juny 24","Juliol 24","Agost 24"]
    nextYear=["Setembre 24","Octubre 24","Novembre 24","Desembre 24","Gener 25","Febrer 25",
        "Març 25","Abril 25","Maig 25","Juny 25","Juliol 25","Agost 25"]
    holidays =  db.consultarFestivos()
    schoolYear = ('2023-09-01','2024-07-31')
    xmas = ('2023-12-21','2024-01-07')
    easter = ('2024-03-23','2024-04-01')
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
