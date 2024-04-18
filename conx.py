import mysql.connector
from reportlab.platypus import Table, TableStyle
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib import colors
from reportlab.pdfgen import canvas


# Esta es una clase que se encarga de conectarse a la base de datos
# y de realizar las consultas para extraer los datos que van a ser
# insertados en la tabla que se imprime en pdf

class solicitudesDB:

    # Sinceramente nose para que es esta funcion que dice init
    # pero es necesaria para poder inicializar la clase y mas

    def __init__(self, host, user, password, database, port):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port

    """ Aqui esta funcion es la que realiza la conexion con la base de datos
    es decir, primero le pasamos los argumentos a la funcion init y luego usando el
    metodo conectar simplemente el ejecutara el codigo que esta dentro de la funcion
    conectar, y el codigo que se encuentra alli es el de la conexion a la base de datos"""

    def conectar(self):
        self.conexion = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
            port=self.port
        )
        print("Conectado con exito.")
    
    """ Esta funcion aqui es para cerrar la conexion de la base de datos,
    sencillo sin nada mas que añadir """

    def desconectar(self):
        self.conexion.close()

    """ Esta funcion toma el total de solicitudes de la carrera que nosotros queramos,
    el dato de entrada para este parametro sera para indicar que carrera queremos consultar,
    aqui se clasifican por id, va desde la id 101 hasta la 109,
    en el manual de sistema se encuentran las id de las carreras con su nombre y a
    que tabla de la base de dato pertenecen. """

    def TotalSCarrera(self, IdCarrera):
        cursor = self.conexion.cursor()
        query = f"SELECT COUNT(*) from VinculoSolicitud WHERE id_carrera = {IdCarrera}"
        cursor.execute(query)
        total = cursor.fetchall()
        total_ent = [int(x) for tup in total for x in tup]
        t = int(total_ent[0])
        return t

    """ Esta funcion lo que hace es extraer el nombre de la carrera
    para colocarlo en el pdf en la parte que dice SUBPROGRAMA encima de la tabla"""
    def NombreCarrera(self, nomCar):
        cursor = self.conexion.cursor()
        query = f"SELECT carrera from subprograma WHERE id_carrera = {nomCar}"
        cursor.execute(query)
        mensajex = list(cursor.fetchall()[0])[0]
        return mensajex

    def TotalSoliPorCarr(self, IdCarrera, IdSol):
        cursor = self.conexion.cursor()
        query = f"Select COUNT(*) from VinculoSolicitud WHERE id_carrera = {IdCarrera} and id_solicitud = {IdSol};"
        cursor.execute(query)
        total_soli = cursor.fetchall()
        fs1 = list(total_soli[0])[0]
        return fs1

    def NombreDeSolis(self):
        cursor = self.conexion.cursor()
        query = "SELECT solicitud FROM solicitudes"
        cursor.execute(query)
        resultado = cursor.fetchall()
        resultado = list(resultado)
        resultado1 = [list(tup) for tup in resultado]
        return resultado1

    def probando(self):
        cursor = self.conexion.cursor()
        total = 0
        f1 = "Select COUNT(*) from VinculoSolicitud WHERE id_carrera = 101 and id_solicitud = %s;"
        for i in range (1,10):
            cursor.execute(f1, (i,))
            ff1 = list(cursor.fetchall()[0])
            for row in ff1:
                x = ((row * 100) / total)
                vv = float("{:.2f}".format(x))
                return vv


# De aqui en adelante viene puro codigo para convocar a las funciones
           


"""Conexion a la base de datos"""
db = solicitudesDB("localhost", "root", "valentin", "indic", "3307")
db.conectar()

n = db.probando() 
print(n)

"""Solicitudes para Ingenieria en Informatica"""
total = db.TotalSCarrera(101)
carrera = db.NombreCarrera(101)
SoliPorCarr = db.TotalSoliPorCarr(101, 1)
NDS = db.NombreDeSolis()

"""Esta es la funcion encargada de sacarle el porcentaje de cada solicitud individualmente"""
def porcentaje(x):
    x = ((x * 100) / total)
    vv = float("{:.2f}".format(x))
    return vv


#Elementos para ser insertados en la tabla en su respectivo orden#

x = ['CDTS', 'SP', 'AR','PDTI', 'AE','CS','EUC','IE','ADN','LP']

ING = [[x[0],NDS[0][0],db.TotalSoliPorCarr(101, 1), porcentaje(db.TotalSoliPorCarr(101, 1))],
[x[1],NDS[1][0],db.TotalSoliPorCarr(101, 2), porcentaje(db.TotalSoliPorCarr(101, 2))],
[x[2],NDS[2][0],db.TotalSoliPorCarr(101, 3), porcentaje(db.TotalSoliPorCarr(101, 3))],
[x[3],NDS[3][0],db.TotalSoliPorCarr(101, 4), porcentaje(db.TotalSoliPorCarr(101, 4))],
[x[4],NDS[4][0],db.TotalSoliPorCarr(101, 5), porcentaje(db.TotalSoliPorCarr(101, 5))],
[x[5],NDS[5][0],db.TotalSoliPorCarr(101, 6), porcentaje(db.TotalSoliPorCarr(101, 6))],
[x[6],NDS[6][0],db.TotalSoliPorCarr(101, 7), porcentaje(db.TotalSoliPorCarr(101, 7))],
[x[7],NDS[7][0],db.TotalSoliPorCarr(101, 8), porcentaje(db.TotalSoliPorCarr(101, 8))],
[x[8],NDS[8][0],db.TotalSoliPorCarr(101, 9), porcentaje(db.TotalSoliPorCarr(101, 9))],
[x[9],NDS[9][0],db.TotalSoliPorCarr(101, 10), porcentaje(db.TotalSoliPorCarr(101, 10)),
 ["N/A", "TOTAL", total]]]


# c = canvas.Canvas("test.pdf", pagesize=letter)

# encabezados = [['ID', 'Solicitud', "Cantidad", "Porcentaje"]]
# tabla = Table(encabezados + ING)

# tabla.setStyle(TableStyle([
# ('GRID', (0, 0), (-1, -1), 1, colors.black),
# ('BOX', (0, 0), (-1, -1), 1, colors.black)
# ]))

# tabla.wrapOn(c, 1, 1)  # Ancho y alto de la tabla
# tabla.drawOn(c, 150, 395)   # Posición (x, y) de la tabla en el canvas
# c.drawImage("pcba.jpg", 420, 680, width=100, height=100)
# c.drawImage("unellez.jpg", 80, 685, width=70, height=80)
# c.drawImage("gobierno.jpg", 180, 720, width=250, height=30)
# c.drawString(180, 660, "Programa de Ciencias Basicas y Aplicadas")
# c.drawString(150, 620, carrera)
# c.drawImage("uno.jpg", 110, 100, width=370, height=270)
# c.drawString(250,350, "Descripcion Grafica")

# # Guardar el documento PDF
# c.save()