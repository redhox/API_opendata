from flask import Flask, render_template, request, jsonify
from data import DataAccess as da

app = Flask(__name__)

@app.route("/api/consommation", methods=['GET'])
def get_all_consommations():
    da.connexion()
    departments = da.get_all_consommations()
    print(departments)
    da.deconnexion()

    return jsonify(departments), 200

@app.route("/api/consommation/<string:departement>", methods=['GET'])
def get_consommation(departement):
    da.connexion()
    department = da.get_consommation(departement)
    da.deconnexion()

    return jsonify(department), 200

@app.route("/api/consommation/<string:departement>", methods=['DELETE'])
def del_consommation(departement):
    da.connexion()
    da.del_consommation(departement)
    da.deconnexion()

    return jsonify({"message":"ok"}), 200

@app.route("/api/consommation", methods=['POST'])
def set_consommation():
    annee = request.values.get("ANNEE")
    consor = request.values.get("CONSOR")
    consot = request.values.get("CONSOT")
    consoi = request.values.get("CONSOI")
    consoa = request.values.get("CONSOA")
    consona = request.values.get("CONSONA")
    departement = request.values.get("DEPARTEMENT")

    da.connexion()
    da.update_consommation(annee, consor, consot, consoi, consoa, consona, departement)
    da.deconnexion()

    return jsonify({"message":"ok"}), 200

@app.route("/api/consommation/<string:departement>", methods=['PUT'])
def put_consommation(id):
    annee = request.values.get("ANNEE")
    consor = request.values.get("CONSOR")
    consot = request.values.get("CONSOT")
    consoi = request.values.get("CONSOI")
    consoa = request.values.get("CONSOA")
    consona = request.values.get("CONSONA")
    departement = request.values.get("DEPARTEMENT")

    da.connexion()
    da.update_consommation(annee, consor, consot, consoi, consoa, consona, departement)
    da.deconnexion()

    return jsonify({"message":"ok"}), 200

@app.errorhandler(404)
def page_not_found(e):
    return "erreur", 404

if __name__ == "__main__" :
    app.run(debug=True, port=5001)