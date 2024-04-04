import tkinter as tk
from tkinter import *
from VentanaAgregar import VentanaAgregar
from VentanaAntds import VentanaAntds
from PIL import Image, ImageTk


class VentanaPrincipal:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("INDICADORES")
        self.ventana.geometry("1024x768")
        self.ventana.resizable(width=False, height=False)
        
        # Boton Agregar
        self.boton1 = tk.Button(self.ventana, text="Agregar", width=10, height=1, font=("Arial", 12), command=self.abrir_agregar) 
        self.boton1.pack()  # Colocar el botón en la posicion predeterminada
        self.boton1.place(x=500, y=184)

        # Boton Consulta
        self.boton2 = tk.Button(self.ventana, text="Consulta", width=15, height=1, font=("Arial", 12)) 
        self.boton2.pack()  # Colocar el botón en la posicion predeterminada
        self.boton2.place(x=475, y=250)

        # Boton Consulta por subprograma
        self.boton3 = tk.Button(self.ventana, text="Consulta por Subprograma", width=22, height=1, font=("Arial", 12)) 
        self.boton3.pack()  # Colocar el botón en la posición predeterminada
        self.boton3.place(x=445, y=316)

        # Boton de agregar nuevo tipo de solicitud
        self.boton4 = tk.Button(self.ventana, text="ANTDS", font=("Arial", 12), command=self.abrir_antds)
        self.boton4.pack()
        self.boton4.place(x=510,y=380)

    def abrir_antds(self):
        self.ventana_antds = tk.Toplevel(self.ventana)
        self.app_antds = VentanaAntds(self.ventana_antds)
        
    def abrir_agregar(self):
        self.ventana_agregar = tk.Toplevel(self.ventana)
        self.app_agregar = VentanaAgregar(self.ventana_agregar)    
       
if __name__ == "__main__":
    ventana = tk.Tk()
    app = VentanaPrincipal(ventana)
    ventana.mainloop()