import customtkinter as ctk
from tkinter import ttk, messagebox

from models.salle import Salle
from services.service_salle import ServiceSalle

class ViewSalle(ctk.CTk):
    def _init_(self):
        super()._init_()
        self.title("Gestion des salles")
        self.geometry("750x500")

        self.service_salle = ServiceSalle()

        self.creer_widgets()
        self.lister_salles()