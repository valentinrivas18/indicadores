import tkinter as tk
import mysql.connector

class VentanaConsulta:
    def __init__(self, consultaventana):
        self.consultaventana = consultaventana
        self.consultaventana.title("Ventana de Consulta")
        self.consultaventana = tk.Button(self.consultaventana, text="Consulta", command=self.imprimir)
        self.consultaventana.pack()

if __name__ == "__main__":
    consultaventana = tk.Tk()
    app = VentanaConsulta(consultaventana)
    consultaventana.mainloop()

    
        