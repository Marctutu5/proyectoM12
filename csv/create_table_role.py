import sqlite3

# Conecta a la base de datos SQLite
conn = sqlite3.connect('database.db')  # Reemplaza con la ruta a tu base de datos SQLite
cursor = conn.cursor()

# Agrega la columna "role" a la tabla "users"
cursor.execute('ALTER TABLE users ADD COLUMN role TEXT')

# Guarda los cambios en la base de datos
conn.commit()

# Cierra la conexión
conn.close()
