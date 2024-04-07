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

query2 = "SELECT COUNT(*) as total from VinculoSolicitud WHERE id_carrera = 101"
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
print(fs1)

f2 = "Select COUNT(*) from VinculoSolicitud WHERE id_carrera = 101 and id_solicitud = 2;"
cursor.execute(f2)
ff2 = cursor.fetchall()
fs2 = list(ff2[0])
print(fs2)

f3 = "Select COUNT(*) from VinculoSolicitud WHERE id_carrera = 101 and id_solicitud = 3;"
cursor.execute(f3)
ff3 = cursor.fetchall()
fs3 = list(ff3[0])
print(fs3)

f4 = "Select COUNT(*) from VinculoSolicitud WHERE id_carrera = 101 and id_solicitud = 4;"
cursor.execute(f4)
ff4 = cursor.fetchall()
fs4 = list(ff4[0])
print(fs4)

f5 = "Select COUNT(*) from VinculoSolicitud WHERE id_carrera = 101 and id_solicitud = 5;"
cursor.execute(f5)
ff5 = cursor.fetchall()
fs5 = list(ff5[0])
print(fs5)

f6 = "Select COUNT(*) from VinculoSolicitud WHERE id_carrera = 101 and id_solicitud = 6;"
cursor.execute(f6)
ff6 = cursor.fetchall()
fs6 = list(ff6[0])
print(fs6)

f7 = "Select COUNT(*) from VinculoSolicitud WHERE id_carrera = 101 and id_solicitud = 7;"
cursor.execute(f7)
ff7 = cursor.fetchall()
fs7 = list(ff7[0])
print(fs7)

f8 = "Select COUNT(*) from VinculoSolicitud WHERE id_carrera = 101 and id_solicitud = 8;"
cursor.execute(f8)
ff8 = cursor.fetchall()
fs8 = list(ff8[0])
print(fs8)

f9 = "Select COUNT(*) from VinculoSolicitud WHERE id_carrera = 101 and id_solicitud = 9;"
cursor.execute(f9)
ff9 = cursor.fetchall()
fs9 = list(ff9[0])
print(fs9)

f10 = "Select COUNT(*) from VinculoSolicitud WHERE id_carrera = 101 and id_solicitud = 10;"
cursor.execute(f10)
ff10 = cursor.fetchall()
fs10 = list(ff10[0])
print(fs10)


encabezados = [['ID', 'Solicitud', "Cantidad", "Porcentaje"]]
filas = [resultado1[0]+fs1,
         resultado1[1]+fs2,
         resultado1[2]+fs3,
         resultado1[3]+fs4,
         resultado1[4]+fs5,
         resultado1[5]+fs6,
         resultado1[6]+fs7,
         resultado1[7]+fs8,
         resultado1[8]+fs9,
         resultado1[9]+fs10,]

tabla = Table(encabezados + filas)
# Agregar bordes a la tabla
tabla.setStyle(TableStyle([
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ('BOX', (0, 0), (-1, -1), 1, colors.black)
]))
doc = SimpleDocTemplate("table.pdf", pagesize=letter)
doc.build([tabla])