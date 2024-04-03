import tkinter as tk
import mysql.connector

class VentanaConsultarGeneral:
    def __init__(self):
        self.consultargVentana = tk.Toplevel()
        self.consultargVentana.title("Consulta General")
        self.consultargVentana.geometry("800x600")
        self.consultargVentana.resizable(width=False, height=False)
        self.consultargVentana.grab_set()
        self.consultargVentana.iconbitmap("icon.ico")