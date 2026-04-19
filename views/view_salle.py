import customtkinter as ctk
from services.service_salle import ServiceSalle

class ViewSalle(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.service_salle = ServiceSalle()
        self.frame_info = ctk.CTkFrame(self)
        self.frame_info.pack(pady=10, padx=10, fill="x")
        self.label_code = ctk.CTkLabel(self.frame_info, text="code salle")
        self.label_code.grid(row=0, column=0, padx=10, pady=5)
        self.entry_code = ctk.CTkEntry(self.frame_info)
        self.entry_code.grid(row=0, column=1, padx=10, pady=5)

        self.label_libelle = ctk.CtkLabel(self.frame_info, text="libelle")
        self.label_libelle.grid(row=1, column=0, padx=10, pady=5)
        self.entry_libelle = ctk.CTkEntry(self.frame_info)
        self.entry_libelle.grid(row=1, column=1, padx=10, pady=5)

        self.label_type = ctk.CTkLabel(self.frame_info, text="Type")
        self.label_type.grid(row=2, column=0, padx=10, pady=5)
        self.entry_type = ctk.CTkEntry(self.frame_info)
        self.entry_type.grid(row=2, column=1, padx=10, pady=5)

        self.label = ctk.CTkLabel(self.frame_info, text="Capacite")
        self.label.grid(row=3, column=0, padx=10, pady=5)
        self.entry_capacite = ctk.CTkEntry(self.frame_info)
        self.entry_capacite.grid(row=3, column=1, padx=10, pady=5)