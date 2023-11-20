import sqlite3

# Conectarse a la base de datos SQLite (asegúrate de que la base de datos exista)
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Agregar las columnas 'email_token' y 'verified' a la tabla 'users' si no existen
cursor.execute("ALTER TABLE users ADD COLUMN email_token TEXT")
cursor.execute("ALTER TABLE users ADD COLUMN verified INTEGER")

# Actualizar todos los usuarios existentes para que 'verified' esté en 0 (FALSO) por defecto
cursor.execute("UPDATE users SET verified = 0")

# Guardar los cambios y cerrar la conexión
conn.commit()
conn.close()

print("Se han modificado la tabla 'users' en la base de datos.")
