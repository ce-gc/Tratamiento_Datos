import json
import sqlite3

# Cargar el JSON
with open('datostemperatura.txt', 'r') as f:
    datos = json.load(f)

# Conectar/crear la base de datos
conn = sqlite3.connect('meteorologia.db')
cursor = conn.cursor()

# Crear tabla solo con los campos necesarios
cursor.execute('''
    CREATE TABLE IF NOT EXISTS temperaturas (
        id     INTEGER PRIMARY KEY AUTOINCREMENT,
        fint   TEXT,
        tamax  REAL
    )
''')

# Insertar solo fint y tamax
for item in datos:
    cursor.execute('''
        INSERT INTO temperaturas (fint, tamax)
        VALUES (?, ?)
    ''', (item['fint'], item['tamax']))

conn.commit()
conn.close()
print(f"{len(datos)} registros insertados correctamente.")