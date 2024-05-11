import tkinter as tk
import mysql.connector
from GeneradorPDF import *
from tkinter import messagebox
from Conexiones import solicitudesDB

ded = solicitudesDB
comandos = generador()
class VentanaConsulta:
    def __init__(self, consultaventana):
        self.consultaventana = consultaventana
        self.consultaventana.title("INDICA - Generar Reporte")
        self.consultaventana.geometry("320x240")
        w = 320
        h = 240

        screen_width = consultaventana.winfo_screenwidth()
        screen_height = consultaventana.winfo_screenheight()

        x = (screen_width/2) - (w/2)
        y = (screen_height/2) - (h/2)

        consultaventana.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.consultaventana.resizable(width=False, height=False)
        self.consultaventana.configure(background='#ffffff')
        self.coloruniversal="#ff8000"
        self.consultaventana.iconbitmap("imagenes/icono/icon.ico")
        self.consultaventana.grab_set()

        # etiqute del titulo
        self.etiquetaconsulta = tk.Label(consultaventana, text="Haz clic en Generar \n para generar el reporte.",
                                         font=("Arial",14,"bold"),anchor="center", background="#ffffff", fg="black")
        self.etiquetaconsulta.pack()
        self.etiquetaconsulta.place(x=60, y=20)
        # boton consulta
        self.botonconsulta = tk.Button(consultaventana,text="Generar", command=comandos.pdfs,
                                       font=("Arial",12,"bold"),background=self.coloruniversal,fg="white",
                                       width=10, height=1)
        self.botonconsulta.pack()
        self.botonconsulta.place(x=110, y=100)
        # boton de cerrar ventana
        self.cerrarventana = tk.Button(consultaventana, text="Cerrar", command=self.cerrar_ventana,
                                       font=("Arial",12,"bold"),background=self.coloruniversal,fg="white",
                                       width=10, height=1)
        self.cerrarventana.pack()
        self.cerrarventana.place(x=110, y=150)
    def cerrar_ventana(self):
            self.consultaventana.destroy()

if __name__ == "__main__":
    consultaventana = tk.Tk()
    app = VentanaConsulta(consultaventana)
    consultaventana.mainloop()