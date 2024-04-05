from reportlab.platypus import Table, TableStyle
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib import colors
import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="valentin",
    database="indic",
    port="3307"
    )

cursor = conexion.cursor()
query1 = "SELECT * FROM solicitudes"
cursor.execute(query1)
resultado = cursor.fetchall()
resultado = list(resultado)
resultado1 = [list(tup) for tup in resultado]

query2 = "SELECT COUNT(*) as total from solicitudes"
cursor.execute(query2)
total = cursor.fetchall()
total_ent = [int(x) for tup in total for x in tup]
t = int(total_ent[0])
print(t)

rango = [num for num in range (0,t)]
filas =[]
for i in resultado1:
    for j in rango:
            filas.append(resultado1[j])
filasn = list(set(map(tuple, filas)))
print(filasn)

encabezados = [['ID', 'Solicitud', "Cantidad", "Porcentaje"]]
filas = [resultado1[0],resultado1[1]]

tabla = Table(encabezados + filas)
# Agregar bordes a la tabla
tabla.setStyle(TableStyle([
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ('BOX', (0, 0), (-1, -1), 1, colors.black)
]))
doc = SimpleDocTemplate("table.pdf", pagesize=letter)
doc.build([tabla])