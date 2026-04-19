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