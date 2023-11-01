from pymongo import MongoClient

class DataAccess :

    @classmethod
    def connexion(cls) :
        cls.client = MongoClient("mongodb://root:example@mongo:27017")
        cls.db = cls.client['consommations']

    @classmethod
    def deconnexion(cls) :
        cls.client.close()

    @classmethod
    def get_all_consommations(cls):
        consommations = cls.db.consommation_departements.find({},{ "_id": 0 })
        return list(consommations)    

    @classmethod
    def get_consommation (cls, departement):
        consommation = cls.db.consommation_departements.find({"DEPARTEMENT":departement},{ "_id": 0 })
        return list(consommation)

    @classmethod
    def del_consommation(cls, departement):
        cls.db.consommation_departements.delete_one({"DEPARTEMENT":departement})

    @classmethod
    def set_consommation(cls, annee, consor, consot, consoi, consoa, consona, departement):
        consommation = {"ANNEE":annee, "CONSOR":consor, "CONSOT":consot, "CONSOI":consoi, "CONSOA":consoa, "CONSONA":consona, "DEPARTEMENT":departement}
        cls.db.consommation_departements.insert_one(consommation)

    @classmethod
    def update_consommation(cls, annee, consor, consot, consoi, consoa, consona, departement):
        consommation = { "ANNEE":annee, "CONSOR":consor, "CONSOT":consot, "CONSOI":consoi, "CONSOA":consoa, "CONSONA":consona, "DEPARTEMENT":departement}
        cls.db.consommation_departements.update_one({"DEPARTEMENT":departement}, {'$set':consommation})


