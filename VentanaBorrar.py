import tkinter as tk
from tkinter import messagebox
import mysql.connector
from Conexiones import solicitudesDB
from PIL import Image, ImageTk
from Conexiones import solicitudesDB

class VentanaBorrar:
    def __init__(self, BorrarVentana):
        self.BorrarVentana = BorrarVentana
        self.BorrarVentana.title("INDICA - Reiniciar Base de Datos")
        self.BorrarVentana.geometry("500x300")
        self.BorrarVentana.resizable(width=False, height=False)
        self.BorrarVentana.configure(background='#ffffff')
        self.coloruniversal="#ff8000"
        self.BorrarVentana.iconbitmap("imagenes/icono/icon.ico")
        self.BorrarVentana.grab_set()

        self.imagen = Image.open("imagenes/pcba.jpg")
        self.tamano_imagen_deseado = (100, 100)
        self.imagen_redimensionada = self.imagen.resize(self.tamano_imagen_deseado)
        self.tkimagen = ImageTk.PhotoImage(self.imagen_redimensionada)

        # Mostrar la imagen en un Label
        self.label = tk.Label(self.BorrarVentana, image=self.tkimagen, background="#ffffff")
        self.label.pack()
        self.label.place(x=0,y=0)
        # -------------------- #

        self.labeltitulo = tk.Label(self.BorrarVentana, text="Reiniciar Base de Datos", font=("Arial", 18),background="#ffffff")
        self.labeltitulo.pack()
        self.labeltitulo.place(x=100, y=40)

        self.labelinfo = tk.Label(self.BorrarVentana,
                                  text="Al presionar el boton BORRAR, usted procedera a eliminar todos los registros y solicitudes del sistema. Si no esta seguro de realizar esta operacion consulte con el personal administrativo capacitado.",
                                  font=("Arial", 12),justify="left", wraplength=500, background="#ffffff")
        self.labelinfo.pack()
        self.labelinfo.place(x=10, y=100)
        
        
        self.botonsoli = tk.Button(self.BorrarVentana, text="BORRAR", command=self.borrar, width=10, height=1,font=("Arial",15,"bold"),background=self.coloruniversal,fg="white",)
        self.botonsoli.pack()
        self.botonsoli.place(x=180, y=170)

        # Boton Cerrar
        self.botonCerrar = tk.Button(self.BorrarVentana, text="Cerrar", command=self.cerrar_ventana,width=10, height=1,font=("Arial",12,"bold"),background=self.coloruniversal,fg="white",) 
        self.botonCerrar.pack()  # Colocar el botón en la posición predeterminada
        self.botonCerrar.place(x=190, y=230)
        

    def cerrar_ventana(self):
        self.BorrarVentana.destroy()        
    def borrar(self):
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
            query9 = "DELETE FROM estudiante"
            query4 = "ALTER TABLE VinculoSolicitud AUTO_INCREMENT = 0"
            query5 = "TRUNCATE TABLE VinculoSolicitud"
            query6 = "ALTER TABLE VinculoSolicitud AUTO_INCREMENT = 1; "
            query7 = "SET FOREIGN_KEY_CHECKS = 1;"
            query8 = "SET SQL_SAFE_UPDATES = 1;"
            cursor.execute(query)
            cursor.execute(query2)
            cursor.execute(query3)
            cursor.execute(query9)
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