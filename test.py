import tkinter as tk

# Función para mostrar un mensaje con los datos del campo de texto
def mostrar_mensaje():
    dato = campo_texto.get()
    mensaje = "Los datos ingresados son: " + dato
    etiqueta_mensaje.config(text=mensaje)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Mostrar Mensaje")

# Campo de texto para ingresar datos
campo_texto = tk.Entry(ventana)
campo_texto.pack()

# Botón que al hacer clic muestra el mensaje con los datos ingresados
boton_mostrar = tk.Button(ventana, text="Mostrar Mensaje", command=mostrar_mensaje)
boton_mostrar.pack()

# Etiqueta para mostrar el mensaje
etiqueta_mensaje = tk.Label(ventana, text="")
etiqueta_mensaje.pack()

# Ejecutar el bucle principal de la ventana
ventana.mainloop()