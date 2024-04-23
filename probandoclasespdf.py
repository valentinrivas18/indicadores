from reportlab.platypus import Table, TableStyle
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from clase import *


"""En esta parte es donde se empieza a formar el pdf como tal, todo lo que hay anterior a esto son las variables que van a
a ser incluidas en el pdf, nombre de la carrera, subprograma."""

c = canvas.Canvas("prueba.pdf", pagesize=letter)

class carreraPlantila:
    def __init__(self,tabla,mensaje,fecha):
        self.tabla = tabla
        self.mensaje = mensaje
        self.fecha = fecha
    def plantillareal(self):
        self.instancia.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BOX', (0, 0), (-1, -1), 1, colors.black)
        ]))

        self.instancia.wrapOn(c, 1, 1)  # Ancho y alto de la tabla
        self.instancia.drawOn(c, 150, 395)   # Posición (x, y) de la tabla en el canvas
        c.drawImage("pcba.jpg", 420, 680, width=100, height=100)
        c.drawImage("unellez.jpg", 80, 685, width=70, height=80)
        c.drawImage("gobierno.jpg", 180, 720, width=250, height=30)
        c.drawString(160, 690, self.instancia)
        c.drawString(160, 660, "Programa de Ciencias Basicas y Aplicadas")
        c.drawString(150, 620, self.instancia)
        # c.drawImage("uno.jpg", 110, 100, width=370, height=270)
        c.drawString(250,350, "Descripcion Grafica")
        c.showPage()