import tkinter as tk
from tkinter import *
from VentanaAgregar import VentanaAgregar
from VentanaBorrar import VentanaBorrar
from VentanaConsulta import *
from VentanaEstudiante import *
from PIL import Image, ImageTk

class VentanaPrincipal:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("INDICADORES")
        self.ventana.geometry("720x450")
        self.ventana.resizable(width=False, height=False)
        self.ventana.configure(background='#ffffff')
        self.coloruniversal="#ff8000"
        self.ventana.iconbitmap("imagenes/icono/icon.ico")
        
        self.bienvenido = tk.Label(self.ventana,font=("Arial", "14","bold"),background="#ffffff",
        text="Programa de Ciencias Basicas y Aplicadas \n \n Generador de Reporte Semestral")
        self.bienvenido.pack()
        self.bienvenido.place(x=185,y=20)

        # -------------------- #
        # imagen del pcba
        self.imagen = Image.open("imagenes/pcba.jpg")
        self.tamano_imagen_deseado = (100, 100)
        self.imagen_redimensionada = self.imagen.resize(self.tamano_imagen_deseado)
        self.tkimagen = ImageTk.PhotoImage(self.imagen_redimensionada)

        # Mostrar la imagen en un Label
        self.label = tk.Label(ventana, image=self.tkimagen, background="#ffffff")
        self.label.pack()
        self.label.place(x=0,y=0)
        # -------------------- #

        # gobierno bolivariano de venezuela
        self.gob = Image.open("imagenes/gobierno.jpg")
        self.gobtamano = (720, 40)
        self.imagenredimi = self.gob.resize(self.gobtamano)
        self.gobimagen = ImageTk.PhotoImage(self.imagenredimi)

        # Mostrar gobierno bolivariano en un Label
        self.labelgobierno = tk.Label(ventana, image=self.gobimagen, background="#ffffff")
        self.labelgobierno.pack()
        self.labelgobierno.place(x=0,y=405)

        # Boton Registrar Estudiante
        self.boton1 = tk.Button(self.ventana, fg="white",text="Registrar", width=15, height=1,
                                font=("Arial", 12,"bold"),background=self.coloruniversal, command=self.abrir_estudiante) 
        self.boton1.pack()  # Colocar el botón en la posicion predeterminada
        self.boton1.place(x=300, y=120)

        # Boton Agregar
        self.boton1 = tk.Button(self.ventana, fg="white",text="Agregar", width=15, height=1,
                                font=("Arial", 12,"bold"),background=self.coloruniversal, command=self.abrir_agregar) 
        self.boton1.pack()  # Colocar el botón en la posicion predeterminada
        self.boton1.place(x=300, y=170)

        # Boton Consulta
        self.boton2 = tk.Button(self.ventana, text="Consulta",background=self.coloruniversal,fg="white", width=15, height=1,font=("Arial", 12,"bold"), command=self.abrir_consulta) 
        self.boton2.pack()  # Colocar el botón en la posicion predeterminada
        self.boton2.place(x=300, y=220)

        # Boton Consulta por subprograma
        # self.boton3 = tk.Button(self.ventana, text="Consulta por Subprograma", width=22, height=1, font=("Arial", 12)) 
        # self.boton3.pack()  # Colocar el botón en la posición predeterminada
        # self.boton3.place(x=445, y=316)

        # Boton de borrar
        self.boton4 = tk.Button(self.ventana,fg="white",background=self.coloruniversal, text="Reiniciar BD", font=("Arial", 12,"bold"), width=15, height=1, command=self.abrir_borrar)
        self.boton4.pack()
        self.boton4.place(x=300,y=270)

        # boton para cerrar ventana
        self.ventana = tk.Button(self.ventana,fg="white",background=self.coloruniversal, text="Cerrar Sesion", font=("Arial", 12,"bold"), width=15, height=1, command=self.cerrarW)
        self.ventana.pack()
        self.ventana.place(x=300,y=320)

    def cerrarW(self):
            self.ventana.destroy()
            exit()

    def abrir_estudiante(self):
         self.ventana_estudiante = tk.Toplevel(self.ventana)
         self.app_estudiante = VentanaEstudiante(self.ventana_estudiante)

    def abrir_borrar(self):
        self.ventana_borrar = tk.Toplevel(self.ventana)
        self.app_borrar = VentanaBorrar(self.ventana_borrar)
        
    def abrir_agregar(self):
        self.ventana_agregar = tk.Toplevel(self.ventana)
        self.app_agregar = VentanaAgregar(self.ventana_agregar)
    
    def abrir_consulta(self):
        self.ventana_consulta = tk.Toplevel(self.ventana)
        self.app_agregar = VentanaConsulta(self.ventana_consulta)

       
if __name__ == "__main__":
    ventana = tk.Tk()
    app = VentanaPrincipal(ventana)
    ventana.protocol("WM_DELETE_WINDOW") 
    ventana.mainloop()