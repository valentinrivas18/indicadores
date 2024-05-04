import mysql.connector
import datetime
from reportlab.platypus import Table, TableStyle
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from conx import solicitudesDB


class Plantilla:
    def __init__(self, carrera):
        self.carrera = carrera
        db = solicitudesDB("localhost", "root", "valentin", "indic", "3307")
        db.conectar()
    def crear_tabla(self):
        """Conexion a la base de datos"""
        db = solicitudesDB("localhost", "root", "valentin", "indic", "3307")
        db.conectar()
        """Esta parte del codigo se encarga unicamente de consultar datos que van a ser ingresados dentro de la tabla,
        nada de lo que este fuera de la tabla se encontrara dentro de este archivo, la razon es porque esta funcion es unicamente
        capaz de retornar los datos de la tabla, toda consulta que se muestre fuera de la base de datos tiene que ir en otra funcion,
        aqui solamente."""

        """Solicitudes para X subprograma(Carrera)"""
        total = db.TotalSCarrera(self.carrera)
        SoliPorCarr = db.TotalSoliPorCarr(self.carrera, 1)
        NDS = db.NombreDeSolis()
        """Aqui se saca el porcentaje"""
        def porcentaje(x):
            try:
                x = ((x * 100) / total)
                vv = float("{:.2f}".format(x))
            except ZeroDivisionError:
                vv = 0
            return vv
        #Elementos para ser insertados en la tabla en su respectivo orden#
        x = ['CDTS',
            'SP',
            'AR',
            'PDTI',
            'AE',
            'CS',
            'EUC',
            'IE',
            'ADN',
            'LP']
        fila1 = [ [x[0],NDS[0][0],db.TotalSoliPorCarr(self.carrera, 1), porcentaje(db.TotalSoliPorCarr(self.carrera, 1))],
                [x[1],NDS[1][0],db.TotalSoliPorCarr(self.carrera, 2), porcentaje(db.TotalSoliPorCarr(self.carrera, 2))],
                [x[2],NDS[2][0],db.TotalSoliPorCarr(self.carrera, 3), porcentaje(db.TotalSoliPorCarr(self.carrera, 3))],
                [x[3],NDS[3][0],db.TotalSoliPorCarr(self.carrera, 4), porcentaje(db.TotalSoliPorCarr(self.carrera, 4))],
                [x[4],NDS[4][0],db.TotalSoliPorCarr(self.carrera, 5), porcentaje(db.TotalSoliPorCarr(self.carrera, 5))],
                [x[5],NDS[5][0],db.TotalSoliPorCarr(self.carrera, 6), porcentaje(db.TotalSoliPorCarr(self.carrera, 6))],
                [x[6],NDS[6][0],db.TotalSoliPorCarr(self.carrera, 7), porcentaje(db.TotalSoliPorCarr(self.carrera, 7))],
                [x[7],NDS[7][0],db.TotalSoliPorCarr(self.carrera, 8), porcentaje(db.TotalSoliPorCarr(self.carrera, 8))],
                [x[8],NDS[8][0],db.TotalSoliPorCarr(self.carrera, 9), porcentaje(db.TotalSoliPorCarr(self.carrera, 9))],
                [x[9],NDS[9][0],db.TotalSoliPorCarr(self.carrera, 10), porcentaje(db.TotalSoliPorCarr(self.carrera, 10))],
                ["N/A", "TOTAL", total]
                    ]
        """Este fragmento de codigo sirver sirve para sumar el porcentaje total de
            las solicitudes del subprograma y agregarlo en la ultima fila de la tabla"""
        prueba = []
        for i in range(0,len(fila1)-1):
            UE = fila1[i][-1]
            prueba.append(UE)
        obj = sum(prueba)
        fila1[len(fila1)-1].append(obj)

        """Estos son los encabezados de la tabla, es decir el titulo de los campos"""
        encabezados = [['ID', 'Solicitud', "Cantidad", "Porcentaje"]]

        """En esta parte ya se unifica los encabezados con las filas, en este caso yo hice una sola tabla para representar
        todas las filas ya que asi se hace mas facil y corto el codigo."""
        tabla = Table(encabezados + fila1)
        db.desconectar()
        return tabla

    def grafico(self):
        db = solicitudesDB("localhost", "root", "valentin", "indic", "3307")
        db.conectar()
        total = db.TotalSCarrera(self.carrera)
        db.TotalSoliPorCarr(self.carrera, 1)
        def porcentaje(x):
            try:
                x = ((x * 100) / total)
                vv = float("{:.2f}".format(x))
            except ZeroDivisionError:
                vv = 0
            return vv
        prcntg = [porcentaje(db.TotalSoliPorCarr(self.carrera, 1)),
                porcentaje(db.TotalSoliPorCarr(self.carrera, 2)),
                porcentaje(db.TotalSoliPorCarr(self.carrera, 3)),
                porcentaje(db.TotalSoliPorCarr(self.carrera, 4)),
                porcentaje(db.TotalSoliPorCarr(self.carrera, 5)),
                porcentaje(db.TotalSoliPorCarr(self.carrera, 6)),
                porcentaje(db.TotalSoliPorCarr(self.carrera, 7)),
                porcentaje(db.TotalSoliPorCarr(self.carrera, 8)),
                porcentaje(db.TotalSoliPorCarr(self.carrera, 9)),
                porcentaje(db.TotalSoliPorCarr(self.carrera, 10))]
        db.desconectar()
        return prcntg

    def fecha(self):
        """Estas dos lineas de codigo sirven para que el pdf generado 
           como nombre la fecha y hora en la que se genero"""
        FA = datetime.datetime.now()
        FechaPDF = FA.strftime("Fecha: "+"%d/%m/%Y")
        FF = FA.strftime("REPORTE-"+"%Iy%M"+"%p-"+"%Y%m%d"+".pdf")
        return FechaPDF
    def mensajecarrera(self):
        """Conexion a la base de datos"""
        db = solicitudesDB("localhost", "root", "valentin", "indic", "3307")
        db.conectar()
        nombrecarrera = "SUBPROGRAMA: " + db.NombreCarrera(self.carrera)
        db.desconectar()
        return nombrecarrera


