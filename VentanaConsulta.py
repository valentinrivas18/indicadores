import tkinter as tk
import mysql.connector
from tablareporte import *

comandos = generador()
class VentanaConsulta:
    def __init__(self, consultaventana):
        self.consultaventana = consultaventana
        self.consultaventana.title("Ventana de Consulta")
        self.consultaventana.geometry("320x240")
        self.consultaventana.resizable(width=False, height=False)
        self.botonconsulta = tk.Button(consultaventana, text="Consulta", command=comandos.pdfs)
        self.etiquetaconsulta = tk.Label(consultaventana, text="Haz clic en consulta para generar el pdf")
        self.etiquetaconsulta.pack()
        self.etiquetaconsulta.place(x=60, y=40)
        self.botonconsulta.pack()
        self.botonconsulta.place(x=130, y=100)
        self.cerrarventana = tk.Button(consultaventana, text="Cerrar")

if __name__ == "__main__":
    consultaventana = tk.Tk()
    app = VentanaConsulta(consultaventana)
    consultaventana.mainloop()