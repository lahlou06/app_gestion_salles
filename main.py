from data.dao_salle import DataSalle

dao = DataSalle()
connexion = dao.get_connection()

if connexion:
    print("connexion reussie")
    connexion.close()