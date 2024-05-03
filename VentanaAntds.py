import tkinter as tk
from tkinter import messagebox
import mysql.connector

class VentanaAntds:
    def __init__(self, antdsVentana):
        self.antdsVentana = antdsVentana
        self.antdsVentana.title("Reiniciar Base de Datos")
        self.antdsVentana.geometry("500x400")
        self.antdsVentana.resizable(width=False, height=False)
        self.antdsVentana.grab_set()

        self.solic_texto = tk.Entry(self.antdsVentana)
        self.solic_texto.pack()
        self.solic_texto.place(x=300, y=130)

        self.labeltitulo = tk.Label(self.antdsVentana, text="Reiniciar Base de Datos", font=("Arial", 18))
        self.labeltitulo.pack()
        self.labeltitulo.place(x=100, y=50)

        self.labelinfo = tk.Label(self.antdsVentana,
                                  text="Al presionar el boton BORRAR, usted procedera a eliminar todos \n los registros y solicitudes del sistema. \n Si no esta seguro de realizar esta operacion consulte con el personal \n administrativo capacitado.",
                                  font=("Arial", 12))
        self.labelinfo.pack()
        self.labelinfo.place(x=10, y=100)
        
        
        self.botonsoli = tk.Button(self.antdsVentana, text="BORRAR", command=self.insertar, font=("Arial",15))
        self.botonsoli.pack()
        self.botonsoli.place(x=220, y=200)
        
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