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


ING_i = Plantilla(101)
tablai = ING_i.crear_tabla()
msjcarrerai = ING_i.mensajecarrera()
fechadi = ING_i.fecha()
graficoi = ING_i.grafico()

ING_p = Plantilla(102)
tablap = ING_p.crear_tabla()
msjcarrerap = ING_p.mensajecarrera()
fechadp = ING_p.fecha()
graficop = ING_p.grafico()

ING_m = Plantilla(103)
tablam = ING_m.crear_tabla()
msjcarreram = ING_m.mensajecarrera()
fechadm = ING_m.fecha()
graficom = ING_m.grafico()

ING_c = Plantilla(104)
tablac = ING_c.crear_tabla()
msjcarrerac = ING_c.mensajecarrera()
fechadc = ING_c.fecha()
graficoc = ING_c.grafico()

LicM = Plantilla(105)
tablalm = LicM.crear_tabla()
msjcarreralm = LicM.mensajecarrera()
fechadlm = LicM.fecha()
graficolm = LicM.grafico()

Arq = Plantilla(106)
tablaA = Arq.crear_tabla()
msjcarreraA = Arq.mensajecarrera()
fechadA = Arq.fecha()
graficoA = Arq.grafico()

tsuT = Plantilla(107)
tablatT = tsuT.crear_tabla()
msjcarreratT = tsuT.mensajecarrera()
fechadtT = tsuT.fecha()
graficotT = tsuT.grafico()

tsuC = Plantilla(108)
tablatC = tsuC.crear_tabla()
msjcarreratC = tsuC.mensajecarrera()
fechadtC = tsuC.fecha()
graficotC = tsuC.grafico()

tsuI = Plantilla(109)
tablatI = tsuI.crear_tabla()
msjcarreratI = tsuI.mensajecarrera()
fechadtI = tsuI.fecha()
graficotI = tsuI.grafico()