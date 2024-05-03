import tkinter as tk
from tkinter import messagebox
import mysql.connector

class VentanaBorrar:
    def __init__(self, BorrarVentana):
        self.BorrarVentana = BorrarVentana
        self.BorrarVentana.title("Reiniciar Base de Datos")
        self.BorrarVentana.geometry("500x400")
        self.BorrarVentana.resizable(width=False, height=False)
        self.BorrarVentana.grab_set()

        self.solic_texto = tk.Entry(self.BorrarVentana)
        self.solic_texto.pack()
        self.solic_texto.place(x=300, y=130)

        self.labeltitulo = tk.Label(self.BorrarVentana, text="Reiniciar Base de Datos", font=("Arial", 18))
        self.labeltitulo.pack()
        self.labeltitulo.place(x=100, y=50)

        self.labelinfo = tk.Label(self.BorrarVentana,
                                  text="Al presionar el boton BORRAR, usted procedera a eliminar todos \n los registros y solicitudes del sistema. \n Si no esta seguro de realizar esta operacion consulte con el personal \n administrativo capacitado.",
                                  font=("Arial", 12))
        self.labelinfo.pack()
        self.labelinfo.place(x=10, y=100)
        
        
        self.botonsoli = tk.Button(self.BorrarVentana, text="BORRAR", command=self.borrar, font=("Arial",15))
        self.botonsoli.pack()
        self.botonsoli.place(x=220, y=200)
        
    def borrar(self):
        texto = self.solic_texto.get()
        conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="valentin",
        database="indic",
        port="3307"
        )

        cursor = conexion.cursor()
        respuesta = messagebox.askyesno("Confirmación", "¿Desea eliminar los registros de solicitudes? Una vez eliminados los datos, no podran ser recuperados, esta operacion es irreversible.")
        if respuesta:
            query = "SET SQL_SAFE_UPDATES = 0;"
            query2 = "SET FOREIGN_KEY_CHECKS = 0"
            query3 = "DELETE FROM VinculoSolicitud"
            query4 = "ALTER TABLE VinculoSolicitud AUTO_INCREMENT = 0"
            query5 = "TRUNCATE TABLE VinculoSolicitud"
            query6 = "ALTER TABLE VinculoSolicitud AUTO_INCREMENT = 1; "
            query7 = "SET FOREIGN_KEY_CHECKS = 1;"
            query8 = "SET SQL_SAFE_UPDATES = 1;"
            cursor.execute(query)
            cursor.execute(query2)
            cursor.execute(query3)
            cursor.execute(query4)
            cursor.execute(query5)
            cursor.execute(query6)
            cursor.execute(query7)
            cursor.execute(query8)
            conexion.commit()
            print("Se eliminaron los registros de solicitudes existentes.")
            messagebox.showinfo("Confirmación", "Se eliminaron los registros de solicitudes existentes.")
            messagebox.showinfo("Confirmación", "La operacion que usted realizo no puede ser reversida, si la acciono por accidente, consulte a un administrador.")
        else:
            messagebox.showinfo("Confirmación", "NO Se eliminaron los registros de solicitudes existentes.")
            # No realiza la operación
            print("Operación cancelada")

  
        def cerrarW(self):
            self.ventana.destroy()
            exit()

if __name__ == "__main__":
    ventana = tk.Tk()
    app = VentanaBorrar(ventana)
    ventana.mainloop()