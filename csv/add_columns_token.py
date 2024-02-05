import sqlite3
from datetime import datetime

# Conecta a la base de datos SQLite
conn = sqlite3.connect('database.db')  # Reemplaza con la ruta a tu base de datos SQLite
cursor = conn.cursor()

# Agrega la columna "token" a la tabla "users"
cursor.execute('ALTER TABLE users ADD COLUMN token TEXT')

# Agrega la columna "token_expiration" a la tabla "users"
# SQLite no soporta directamente el tipo "DATETIME", por lo que se usa TEXT y se manejará en el código
cursor.execute('ALTER TABLE users ADD COLUMN token_expiration TEXT')

# Guarda los cambios en la base de datos
conn.commit()

# Cierra la conexión
conn.close()

print("Columnas 'token' y 'token_expiration' añadidas a la tabla 'users'.")
