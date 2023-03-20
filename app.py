"""
JCEE App for handling DUAL/FCT schedules
Author: A.Guardiola
Versión: Alfa
Date: December 22
"""

import db.db as db
from flask import Flask, render_template, request, jsonify
import os

# Secuencia principal
# cal.crearFestivo('Constitución','2022-12-06','NAC')
# print(cal.esLaborable('2022-12-06'))
app = Flask(__name__)

# Database initialization
db.initBD()
db.defaultHolidays()

@app.route("/")
def root():
    currentYear=["Setembre 22","Octubre 22","Novembre 22","Desembre 22","Gener 23","Febrer 23",
        "Març 23","Abril 23","Maig 23","Juny 23","Juliol 23","Agost 23"]
    nextYear=["Setembre 23","Octubre 23","Novembre 23","Desembre 23","Gener 24","Febrer 24",
        "Març 24","Abril 24","Maig 24","Juny 24","Juliol 24","Agost 24"]
    holidays =  db.consultarFestivos()
    schoolYear = ('2022-09-01','2023-07-31')
    xmas = ('2022-12-22','2023-01-08')
    easter = ('2023-04-03','2023-04-10')
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

app.config['JSON_AS_ASCII'] = False
if os.getenv('RENDER') != True:
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)