import matplotlib.pyplot as plt
import io
import mysql.connector
from reportlab.platypus import Table, TableStyle
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib import colors
from reportlab.pdfgen import canvas

def page3():
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

    query2 = "SELECT COUNT(*) from VinculoSolicitud WHERE id_carrera = 103"
    cursor.execute(query2)
    total = cursor.fetchall()
    total_ent = [int(x) for tup in total for x in tup]
    t = int(total_ent[0])


    query3 = "SELECT carrera from subprograma WHERE id_carrera = 103"
    cursor.execute(query3)
    mensajex = list(cursor.fetchall()[0])

    ## En esta seccion se consulta el numero de solicitudes de la solicitud

    suma = []

    f1 = "Select COUNT(*) from VinculoSolicitud WHERE id_carrera = 103 and id_solicitud = 1;"
    cursor.execute(f1)
    ff1 = cursor.fetchall()
    fs1 = list(ff1[0])


    f2 = "Select COUNT(*) from VinculoSolicitud WHERE id_carrera = 103 and id_solicitud = 2;"
    cursor.execute(f2)
    ff2 = cursor.fetchall()
    fs2 = list(ff2[0])


    f3 = "Select COUNT(*) from VinculoSolicitud WHERE id_carrera = 103 and id_solicitud = 3;"
    cursor.execute(f3)
    ff3 = cursor.fetchall()
    fs3 = list(ff3[0])


    f4 = "Select COUNT(*) from VinculoSolicitud WHERE id_carrera = 103 and id_solicitud = 4;"
    cursor.execute(f4)
    ff4 = cursor.fetchall()
    fs4 = list(ff4[0])


    f5 = "Select COUNT(*) from VinculoSolicitud WHERE id_carrera = 103 and id_solicitud = 5;"
    cursor.execute(f5)
    ff5 = cursor.fetchall()
    fs5 = list(ff5[0])


    f6 = "Select COUNT(*) from VinculoSolicitud WHERE id_carrera = 103 and id_solicitud = 6;"
    cursor.execute(f6)
    ff6 = cursor.fetchall()
    fs6 = list(ff6[0])


    f7 = "Select COUNT(*) from VinculoSolicitud WHERE id_carrera = 103 and id_solicitud = 7;"
    cursor.execute(f7)
    ff7 = cursor.fetchall()
    fs7 = list(ff7[0])

    f8 = "Select COUNT(*) from VinculoSolicitud WHERE id_carrera = 103 and id_solicitud = 8;"
    cursor.execute(f8)
    ff8 = cursor.fetchall()
    fs8 = list(ff8[0])

    f9 = "Select COUNT(*) from VinculoSolicitud WHERE id_carrera = 103 and id_solicitud = 9;"
    cursor.execute(f9)
    ff9 = cursor.fetchall()
    fs9 = list(ff9[0])

    f10 = "Select COUNT(*) from VinculoSolicitud WHERE id_carrera = 103 and id_solicitud = 10;"
    cursor.execute(f10)
    ff10 = cursor.fetchall()
    fs10 = list(ff10[0])

    def porcentaje(x):
        x = ((x[0] * 100) / t)
        vv = float("{:.2f}".format(x))
        l = []
        l.append(vv)
        return l

    suma = [porcentaje(fs1)+
            porcentaje(fs2)+
            porcentaje(fs3)+
            porcentaje(fs4)+
            porcentaje(fs5)+
            porcentaje(fs6)+
            porcentaje(fs7)+
            porcentaje(fs8)+
            porcentaje(fs9)+
            porcentaje(fs10)]
    x = ['CDTS', 'SP', 'AR','PDTI', 'AE','CS','EUC','IE','ADN','LP']
    fila1 = [x[0]]+[resultado1[0][1]]+fs1+porcentaje(fs1)
    fila2 = [x[1]]+[resultado1[1][1]]+fs2+porcentaje(fs2)
    fila3 = [x[2]]+[resultado1[2][1]]+fs3+porcentaje(fs3)
    fila4 = [x[3]]+[resultado1[3][1]]+fs4+porcentaje(fs4)
    fila5 = [x[4]]+[resultado1[4][1]]+fs5+porcentaje(fs5)
    fila6 = [x[5]]+[resultado1[5][1]]+fs6+porcentaje(fs6)
    fila7 = [x[6]]+[resultado1[6][1]]+fs7+porcentaje(fs7)
    fila8 = [x[7]]+[resultado1[7][1]]+fs8+porcentaje(fs8)
    fila9 = [x[8]]+[resultado1[8][1]]+fs9+porcentaje(fs9)
    fila10 = [x[9]]+[resultado1[9][1]]+fs10+porcentaje(fs10)
    fila11 = ["N/A", "TOTAL", t, sum(suma[0])-0.01]

    print((resultado1[0])[1])

    ## creando el grafico
    ## grafico

    c = canvas.Canvas("103.pdf", pagesize=letter)

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
            fila10,
            fila11]

    tabla = Table(encabezados + filas)
    # Agregar bordes a la tabla
    tabla.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BOX', (0, 0), (-1, -1), 1, colors.black)
    ]))


    mensaje = f"SUBPROGRAMA: {mensajex[0]}"
    #x = ['CDTS', 'SP', 'AR','PDTI', 'AE','CS','EUC','IE','ADN','LP']
    yp = [porcentaje(fs1)[0],porcentaje(fs2)[0],porcentaje(fs3)[0],porcentaje(fs4)[0],porcentaje(fs5)[0],porcentaje(fs6)[0],porcentaje(fs7)[0],porcentaje(fs8)[0],porcentaje(fs9)[0],porcentaje(fs10)[0]]
    y = [fila1[2], fila2[2], fila3[2], fila4[2], fila5[2], fila6[2], fila7[2], fila8[2], fila9[2], fila10[2]]
    print(y)
    plt.bar(x, yp)
    print(porcentaje(fs1))

    for i, v in enumerate(yp):
        plt.text(i, v / 2, str(v), color='white', ha='center', size="8")

    # Etiquetas de los ejes
    plt.xlabel('Solicitudes')
    plt.ylabel('Cantidad')
    plt.savefig("103.jpg")


    tabla.wrapOn(c, 1, 1)  # Ancho y alto de la tabla
    tabla.drawOn(c, 150, 395)   # Posición (x, y) de la tabla en el canvas
    c.drawImage("pcba.jpg", 420, 680, width=100, height=100)
    c.drawImage("unellez.jpg", 80, 685, width=70, height=80)
    c.drawImage("gobierno.jpg", 180, 720, width=250, height=30)
    c.drawString(180, 660, "Programa de Ciencias Basicas y Aplicadas")
    c.drawString(150, 620, mensaje)
    c.drawImage("103.jpg", 110, 100, width=370, height=270)
    c.drawString(250,350, "Descripcion Grafica")

    # Guardar el documento PDF
    c.save()





