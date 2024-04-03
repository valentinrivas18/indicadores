import tkinter as tk
import mysql.connector

class VentanaConsulta:
    def __init__(self, root):
        self.root = root
        self.root.title("Ventana de Consulta")

        # Conexión a la base de datos MySQL
        conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="valentin",
        database="indic",
        port="3307"
        )
        
        cursor = conexion.cursor()
        
        # Ejemplo de consulta a una tabla llamada 'datos'
        query = "SELECT * FROM VinculoSolicitud"
        
        cursor.execute(query)
        d = cursor.fetchall()
        print(d)
        for row in d:
            label_texto = tk.Label(self.root, text=row)  # Suponiendo que el texto está en la segunda columna
            label_texto.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaConsulta(root)
    root.mainloop()

    
        