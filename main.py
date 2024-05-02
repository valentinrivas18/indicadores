import mysql.connector

class BDD:
    def conexionbd():
        conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="valentin",
        database="ind",
        port="3307",

        cursor = conexion.cursor()
    )


