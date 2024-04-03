import tkinter as tk
import mysql.connector

class VentanaInsercion:
    def __init__(self, root):
        self.root = root
        self.root.title("Ventana de Inserción")

        self.entry_texto = tk.Entry(self.root)
        self.entry_texto.pack()

        self.button_insertar = tk.Button(self.root, text="Insertar en BD", command=self.insertar_en_bd)
        self.button_insertar.pack()

    def insertar_en_bd(self):
        texto = self.entry_texto.get()
        
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="valentin",
            database="indic",
            port="3307"
            )
        
        cursor = conexion.cursor()
        
        # Ejemplo de inserción en una tabla llamada 'datos'
        query = "INSERT INTO solicitudes (solicitud) VALUES (%s)"
        cursor.execute(query, (texto,))
        
        conexion.commit()

if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaInsercion(root)
    root.mainloop()