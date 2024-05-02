import tkinter as tk
from tkinter import *
from crearventanas import agregar,consultar,consultargeneral,antds
from PIL import Image, ImageTk
from logo import *

# Crear la ventana
ventana = tk.Tk()
ventana.title("INDICADORES")
ventana.geometry("1024x768")
ventana.resizable(width=False, height=False)
ventana.iconbitmap("icon.ico")

img_tk = logopcba("pcba.png")
# mostrar la imagen
label_imagen = tk.Label(ventana, image=img_tk)
label_imagen.image = img_tk
label_imagen.config(image=img_tk)
label_imagen.place(x=0, y=0)

# Boton Agregar
boton1 = tk.Button(ventana, text="Agregar", width=10, height=1, font=("Arial", 12), command=agregar) 
boton1.pack()  # Colocar el botón en la posición predeterminada
boton1.place(x=500, y=184)

# Boton Consulta

boton2 = tk.Button(ventana, text="Consulta", width=15, height=1, font=("Arial", 12), command=consultargeneral) 
boton2.pack()  # Colocar el botón en la posición predeterminada
boton2.place(x=475, y=250)

# Boton Consulta por subprograma

boton3 = tk.Button(ventana, text="Consulta por Subprograma", width=22, height=1, font=("Arial", 12), command=consultar) 
boton3.pack()  # Colocar el botón en la posición predeterminada
boton3.place(x=445, y=316)

# Boton de agregar nuevo tipo de solicitud

boton4 = tk.Button(ventana, text="ANTDS", font=("Arial", 12), command=antds)
boton4.pack()
boton4.place(x=510,y=380)


ventana.mainloop()