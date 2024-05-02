from reportlab.platypus import Table, TableStyle
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib import colors
from reportlab.pdfgen import canvas
import matplotlib.pyplot as plt
from clase import *
from tkinter import filedialog
from tkinter import messagebox

x = ['CDTS', 'SP', 'AR','PDTI', 'AE','CS','EUC','IE','ADN','LP']

class generador:
    def __init__(self):
        pass
    def pdfs(self):
        """En esta parte es donde se empieza a formar el pdf como tal, todo lo que hay anterior a esto son las variables que van a
        a ser incluidas en el pdf, nombre de la carrera, subprograma."""

        c = canvas.Canvas("prueba.pdf", pagesize=letter)

        """ING Informatica"""

        tablai.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BOX', (0, 0), (-1, -1), 1, colors.black)
        ]))

        
        plt.figure()
        ingi = plt.bar(x, graficoi)
        plt.savefig("101.jpg")
        c.drawImage("101.jpg", 110, 100, width=370, height=270)


        tablai.wrapOn(c, 1, 1)  # Ancho y alto de la tabla
        tablai.drawOn(c, 150, 395)   # Posición (x, y) de la tabla en el canvas
        c.drawImage("pcba.jpg", 420, 680, width=100, height=100)
        c.drawImage("unellez.jpg", 80, 685, width=70, height=80)
        c.drawImage("gobierno.jpg", 180, 720, width=250, height=30)
        c.drawString(160, 690, fechadi)
        c.drawString(160, 660, "Programa de Ciencias Basicas y Aplicadas")
        c.drawString(150, 620, msjcarrerai)
        c.drawString(250,350, "Descripcion Grafica")
        c.showPage()

        """ING Petroleo"""
        tablap.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BOX', (0, 0), (-1, -1), 1, colors.black)
        ]))
        plt.figure()
        plt.bar(x, graficop)
        # Etiquetas de los ejes
        plt.xlabel('Solicitudes')
        plt.ylabel('Porcentaje')
        plt.savefig("102.jpg")
        c.drawImage("102.jpg", 110, 100, width=370, height=270)
        tablap.wrapOn(c, 1, 1)  # Ancho y alto de la tabla
        tablap.drawOn(c, 150, 395)   # Posición (x, y) de la tabla en el canvas
        c.drawImage("pcba.jpg", 420, 680, width=100, height=100)
        c.drawImage("unellez.jpg", 80, 685, width=70, height=80)
        c.drawImage("gobierno.jpg", 180, 720, width=250, height=30)
        c.drawString(160, 690, fechadp)
        c.drawString(160, 660, "Programa de Ciencias Basicas y Aplicadas")
        c.drawString(150, 620, msjcarrerap)
        c.drawString(250,350, "Descripcion Grafica")
        c.showPage()

        """ING Minas"""
        tablam.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BOX', (0, 0), (-1, -1), 1, colors.black)
        ]))
        plt.figure()
        plt.bar(x, graficom)
        # Etiquetas de los ejes
        plt.xlabel('Solicitudes')
        plt.ylabel('Porcentaje')
        plt.savefig("103.jpg")
        c.drawImage("103.jpg", 110, 100, width=370, height=270)
        tablam.wrapOn(c, 1, 1)  # Ancho y alto de la tabla
        tablam.drawOn(c, 150, 395)   # Posición (x, y) de la tabla en el canvas
        c.drawImage("pcba.jpg", 420, 680, width=100, height=100)
        c.drawImage("unellez.jpg", 80, 685, width=70, height=80)
        c.drawImage("gobierno.jpg", 180, 720, width=250, height=30)
        c.drawString(160, 690, fechadm)
        c.drawString(160, 660, "Programa de Ciencias Basicas y Aplicadas")
        c.drawString(150, 620, msjcarreram)
        # c.drawImage("uno.jpg", 110, 100, width=370, height=270)
        c.drawString(250,350, "Descripcion Grafica")
        c.showPage()

        """ING Civil"""
        tablac.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BOX', (0, 0), (-1, -1), 1, colors.black)
        ]))
        plt.figure()
        plt.bar(x, graficoc)
        # Etiquetas de los ejes
        plt.xlabel('Solicitudes')
        plt.ylabel('Porcentaje')
        plt.savefig("104.jpg")
        c.drawImage("104.jpg", 110, 100, width=370, height=270)
        tablac.wrapOn(c, 1, 1)  # Ancho y alto de la tabla
        tablac.drawOn(c, 150, 395)   # Posición (x, y) de la tabla en el canvas
        c.drawImage("pcba.jpg", 420, 680, width=100, height=100)
        c.drawImage("unellez.jpg", 80, 685, width=70, height=80)
        c.drawImage("gobierno.jpg", 180, 720, width=250, height=30)
        c.drawString(160, 690, fechadc)
        c.drawString(160, 660, "Programa de Ciencias Basicas y Aplicadas")
        c.drawString(150, 620, msjcarrerac)
        # c.drawImage("uno.jpg", 110, 100, width=370, height=270)
        c.drawString(250,350, "Descripcion Grafica")
        c.showPage()

        """Lic Meteorologia"""
        tablalm.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BOX', (0, 0), (-1, -1), 1, colors.black)
        ]))
        plt.figure()
        plt.bar(x, graficolm)

        plt.xlabel('Solicitudes')
        plt.ylabel('Porcentaje')
        plt.savefig("105.jpg")
        c.drawImage("105.jpg", 110, 100, width=370, height=270)

        tablalm.wrapOn(c, 1, 1)  # Ancho y alto de la tabla
        tablalm.drawOn(c, 150, 395)   # Posición (x, y) de la tabla en el canvas
        c.drawImage("pcba.jpg", 420, 680, width=100, height=100)
        c.drawImage("unellez.jpg", 80, 685, width=70, height=80)
        c.drawImage("gobierno.jpg", 180, 720, width=250, height=30)
        c.drawString(160, 690, fechadlm)
        c.drawString(160, 660, "Programa de Ciencias Basicas y Aplicadas")
        c.drawString(150, 620, msjcarreralm)
        # c.drawImage("uno.jpg", 110, 100, width=370, height=270)
        c.drawString(250,350, "Descripcion Grafica")
        c.showPage()

        """Arquitectura"""
        tablaA.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BOX', (0, 0), (-1, -1), 1, colors.black)
        ]))
        plt.figure()
        plt.bar(x, graficoA)
        plt.xlabel('Solicitudes')
        plt.ylabel('Porcentaje')
        plt.savefig("106.jpg")
        c.drawImage("106.jpg", 110, 100, width=370, height=270)
        tablaA.wrapOn(c, 1, 1)  # Ancho y alto de la tabla
        tablaA.drawOn(c, 150, 395)   # Posición (x, y) de la tabla en el canvas
        c.drawImage("pcba.jpg", 420, 680, width=100, height=100)
        c.drawImage("unellez.jpg", 80, 685, width=70, height=80)
        c.drawImage("gobierno.jpg", 180, 720, width=250, height=30)
        c.drawString(160, 690, fechadA)
        c.drawString(160, 660, "Programa de Ciencias Basicas y Aplicadas")
        c.drawString(150, 620, msjcarreraA)
        # c.drawImage("uno.jpg", 110, 100, width=370, height=270)
        c.drawString(250,350, "Descripcion Grafica")
        c.showPage()

        """tsu topografica"""
        tablatT.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BOX', (0, 0), (-1, -1), 1, colors.black)
        ]))
        plt.figure()
        plt.bar(x, graficotT)
        plt.xlabel('Solicitudes')
        plt.ylabel('Porcentaje')
        plt.savefig("107.jpg")
        c.drawImage("107.jpg", 110, 100, width=370, height=270)
        tablatT.wrapOn(c, 1, 1)  # Ancho y alto de la tabla
        tablatT.drawOn(c, 150, 395)   # Posición (x, y) de la tabla en el canvas
        c.drawImage("pcba.jpg", 420, 680, width=100, height=100)
        c.drawImage("unellez.jpg", 80, 685, width=70, height=80)
        c.drawImage("gobierno.jpg", 180, 720, width=250, height=30)
        c.drawString(160, 690, fechadtT)
        c.drawString(160, 660, "Programa de Ciencias Basicas y Aplicadas")
        c.drawString(150, 620, msjcarreratT)
        # c.drawImage("uno.jpg", 110, 100, width=370, height=270)
        c.drawString(250,350, "Descripcion Grafica")
        c.showPage()

        """Tsu construccion civil"""
        tablatC.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BOX', (0, 0), (-1, -1), 1, colors.black)
        ]))
        plt.figure()
        plt.bar(x, graficotC)
        plt.xlabel('Solicitudes')
        plt.ylabel('Porcentaje')
        plt.savefig("108.jpg")
        c.drawImage("108.jpg", 110, 100, width=370, height=270)
        tablatC.wrapOn(c, 1, 1)  # Ancho y alto de la tabla
        tablatC.drawOn(c, 150, 395)   # Posición (x, y) de la tabla en el canvas
        c.drawImage("pcba.jpg", 420, 680, width=100, height=100)
        c.drawImage("unellez.jpg", 80, 685, width=70, height=80)
        c.drawImage("gobierno.jpg", 180, 720, width=250, height=30)
        c.drawString(160, 690, fechadtC)
        c.drawString(160, 660, "Programa de Ciencias Basicas y Aplicadas")
        c.drawString(150, 620, msjcarreratC)
        # c.drawImage("uno.jpg", 110, 100, width=370, height=270)
        c.drawString(250,350, "Descripcion Grafica")
        c.showPage()# Guardar el documento PDF

        """tsu informatica"""
        tablatI.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BOX', (0, 0), (-1, -1), 1, colors.black)
        ]))
        plt.figure()
        plt.bar(x, graficotI)
        # Etiquetas de los ejes
        plt.xlabel('Solicitudes')
        plt.ylabel('Porcentaje')
        plt.savefig("tsuinformatica.jpg")
        c.drawImage("tsuinformatica.jpg", 110, 100, width=370, height=270)

        tablatI.wrapOn(c, 1, 1)  # Ancho y alto de la tabla
        tablatI.drawOn(c, 150, 395)   # Posición (x, y) de la tabla en el canvas
        c.drawImage("pcba.jpg", 420, 680, width=100, height=100)
        c.drawImage("unellez.jpg", 80, 685, width=70, height=80)
        c.drawImage("gobierno.jpg", 180, 720, width=250, height=30)
        c.drawString(160, 690, fechadtI)
        c.drawString(160, 660, "Programa de Ciencias Basicas y Aplicadas")
        c.drawString(150, 620, msjcarreratI)
        c.drawString(250,350, "Descripcion Grafica")
        c.showPage()

        c.save()
        ruta = filedialog.asksaveasfilename(defaultextension=".pdf")

        # Mueve el archivo generado a la ubicación seleccionada por el usuario
        if ruta:
            archivo = "prueba.pdf"
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
                        messagebox.showinfo("Notificacion", "El archivo se ha guardado exitosamente")
                    except Exception as e:
                        print("Error al mover el archivo", str(e))
                        messagebox.showinfo("Notificacion", "Error al mover el archivo")
                else:
                    print("El archivo ya está en la ubicación seleccionada")
            else:
                print("No se ha seleccionado una ubicación")
        