from reportlab.platypus import Table, TableStyle
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from clase import *


"""En esta parte es donde se empieza a formar el pdf como tal, todo lo que hay anterior a esto son las variables que van a
a ser incluidas en el pdf, nombre de la carrera, subprograma."""

c = canvas.Canvas("prueba.pdf", pagesize=letter)

"""ING Informatica"""

tablai.setStyle(TableStyle([
('GRID', (0, 0), (-1, -1), 1, colors.black),
('BOX', (0, 0), (-1, -1), 1, colors.black)
]))

tablai.wrapOn(c, 1, 1)  # Ancho y alto de la tabla
tablai.drawOn(c, 150, 395)   # Posición (x, y) de la tabla en el canvas
c.drawImage("pcba.jpg", 420, 680, width=100, height=100)
c.drawImage("unellez.jpg", 80, 685, width=70, height=80)
c.drawImage("gobierno.jpg", 180, 720, width=250, height=30)
c.drawString(160, 690, fechadi)
c.drawString(160, 660, "Programa de Ciencias Basicas y Aplicadas")
c.drawString(150, 620, msjcarrerai)
# c.drawImage("uno.jpg", 110, 100, width=370, height=270)
c.drawString(250,350, "Descripcion Grafica")
c.showPage()

"""ING Petroleo"""
tablap.setStyle(TableStyle([
('GRID', (0, 0), (-1, -1), 1, colors.black),
('BOX', (0, 0), (-1, -1), 1, colors.black)
]))

tablap.wrapOn(c, 1, 1)  # Ancho y alto de la tabla
tablap.drawOn(c, 150, 395)   # Posición (x, y) de la tabla en el canvas
c.drawImage("pcba.jpg", 420, 680, width=100, height=100)
c.drawImage("unellez.jpg", 80, 685, width=70, height=80)
c.drawImage("gobierno.jpg", 180, 720, width=250, height=30)
c.drawString(160, 690, fechadp)
c.drawString(160, 660, "Programa de Ciencias Basicas y Aplicadas")
c.drawString(150, 620, msjcarrerap)
# c.drawImage("uno.jpg", 110, 100, width=370, height=270)
c.drawString(250,350, "Descripcion Grafica")
c.showPage()

"""ING Minas"""
tablam.setStyle(TableStyle([
('GRID', (0, 0), (-1, -1), 1, colors.black),
('BOX', (0, 0), (-1, -1), 1, colors.black)
]))

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

tablatI.wrapOn(c, 1, 1)  # Ancho y alto de la tabla
tablatI.drawOn(c, 150, 395)   # Posición (x, y) de la tabla en el canvas
c.drawImage("pcba.jpg", 420, 680, width=100, height=100)
c.drawImage("unellez.jpg", 80, 685, width=70, height=80)
c.drawImage("gobierno.jpg", 180, 720, width=250, height=30)
c.drawString(160, 690, fechadtI)
c.drawString(160, 660, "Programa de Ciencias Basicas y Aplicadas")
c.drawString(150, 620, msjcarreratI)
# c.drawImage("uno.jpg", 110, 100, width=370, height=270)
c.drawString(250,350, "Descripcion Grafica")
c.showPage()

c.save()

