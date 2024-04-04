import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors

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

# Crear el archivo PDF
filename = "reportes.pdf"
doc = SimpleDocTemplate(filename, pagesize=landscape(letter))

data = [df.columns.tolist()] + df.values.tolist()

# Crear una tabla con los datos
table = Table(data)

# Agregar la tabla al archivo PDF
doc.build([table])

# Cerrar la conexión a la base de datos
cursor.close()
conn.close()

