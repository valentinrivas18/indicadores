import mysql.connector
import tkinter as tk
from tkinter import *

# Crear la interfaz gráfica con Tkinter
root = tk.Tk()
root.geometry("300x200")
root.title("Registros en Lista Desplegable")

registros = ["hola", "1", "2", "5"]

# Crear la lista desplegable y cargar los registros
variable = StringVar(root)
variable.set(registros[0])  # Valor por defecto

dropdown = OptionMenu(root, variable, *registros)
dropdown.pack()

root.mainloop()