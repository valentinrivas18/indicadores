import mysql.connector
import datetime
from reportlab.platypus import Table, TableStyle
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from conx import solicitudesDB

"""Conexion a la base de datos"""
db = solicitudesDB("localhost", "root", "valentin", "indic", "3307")
db.conectar()
"""Solicitudes para Ingenieria en Informatica"""
total = db.TotalSCarrera(101)
carrera = "SUBPROGRAMA: " + db.NombreCarrera(101)
SoliPorCarr = db.TotalSoliPorCarr(101, 1)
NDS = db.NombreDeSolis()
"""Aqui se saca el porcentaje"""
def porcentaje(x):
    x = ((x * 100) / total)
    vv = float("{:.2f}".format(x))
    return vv
#Elementos para ser insertados en la tabla en su respectivo orden#
x = ['CDTS', 'SP', 'AR','PDTI', 'AE','CS','EUC','IE','ADN','LP']
fila1 = [ [x[0],NDS[0][0],db.TotalSoliPorCarr(101, 1), porcentaje(db.TotalSoliPorCarr(101, 1))],
          [x[1],NDS[1][0],db.TotalSoliPorCarr(101, 2), porcentaje(db.TotalSoliPorCarr(101, 2))],
          [x[2],NDS[2][0],db.TotalSoliPorCarr(101, 3), porcentaje(db.TotalSoliPorCarr(101, 3))],
          [x[3],NDS[3][0],db.TotalSoliPorCarr(101, 4), porcentaje(db.TotalSoliPorCarr(101, 4))],
          [x[4],NDS[4][0],db.TotalSoliPorCarr(101, 5), porcentaje(db.TotalSoliPorCarr(101, 5))],
          [x[5],NDS[5][0],db.TotalSoliPorCarr(101, 6), porcentaje(db.TotalSoliPorCarr(101, 6))],
          [x[6],NDS[6][0],db.TotalSoliPorCarr(101, 7), porcentaje(db.TotalSoliPorCarr(101, 7))],
          [x[7],NDS[7][0],db.TotalSoliPorCarr(101, 8), porcentaje(db.TotalSoliPorCarr(101, 8))],
          [x[8],NDS[8][0],db.TotalSoliPorCarr(101, 9), porcentaje(db.TotalSoliPorCarr(101, 9))],
          [x[9],NDS[9][0],db.TotalSoliPorCarr(101, 10), porcentaje(db.TotalSoliPorCarr(101, 10))],
          ["N/A", "TOTAL", total]
            ]
"""Este fragmento de codigo sirver sirve para sumar el porcentaje total de
    las solicitudes del subprograma"""
prueba = []
for i in range(0,len(fila1)-1):
    UE = fila1[i][-1]
    prueba.append(UE)
obj = sum(prueba)
fila1[len(fila1)-1].append(obj)


"""Estas dos lineas de codigo sirven para que el pdf generado tenga como nombre la fecha y hora en la que se genero"""
FA = datetime.datetime.now()
FechaPDF = FA.strftime("Fecha: "+"%d/%m/%Y")
FF = FA.strftime("REPORTE-"+"%Iy%M"+"%p-"+"%Y%m%d"+".pdf")

c = canvas.Canvas("prueba.pdf", pagesize=letter)

encabezados = [['ID', 'Solicitud', "Cantidad", "Porcentaje"]]
tabla = Table(encabezados + fila1)

tabla.setStyle(TableStyle([
('GRID', (0, 0), (-1, -1), 1, colors.black),
('BOX', (0, 0), (-1, -1), 1, colors.black)
]))

tabla.wrapOn(c, 1, 1)  # Ancho y alto de la tabla
tabla.drawOn(c, 150, 395)   # Posición (x, y) de la tabla en el canvas
c.drawImage("pcba.jpg", 420, 680, width=100, height=100)
c.drawImage("unellez.jpg", 80, 685, width=70, height=80)
c.drawImage("gobierno.jpg", 180, 720, width=250, height=30)
c.drawString(160, 690, FechaPDF)
c.drawString(160, 660, "Programa de Ciencias Basicas y Aplicadas")
c.drawString(150, 620, carrera)
# c.drawImage("uno.jpg", 110, 100, width=370, height=270)
c.drawString(250,350, "Descripcion Grafica")
c.showPage()


# Ingenieria en tal
c.drawString(250,350, "Descripcion Grafica")
c.showPage()



# Guardar el documento PDF
c.save()