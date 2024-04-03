import tkinter as tk
from tkinter import messagebox
import mysql.connector
from tkinter import ttk
class VentanaAgregar:
    def __init__(self, agregarVentana):
        self.agregarVentana = agregarVentana
        self.agregarVentana.title("Agregar")
        self.agregarVentana.geometry("800x600")
        self.agregarVentana.resizable(width=False, height=False)
        self.agregarVentana.grab_set()

        conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="valentin",
        database="indic",
        port="3307"
        )

        connection = conexion.cursor()

        # Realizar una consulta para obtener los registros del campo deseado
        
        query1 = "SELECT solicitud FROM solicitudes"
        connection.execute(query1)
        registros = [registro[0] for registro in connection]
        
        query2 = "SELECT carrera FROM subprograma"
        connection.execute(query2)
        registros2 = [registro[0] for registro in connection]


        #Lista desplegable1
       
        self.opcionSeleccionada = tk.StringVar()
        self.lista_desplegable = ttk.Combobox(self.agregarVentana, textvariable=self.opcionSeleccionada, state="readonly")
        self.lista_desplegable['values'] = registros2
        self.lista_desplegable.pack()
        self.lista_desplegable.place(x=50, y=60)
        #Lista desplegable2
        self.opcionSeleccionada2 = tk.StringVar()
        self.lista_desplegable2 = ttk.Combobox(self.agregarVentana, textvariable=self.opcionSeleccionada2, state="readonly")
        self.lista_desplegable2['values'] = registros
        self.lista_desplegable2.pack()
        self.lista_desplegable2.place(x=50, y=130)
        #label text lista 1
        self.label1 = tk.Label(agregarVentana, text="Subprograma: ")
        self.label1.pack()
        self.label1.place(x=50, y= 30)
        #label text lista 1
        self.label2 = tk.Label(agregarVentana, text="Tipo de solicitud: ")
        self.label2.pack()
        self.label2.place(x=50, y=100)
        # textbox de la cedula
        self.cedula_texto = tk.Entry(agregarVentana)
        self.cedula_texto.pack()
        self.cedula_texto.place(x=300, y=60)
        # label text paracedula
        self.labelcedula = tk.Label(agregarVentana, text="Cedula")
        self.labelcedula.pack()
        self.labelcedula.place(x=300, y=30)
        # boton para agregar
        # Boton Agregar
        self.botonAgregar = tk.Button(agregarVentana, text="Agregar", command=self.agregar) 
        self.botonAgregar.pack()  # Colocar el botón en la posición predeterminada
        self.botonAgregar.place(x=250, y=200)
        
        
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
        entero3 = int(texto)
        
        estudianteint = "INSERT INTO estudiante (cedula) VALUES (%s)"
        cursor.execute(estudianteint, (entero3,))
        conexion.commit()
        
        insertar = "INSERT INTO VinculoSolicitud (id_carrera, id_solicitud, cedula) VALUES (%s, %s, %s)"
        cursor.execute(insertar, (entero, entero2, entero3))
        conexion.commit()
        print("dato insertado")
        messagebox.showinfo("Confirmación", "El dato ha sido ingresado correctamente.")
        
   
        
if __name__ == "__main__":
    ventana = tk.Tk()
    app = VentanaAgregar(ventana)
    ventana.mainloop()