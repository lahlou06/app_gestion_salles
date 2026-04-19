import json
import mysql.connector
class DataSalle:
    pass
def get_connection(self):
    with open("data/config.json", "r") as fichier:
        config = json.load(fichier)
    connection = mysql.connector.connect(
        host=config["host"],
        user=config["user"],
        password=config["password"],
        database=config["database"],
    )
    return connection
def insert_salle(self,salle):
    connection = self.get_connection()
    cursor = connection.cursor()
    requete = "INSERT INTO salle (code, libelle, type, capacite) VALUES (%s, %s, %s, %s)"
    valeurs = (salle.code, salle.libelle, salle.type, salle.capacite)
    cursor.excute(requete, valeurs)
    connection.commit()
    cursor.close()
    connection.close()



