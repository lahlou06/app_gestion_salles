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
