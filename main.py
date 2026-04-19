from data.dao_salle import DataSalle

dao = DataSalle()
connexion = dao.get_connection()

if connexion:
    print("connexion reussie")
    connexion.close()
from data.dao_salle import DataSalle
from models.salle import Salle
dao = DataSalle()
salle = Salle("A06", "Salle Info", "Laboratoire", 30)
dao.insert_salle(salle)
print("salle ajoutee")
from data.dao_salle import DataSalle

dao = DataSalle()
dao.delete_salle("A06")
print("salle supprimee")
from data.dao_salle import DataSalle
from models.salle import Salle

dao = DataSalle()
salle = Salle("A06", "Salle Modifiee", "Bureau", 40)
dao.update_salle(salle)
print("salle modifiee")
from data.dao_salle import DataSalle

dao = DataSalle()
resultat = dao.get_salle("A06")
print(resultat)
from data.dao_salle import DataSalle

dao = DataSalle()
resultats = dao.get_salles()

for salle in resultats:
    print(salle)
from services.service_salle import ServiceSalle
from models.salle import Salle

service = ServiceSalle()
print("Liste des salles")
resultats = service.recuperer_salles()
for salle in resultats:
    print(salle)
    print("Ajout d une salle")
    nouvelle_salle = Salle("A10", "Salle Test", "Laboratoire", 25)
    resultat = service.ajouter_salle(nouvelle_salle)
    print(resultat)
print("Modification d une salle")
salle_modifiee = Salle("A11", "Salle Test Modifiee", "Bureau", 30)
resultat = service.modifier_salle(salle_modifiee)
print(resultat)
print("Recherche d une salle")
resultat = service.rechercher_salle("A11")
print(resultat)
print("Suppression d une salle")
resultat = service.supprimer_salle("A11")
print(resultat)