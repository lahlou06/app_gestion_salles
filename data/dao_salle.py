import json
from multiprocessing import connection

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
def update_salle(self, salle):
    connection = self.get_connection()
    cursor = connection.cursor()
    requete = "UPDATE salle SET libelle=%s, type=%s, capacite=%s WHERE code=%s"
    valeurs = (salle.libelle, salle.type, salle.capacite, salle.code)
    cursor.excute(requete, valeurs)
    connection.commit()
    cursor.close()
    connection.close()
def delete_salle(self, code):
    connection = self.get_connection()
    cursor = connection.cursor()
    requete = "DELETE FROM salle WHERE code=%s"
    cursor.execute(requete, (code,))
    connection.commit()
    cursor.close()
    connection.close()
def get_salle(self, code):
    connection = self.get_connection()
    cursor = connection.cursor()
    requete = "SELECT * FROM salle WHERE code=%s"
    cursor.execute(requete, (code,))
    resultat = cursor.fetchone()
    cursor.close()
    connection.close()
    if resultat:
        return resultat
    return None
def get_salles(self):
    connection = self.get_connection()
    cursor = connection.cursor()
    requete = "SELECT * FROM salle"
    cursor.execute(requete)
    resultats = cursor.fetchall()
    cursor.close()
    connection.close()
    return resultats




