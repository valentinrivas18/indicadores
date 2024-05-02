import tkinter as tk
from tkinter import ttk
from main import *


# Ventana "Agregar"
def agregar():
    agregarVentana =  tk.Toplevel()
    agregarVentana.title("Agregar")
    agregarVentana.geometry("800x600")
    agregarVentana.resizable(width=False, height=False)
    agregarVentana.grab_set()
    agregarVentana.iconbitmap("icon.ico")


    ## opciones
    opciones = ["opcion1", "opcion2", "opcion3"]
    opciones2 = ["listta2", "lista3", "lista4"]
    #Lista desplegable1
    
    opcionSeleccionada = tk.StringVar()
    lista_desplegable = ttk.Combobox(agregarVentana, textvariable=opcionSeleccionada, state="readonly")
    lista_desplegable['values'] = opciones
    lista_desplegable.pack()
    lista_desplegable.place(x=50, y=60)
    #Lista desplegable2
    opcionSeleccionada2 = tk.StringVar()
    lista_desplegable2 = ttk.Combobox(agregarVentana, textvariable=opcionSeleccionada2, state="readonly")
    lista_desplegable2['values'] = opciones2
    lista_desplegable2.pack()
    lista_desplegable2.place(x=50, y=130)
    #label text lista 1
    label1 = tk.Label(agregarVentana, text="Subprograma: ")
    label1.pack()
    label1.place(x=50, y= 30)
    #label text lista 1
    label2 = tk.Label(agregarVentana, text="Tipo de solicitud: ")
    label2.pack()
    label2.place(x=50, y=100)
    # textbox de la cedula
    cedula_texto = tk.Entry(agregarVentana)
    cedula_texto.pack()
    cedula_texto.place(x=300, y=60)
    # label text paracedula
    labelcedula = tk.Label(agregarVentana, text="Cedula")
    labelcedula.pack()
    labelcedula.place(x=300, y=30)
    # boton para agregar
    # Boton Agregar
    botonAgregar = tk.Button(agregarVentana, text="Agregar") 
    botonAgregar.pack()  # Colocar el botón en la posición predeterminada
    botonAgregar.place(x=250, y=200)



# Ventana "Consultar"
def consultar():
    consultarVentana =  tk.Toplevel()
    consultarVentana.title("Consulta Individual")
    consultarVentana.geometry("800x600")
    consultarVentana.resizable(width=False, height=False)
    consultarVentana.grab_set()
    consultarVentana.iconbitmap("icon.ico")

def consultargeneral():
    consultargVentana = tk.Toplevel()
    consultargVentana.title("Consulta General")
    consultargVentana.geometry("800x600")
    consultargVentana.resizable(width=False, height=False)
    consultargVentana.grab_set()
    consultargVentana.iconbitmap("icon.ico")



def antds():
    antdsVentana = tk.Toplevel()
    antdsVentana.title ("Agregar nuevo tipo de solicitud")
    antdsVentana.geometry("800x600")
    antdsVentana.resizable(width=False, height=False)
    antdsVentana.grab_set()
    antdsVentana.iconbitmap("icon.ico")
    # text box para solicitud
    solic_texto = tk.Entry(antdsVentana)
    solic_texto.pack()
    solic_texto.place(x=300, y=130)
    # label text para solicitud
    labelsolic = tk.Label(antdsVentana, text="Solicitud")
    labelsolic.pack()
    labelsolic.place(x=300, y=100)
    # titulo
    labeltitulo = tk.Label(antdsVentana, text="Agregar nuevo tipo de soliciutd", font=("Arial", 18))
    labeltitulo.pack()
    labeltitulo.place(x=250, y=50)
    # buton agregar soli
    botonsoli = tk.Button(antdsVentana, text="Agregar")
    botonsoli.pack()  # Colocar el botón en la posición predeterminada
    botonsoli.place(x=280, y=170)
    obtener = solic_texto.get()
    return obtener
    


    