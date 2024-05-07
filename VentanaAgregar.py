import tkinter as tk
from tkinter import messagebox
import mysql.connector
from tkinter import ttk
class VentanaAgregar:
    def __init__(self, agregarVentana):
        self.agregarVentana = agregarVentana
        self.agregarVentana.title("INDICA - Agregar nueva solicitud")
        self.agregarVentana.geometry("400x500")
        self.agregarVentana.resizable(width=False, height=False)
        self.agregarVentana.resizable(width=False, height=False)
        self.agregarVentana.configure(background='#ffffff')
        self.coloruniversal="#ff8000"
        self.agregarVentana.iconbitmap("imagenes/icono/icon.ico")
        self.agregarVentana.grab_set()
        def validate_input(new_value):
            if new_value == "":
                return True
            try:
                int(new_value)
                return len(new_value) <= 8
            except ValueError:
                return False

        cs = self.agregarVentana.register(validate_input)  # Registrar la función de validación

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
        solicitudes = [registro[0] for registro in connection]
        query2 = "SELECT carrera FROM subprograma"
        connection.execute(query2)
        subprograma = [registro[0] for registro in connection]
        

        # label text paracedula
        self.titulo = tk.Label(agregarVentana, text="Agregar nueva solicitud", width=20, height=1, font=("Arial", "15","bold"),background="#ffffff")
        self.titulo.pack()
        self.titulo.place(x=75, y=40)

        # label text paracedula
        self.labelcedula = tk.Label(agregarVentana, text="Cedula", width=20, height=1, font=("Arial", "14","bold"),background="#ffffff")
        self.labelcedula.pack()
        self.labelcedula.place(x=70, y=100)
        # textbox de la cedula
        self.cedula_texto = tk.Entry(agregarVentana, width=15,font=("Arial",12),justify=tk.CENTER,validate="key",validatecommand=(cs, "%P"))
        self.cedula_texto.pack()
        self.cedula_texto.place(x=130, y=150)
        #label de la lista subprograma
        self.label1 = tk.Label(agregarVentana, text="Subprograma: ", width=20, height=1,font=("Arial", "14","bold"),background="#ffffff",justify=tk.CENTER)
        self.label1.pack()
        self.label1.place(x=70, y=200)
        #Lista de subprograma
        self.opcionSeleccionada = tk.StringVar()
        self.lista_desplegable = ttk.Combobox(self.agregarVentana, textvariable=self.opcionSeleccionada, state="readonly",width=25, height=10)
        self.lista_desplegable['values'] = subprograma
        self.lista_desplegable.pack()
        self.lista_desplegable.place(x=110, y=250)
        #label de la lista solicitud
        self.label2 = tk.Label(agregarVentana, text="Tipo de solicitud: ",width=20, height=1,font=("Arial", "14","bold"),background="#ffffff")
        self.label2.pack()
        self.label2.place(x=70, y=300)
        #Lista de solicitudess
        self.opcionSeleccionada2 = tk.StringVar()
        self.lista_desplegable2 = ttk.Combobox(self.agregarVentana, textvariable=self.opcionSeleccionada2, state="readonly",width=25, height=10)
        self.lista_desplegable2['values'] = solicitudes
        self.lista_desplegable2.pack()
        self.lista_desplegable2.place(x=110, y=350)
        
        # Boton Agregar
        self.botonAgregar = tk.Button(agregarVentana, text="Agregar", command=self.agregar,width=10, height=1,font=("Arial",12,"bold"),background=self.coloruniversal,fg="white",) 
        self.botonAgregar.pack()  # Colocar el botón en la posición predeterminada
        self.botonAgregar.place(x=150, y=400)

        # Boton Cerrar
        self.botonCerrar = tk.Button(agregarVentana, text="Cerrar", command=self.cerrar_ventana,width=10, height=1,font=("Arial",12,"bold"),background=self.coloruniversal,fg="white",) 
        self.botonCerrar.pack()  # Colocar el botón en la posición predeterminada
        self.botonCerrar.place(x=150, y=450)
        

    def cerrar_ventana(self):
                self.agregarVentana.destroy()
    
    def agregar(self):
        conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="valentin",
        database="indic",
        port="3307"
        )
        cursor = conexion.cursor()

        # Obteniendo Datos del ComboBox (Carrera)
        dato_seleccionado = self.opcionSeleccionada.get()

        # Obteniendo Datos del ComboBox2 (Carrera)
        dato_seleccionado2 = self.opcionSeleccionada2.get()

        # Obteniendo Datos del Textbox (Cedula)
        texto = self.cedula_texto.get()

        """Comprobando que el campo cedula existe, y que los demas no estan vacios."""

        if texto == "" and dato_seleccionado == "" and dato_seleccionado2 == "":
            messagebox.showerror("Error", 
                        "Todos los campos estan vacios.")
        else:
            if texto:
                print("La cedula introducida es: ",texto)
                cursor.execute("SELECT * FROM estudiante WHERE cedula = %s", (texto,))
                resultado = cursor.fetchone()
                print("hola", resultado)
                if resultado:
                    entero3 = int(texto)
                    # estudianteint = "INSERT INTO estudiante (cedula) VALUES (%s)"
                    # cursor.execute(estudianteint, (entero3,))
                    # conexion.commit()
                    if dato_seleccionado == "":
                        messagebox.showerror("Campo Vacío", 
                                            "No se selecciono ninguna carrera. Selecciona una.")
                    else:
                        dato_seleccionado = self.opcionSeleccionada.get()
                        query = "SELECT id_carrera FROM subprograma WHERE carrera = %s"
                        cursor.execute(query, (dato_seleccionado,))
                        resultado = cursor.fetchall()
                        cursor.fetchall()
                        conexion.commit()
                        mi_tupla = tuple(resultado)
                        entero = int(mi_tupla[0][0])
                        print(entero)
                        if dato_seleccionado2 == "":
                                messagebox.showerror("Campo Vacío", 
                                                "No se selecciono ninguna solicitud. Selecciona una.")
                        else:
                            query = "SELECT id_solicitud FROM solicitudes WHERE solicitud = %s"
                            cursor.execute(query, (dato_seleccionado2,))
                            resultado2 = cursor.fetchall()
                            cursor.fetchall()
                            conexion.commit()
                            mi_tupla2 = tuple(resultado2)
                            entero2 = int(mi_tupla2[0][0])
                            print(entero2)
                            insertar = "INSERT INTO VinculoSolicitud (id_carrera, id_solicitud, cedula) VALUES (%s, %s, %s)"
                            cursor.execute(insertar, (entero, entero2, entero3))
                            conexion.commit()
                            print("dato insertado")
                            messagebox.showinfo("Confirmación", "El dato ha sido ingresado correctamente.")
                            conexion.close()
                else:
                    messagebox.showerror("Error", 
                            "La cedula que ingresaste, no se encuentra en el sistema.")
            else:
                messagebox.showerror("Error", 
                            "Debes de ingresar una cedula de identidad.")

if __name__ == "__main__":
    ventana = tk.Tk()
    app = VentanaAgregar(ventana)
    ventana.mainloop()