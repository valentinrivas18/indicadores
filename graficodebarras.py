import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="valentin",
    database="indic",
    port="3307"
    )

cursor = conexion.cursor()
query = "SELECT COUNT(id_solicitud) AS solicitudes, SUM(CASE WHEN id_carrera = 101 THEN 1 ELSE 0 END) / COUNT(id_solicitud) * 100 AS porcentaje FROM VinculoSolicitud"
cursor.execute(query)
data = cursor.fetchall()
print(data)