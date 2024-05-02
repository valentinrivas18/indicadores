import tkinter as tk
from tkinter import messagebox

# Función asociada al botón para imprimir el texto del cuadro de texto
def imprimir_texto():
    texto = entrada.get()
    if texto:
        print(texto)
    else:
        messagebox.showerror("Campo Vacío", 
                             "Por favor, ingrese texto antes de imprimir.")
    print(texto)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ejemplo de Text Box y Botón")

# Crear el cuadro de texto
entrada = tk.Entry(ventana)
entrada.pack()

# Crear el botón
boton = tk.Button(ventana, text="Imprimir Texto", command=imprimir_texto)
boton.pack()

# Ejecutar la aplicación
ventana.mainloop()