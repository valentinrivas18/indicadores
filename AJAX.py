import tkinter as tk
from tkinter import filedialog
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generar_pdf():
    # Crea un objeto de canvas para generar el PDF
    c = canvas.Canvas("salida.pdf", pagesize=letter)

    # Agrega contenido al PDF
    c.drawString(100, 750, "¡Hola, mundo!")
    c.save()

    # Pide al usuario que seleccione una ubicación para guardar el PDF
    ruta = filedialog.asksaveasfilename(defaultextension=".pdf")

    # Mueve el archivo generado a la ubicación seleccionada por el usuario
    if ruta:
        archivo = "salida.pdf"
        if archivo and ruta:
            if archivo.endswith(".pdf"):
                archivo_destino = ruta
            else:
                archivo_destino = ruta + ".pdf"
            if archivo != archivo_destino:
                try:
                    archivo_original = open(archivo, "rb")
                    archivo_destino = open(archivo_destino, "wb")
                    archivo_destino.write(archivo_original.read())
                    archivo_original.close()
                    archivo_destino.close()
                    print("Archivo movido exitosamente")
                except Exception as e:
                    print("Error al mover el archivo", str(e))
            else:
                print("El archivo ya está en la ubicación seleccionada")
        else:
            print("No se ha seleccionado una ubicación")

# Crea la ventana principal de Tkinter
root = tk.Tk()

# Crea un botón para generar el PDF
boton = tk.Button(root, text="Generar PDF", command=generar_pdf)
boton.pack()

# Inicia el bucle principal de Tkinter
root.mainloop()