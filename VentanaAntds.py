import tkinter as tk
from tkinter import messagebox
import mysql.connector

class VentanaAntds:
    def __init__(self, antdsVentana):
        self.antdsVentana = antdsVentana
        self.antdsVentana.title("Agregar nuevo tipo de solicitud")
        self.antdsVentana.geometry("800x600")
        self.antdsVentana.resizable(width=False, height=False)
        self.antdsVentana.grab_set()

        self.solic_texto = tk.Entry(self.antdsVentana)
        self.solic_texto.pack()
        self.solic_texto.place(x=300, y=130)

        self.labelsolic = tk.Label(self.antdsVentana, text="Solicitud")
        self.labelsolic.pack()
        self.labelsolic.place(x=300, y=100)

        self.labeltitulo = tk.Label(self.antdsVentana, text="Agregar nuevo tipo de solicitud", font=("Arial", 18))
        self.labeltitulo.pack()
        self.labeltitulo.place(x=250, y=50)
        
        
        self.botonsoli = tk.Button(self.antdsVentana, text="Agregar", command=self.insertar)
        self.botonsoli.pack()
        self.botonsoli.place(x=280, y=170)
        
    def insertar(self):
        texto = self.solic_texto.get()
        conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="valentin",
        database="indic",
        port="3307"
        )

        cursor = conexion.cursor()

        # insertar 1 dato
        query = "INSERT INTO solicitudes(solicitud) VALUES (%s)"
        cursor.execute(query,(texto,))
        conexion.commit()
        print("Se insterto el dato.")
        messagebox.showinfo("Confirmación", "El dato ha sido ingresado correctamente.")

if __name__ == "__main__":
    ventana = tk.Tk()
    app = VentanaAntds(ventana)
    ventana.mainloop()