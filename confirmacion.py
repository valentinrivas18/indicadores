import tkinter as tk
from tkinter import messagebox

def confirmar_operacion():
    respuesta = messagebox.askyesno("Confirmación", "¿Desea realizar la operación?")
    if respuesta:
        # Realiza la operación
        print("Operación realizada")
    else:
        # No realiza la operación
        print("Operación cancelada")

root = tk.Tk()
boton = tk.Button(root, text="Realizar operación", command=confirmar_operacion)
boton.pack()

root.mainloop()