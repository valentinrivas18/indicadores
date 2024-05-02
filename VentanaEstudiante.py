import tkinter as tk
from tkinter import messagebox
import mysql.connector
from tkinter import ttk
class VentanaEstudiante:
    def __init__(self, EstudianteVentana):
        self.EstudianteVentana = EstudianteVentana
        self.EstudianteVentana.title("Agregar")
        self.EstudianteVentana.geometry("400x350")
        self.EstudianteVentana.resizable(width=False, height=False)
        self.EstudianteVentana.iconbitmap("icon.ico")
        self.EstudianteVentana.resizable(width=False, height=False)
        self.EstudianteVentana.configure(background='#ffffff')
        self.coloruniversal="#ff8000"
        self.EstudianteVentana.iconbitmap("icon.ico")
        self.EstudianteVentana.grab_set()
        def validate_input(new_value):
            if new_value == "":
                return True
            try:
                int(new_value)
                return len(new_value) <= 8
            except ValueError:
                return False

        cs = self.EstudianteVentana.register(validate_input)  # Registrar la función de validación

        conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="valentin",
        database="indic",
        port="3307"
        )

        connection = conexion.cursor()
        # Realizar una consulta para obtener los registros del campo deseado

        # label text paracedula
        self.titulo = tk.Label(EstudianteVentana, text="Registrar estudiante", width=20, height=1, font=("Arial", "15","bold"),background="#ffffff")
        self.titulo.pack()
        self.titulo.place(x=75, y=40)

        # label text paracedula
        self.labelcedula = tk.Label(EstudianteVentana, text="Cedula", width=20, height=1, font=("Arial", "14","bold"),background="#ffffff")
        self.labelcedula.pack()
        self.labelcedula.place(x=70, y=100)
        # textbox de la cedula
        self.cedula_texto = tk.Entry(EstudianteVentana, width=15,font=("Arial",12),justify=tk.CENTER,validate="key",validatecommand=(cs, "%P"))
        self.cedula_texto.pack()
        self.cedula_texto.place(x=130, y=150)

        # Boton Agregar
        self.botonAgregar = tk.Button(EstudianteVentana, text="Agregar", command=self.agregar,width=10, height=1,font=("Arial",12,"bold"),background=self.coloruniversal,fg="white",) 
        self.botonAgregar.pack()  # Colocar el botón en la posición predeterminada
        self.botonAgregar.place(x=150, y=200)

        # Boton Cerrar
        self.botonCerrar = tk.Button(EstudianteVentana, text="Cerrar", command=self.cerrar_ventana,width=10, height=1,font=("Arial",12,"bold"),background=self.coloruniversal,fg="white",) 
        self.botonCerrar.pack()  # Colocar el botón en la posición predeterminada
        self.botonCerrar.place(x=150, y=250)
        

    def cerrar_ventana(self):
                self.EstudianteVentana.destroy()
    def agregar(self):
        conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="valentin",
        database="indic",
        port="3307"
        )
        cursor = conexion.cursor()
        #obteniendo datos del combobox1 (el id de la carrera)
        dato_seleccionado = self.opcionSeleccionada.get()
        if dato_seleccionado:
            print(dato_seleccionado)
        else:
            messagebox.showerror("Campo Vacío", 
                             "Por favor, ingrese texto antes de imprimir.")
        query = "SELECT id_carrera FROM subprograma WHERE carrera = %s"
        cursor.execute(query, (dato_seleccionado,))
        resultado = cursor.fetchall()
        cursor.fetchall()
        conexion.commit()
        
        mi_tupla = tuple(resultado)
        entero = int(mi_tupla[0][0])
        print(entero)
        #obteniendo datos del combobox2 (el id de la solicitud)
        dato_seleccionado2 = self.opcionSeleccionada2.get()
        if dato_seleccionado2:
            print(dato_seleccionado2)
        else:
            messagebox.showerror("Campo Vacío", 
                             "Por favor, ingrese texto antes de imprimir.")
        query = "SELECT id_solicitud FROM solicitudes WHERE solicitud = %s"
        cursor.execute(query, (dato_seleccionado2,))
        resultado2 = cursor.fetchall()
        cursor.fetchall()
        conexion.commit()
        mi_tupla2 = tuple(resultado2)
        entero2 = int(mi_tupla2[0][0])
        print(entero2)
        #obteniendo datos del textbox (la cedula)
        texto = self.cedula_texto.get()
        if texto:
            print(texto)
        else:
            messagebox.showerror("Campo Vacío", 
                             "Por favor, ingrese texto antes de imprimir.")
        entero3 = int(texto)
        estudianteint = "INSERT INTO estudiante (cedula) VALUES (%s)"
        cursor.execute(estudianteint, (entero3,))
        conexion.commit()
        
        insertar = "INSERT INTO VinculoSolicitud (id_carrera, id_solicitud, cedula) VALUES (%s, %s, %s)"
        cursor.execute(insertar, (entero, entero2, entero3))
        conexion.commit()
        print("dato insertado")
        messagebox.showinfo("Confirmación", "El dato ha sido ingresado correctamente.")
        conexion.close()
   
if __name__ == "__main__":
    ventana = tk.Tk()
    app = VentanaEstudiante(ventana)
    ventana.mainloop()