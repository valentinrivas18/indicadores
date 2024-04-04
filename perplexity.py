import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk

# Conexión a la base de datos MySQL
conn = mysql.connector.connect(
host='localhost',
user='root',
password='valentin',
database='indic',
port="3307"
)

cursor = conn.cursor()

# Consulta SQL para obtener los datos requeridos
query = "SELECT id_solicitud, cedula FROM VinculoSolicitud WHERE id_carrera = 101"
cursor.execute(query)
data = cursor.fetchall()

# Crear un DataFrame con los datos
df = pd.DataFrame(data, columns=['id_solicitud', 'cedula'])
0
# Calcular el número de solicitudes por cada número de solicitud
solicitudes_por_numero = df['id_solicitud'].value_counts()
total_solicitudes = solicitudes_por_numero.sum()
max_solicitudes = solicitudes_por_numero.max()

print(type(total_solicitudes))

# Calcular el porcentaje de solicitudes por número de solicitud
porcentaje_solicitudes = (solicitudes_por_numero / total_solicitudes) * 100
porcentaje_solicitudes = porcentaje_solicitudes.round(2)
resultados = pd.DataFrame({
    'Numero de Solicitud': solicitudes_por_numero.index,
    'Cantidad': solicitudes_por_numero.values,
    'Porcentaje': porcentaje_solicitudes.values
})

print(resultados)

# Generar un gráfico de barras con los porcentajes
porcentaje_df = porcentaje_solicitudes.reset_index()
porcentaje_df.columns = ['id_solicitud', 'porcentaje']

# Graficar los porcentajes de solicitudes por número de solicitud en un gráfico de barras
plt.bar(porcentaje_df['id_solicitud'], porcentaje_df['porcentaje'])
plt.xlabel('Número de Solicitud')
plt.ylabel('Porcentaje')
plt.title('Porcentaje de Solicitudes por Número de Solicitud en Carrera Ingenieria en Petroleo')
plt.xticks(range(min(porcentaje_df['id_solicitud']), max(porcentaje_df['id_solicitud'])+1))
plt.show()



print("Se mostro el matplot")

# Cerrar la conexión a la base de datos
cursor.close()
conn.close()