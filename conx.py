import mysql.connector

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
