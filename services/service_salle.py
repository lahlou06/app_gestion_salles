from enum import nonmember

from mysql.connector.constants import flag_is_set


class ServiceSalle:
    pass
from data.dao_salle import DataSalle

class ServiceSalle:
    def __init__(self):
        self.dao_salle = DataSalle()
    def ajouter_salle(self, salle):
        if salle.code and salle.libelle and salle.type and salle.capacite >= 1:
            self.dao_salle.insert_salle(salle)
            return True
        return False
    def ajouter_salle(self, salle):
        if salle.code and salle.libelle and salle.type and salle.capacite >= 1:
            self.dao_salle.insert_salle(salle)
            return True, "Salle ajouter avec succes"
        return False, "Erreur lors de l'ajout de la salle"
    def modifier_salle(self, salle):
        if salle.code and salle.libelle and salle.type and salle.capacite >= 1:
            self.dao_salle.update_salle(salle)
            return True, "Salle modifiee avec succes"
        return False, "Erreur lors de la modification"
    def supprimer_salle(self, code):
        if code:
            self.dao_salle.delete_salle(code)
            return True, "Salle supprimee avec succes"
        return False, "Erreur lors de la suppression"
    def rechercher_salle(self, code):
        if code:
            resultat = self.dao_salle.get_salle(code)
            return resultat
        return None

