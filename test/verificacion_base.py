import json
import sqlite3

# Verificación
conn = sqlite3.connect('meteorologia.db')
cursor = conn.cursor()
cursor.execute('SELECT * FROM temperaturas')
for fila in cursor.fetchall():
    print(fila)
conn.close()