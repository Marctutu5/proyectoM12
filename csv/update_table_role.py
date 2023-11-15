import sqlite3

# Conecta a la base de datos SQLite
conn = sqlite3.connect('database.db')  # Reemplaza con la ruta a tu base de datos SQLite
cursor = conn.cursor()

# Actualiza las filas existentes estableciendo el valor "wanner" en el campo "role"
cursor.execute('UPDATE users SET role = "wanner"')

# Guarda los cambios en la base de datos
conn.commit()

# Cierra la conexión
conn.close()
