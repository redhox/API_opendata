from flask import Flask, render_template, jsonify, redirect, url_for, request
import json
import requests
import pandas as pd
from statistics import mean
import pprint
#consommation

URL_API = "http://flask-serveur:5001/api/consommation"

app = Flask(__name__)


@app.route("/")
def index():
    reponse = requests.get(URL_API)
    departements = json.loads(reponse.content.decode("utf-8"))
    liste_department=set()
    for departement in departements:
        liste_department.add(departement['DEPARTEMENT'])
    
    liste_department = list(liste_department)
    
    df = pd.DataFrame(departements)
    moyenne_dep_years = df.groupby(["DEPARTEMENT", "ANNEE"]).mean().reset_index()
    moyenne_dep_years_list = moyenne_dep_years.to_dict(orient="records")
    pprint.pprint(moyenne_dep_years_list)
        
    return render_template("index.html", etudiants=departements ,liste_department=liste_department,moyenne_dep_years_list=moyenne_dep_years_list)


@app.route("/departement/<string:id>")
def get_etudiant(id):
    url = URL_API + "/" + id
    reponse = requests.get(url)
    content = json.loads(reponse.content.decode("utf-8"))
    
    return render_template("etudiant.html", contenu=content)


"""
@app.route("/etudiant/delete/<string:id>")
def del_etudiant(id):
    url = URL_API + "/"+id
    requests.delete(url)
    return redirect(url_for('index'), code=302)

@app.route("/etudiant/add")
def add_etudiant():
    contenu = {"title":"Inscription", "subtitle":"Remplir", "url":url_for('create_etudiant'), "nom":"", "prenom":"", "age":"", "classe":""}
    return render_template("inscription.html", contenu=contenu)

@app.route("/etudiant/create", methods=['POST'])
def create_etudiant():
    nom = request.values.get("nom")
    prenom = request.values.get("prenom")
    age = request.values.get("age")
    classe = request.values.get("classe")
    requests.post(URL_API, data={"nom":nom, "prenom":prenom, "age":age, "classe":classe})
    return  redirect(url_for('index'), code=302)

@app.route("/etudiant/update/<string:id>")
def update_etudiant(id):
    url = URL_API + "/" + id
    reponse = requests.get(url)
    etudiant = json.loads(reponse.content.decode("utf-8"))
    contenu = {"title":"Modification", "subtitle":"Modifier", "url":url_for('maj_etudiant', id=id), "nom":etudiant['nom'], "prenom":etudiant['prenom'], "age":etudiant['age'], "classe":etudiant['classe']}
    return render_template("inscription.html", contenu=contenu)

@app.route("/etudiant/maj/<string:id>", methods=['POST'])
def maj_etudiant(id):
    url = URL_API + "/" + id
    nom = request.values.get("nom")
    prenom = request.values.get("prenom")
    age = request.values.get("age")
    classe = request.values.get("classe")
    requests.put(url, data={"nom":nom, "prenom":prenom, "age":age, "classe":classe})
    return  redirect(url_for('index'), code=302)
"""

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

if __name__ == "__main__" :
    app.run(debug=True)
