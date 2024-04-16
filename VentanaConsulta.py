import tkinter as tk
import mysql.connector
from uno import *
from dos import *
from tres import *
from cuatro import *
from cinco import *
from seis import *
from siete import *
from ocho import *
from nueve import *

class VentanaConsulta:
    def __init__(self, consultaventana):
        self.consultaventana = consultaventana
        self.consultaventana.title("Ventana de Consulta")
        self.consultaventana = tk.Button(self.consultaventana, text="Consulta", command=self.imprimir)
        self.consultaventana.pack()

    def imprimir(self):
        page1()



if __name__ == "__main__":
    consultaventana = tk.Tk()
    app = VentanaConsulta(consultaventana)
    consultaventana.mainloop()

    
        