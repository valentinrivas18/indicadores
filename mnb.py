from reportlab.platypus import Table, TableStyle
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib import colors

encabezados = [['Columna 1', 'Columna 2', "Columna 3"]]
filas = [[1,2,3], [4,5,6], [7,8,9]]

tabla = Table(encabezados + filas)
# Agregar bordes a la tabla
tabla.setStyle(TableStyle([
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ('BOX', (0, 0), (-1, -1), 1, colors.black)
]))
doc = SimpleDocTemplate("table.pdf", pagesize=letter)
doc.build([tabla])