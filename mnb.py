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

query2 = "SELECT COUNT(*) from VinculoSolicitud WHERE id_carrera = 101"
cursor.execute(query2)
total = cursor.fetchall()
total_ent = [int(x) for tup in total for x in tup]
t = int(total_ent[0])
print(t)

## En esta seccion se consulta el numero de solicitudes de la solicitud

f1 = "Select COUNT(*) from VinculoSolicitud WHERE id_carrera = 101 and id_solicitud = 1;"
cursor.execute(f1)
ff1 = cursor.fetchall()
fs1 = list(ff1[0])


f2 = "Select COUNT(*) from VinculoSolicitud WHERE id_carrera = 101 and id_solicitud = 2;"
cursor.execute(f2)
ff2 = cursor.fetchall()
fs2 = list(ff2[0])


f3 = "Select COUNT(*) from VinculoSolicitud WHERE id_carrera = 101 and id_solicitud = 3;"
cursor.execute(f3)
ff3 = cursor.fetchall()
fs3 = list(ff3[0])


f4 = "Select COUNT(*) from VinculoSolicitud WHERE id_carrera = 101 and id_solicitud = 4;"
cursor.execute(f4)
ff4 = cursor.fetchall()
fs4 = list(ff4[0])


f5 = "Select COUNT(*) from VinculoSolicitud WHERE id_carrera = 101 and id_solicitud = 5;"
cursor.execute(f5)
ff5 = cursor.fetchall()
fs5 = list(ff5[0])


f6 = "Select COUNT(*) from VinculoSolicitud WHERE id_carrera = 101 and id_solicitud = 6;"
cursor.execute(f6)
ff6 = cursor.fetchall()
fs6 = list(ff6[0])


f7 = "Select COUNT(*) from VinculoSolicitud WHERE id_carrera = 101 and id_solicitud = 7;"
cursor.execute(f7)
ff7 = cursor.fetchall()
fs7 = list(ff7[0])

f8 = "Select COUNT(*) from VinculoSolicitud WHERE id_carrera = 101 and id_solicitud = 8;"
cursor.execute(f8)
ff8 = cursor.fetchall()
fs8 = list(ff8[0])

f9 = "Select COUNT(*) from VinculoSolicitud WHERE id_carrera = 101 and id_solicitud = 9;"
cursor.execute(f9)
ff9 = cursor.fetchall()
fs9 = list(ff9[0])


f10 = "Select COUNT(*) from VinculoSolicitud WHERE id_carrera = 101 and id_solicitud = 10;"
cursor.execute(f10)
ff10 = cursor.fetchall()
fs10 = list(ff10[0])

def porcentaje(x):
    v = x[0] / t
    vv = float("{:.2f}".format(v))
    l = []
    l.append(vv)
    return l

fila1 = resultado1[0]+fs1+porcentaje(fs1)
fila2 = resultado1[1]+fs2+porcentaje(fs2)
fila3 = resultado1[2]+fs3+porcentaje(fs3)
fila4 = resultado1[3]+fs4+porcentaje(fs4)
fila5 = resultado1[4]+fs5+porcentaje(fs5)
fila6 = resultado1[5]+fs6+porcentaje(fs6)
fila7 = resultado1[6]+fs7+porcentaje(fs7)
fila8 = resultado1[7]+fs8+porcentaje(fs8)
fila9 = resultado1[8]+fs9+porcentaje(fs9)
fila10 = resultado1[9]+fs10+porcentaje(fs10)

print(fila1)


encabezados = [['ID', 'Solicitud', "Cantidad", "Porcentaje"]]
filas = [fila1,
         fila2,
         fila3,
         fila4,
         fila5,
         fila6,
         fila7,
         fila8,
         fila9,
         fila10]

tabla = Table(encabezados + filas)
# Agregar bordes a la tabla
tabla.setStyle(TableStyle([
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ('BOX', (0, 0), (-1, -1), 1, colors.black)
]))
doc = SimpleDocTemplate("table.pdf", pagesize=letter)
doc.build([tabla])