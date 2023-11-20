import sqlite3
import secrets

# Conectarse a la base de datos SQLite (asegúrate de que la base de datos exista)
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Obtener el número total de registros en la tabla 'users'
total_registros = cursor.execute("SELECT COUNT(*) FROM users").fetchone()[0]

# Actualizar cada registro de la columna 'email_token' con cadenas aleatorias de 20 caracteres
for _ in range(total_registros):
    email_token = secrets.token_urlsafe(20)
    cursor.execute("UPDATE users SET email_token = ? WHERE ROWID = ?", (email_token, _ + 1))

# Establecer la columna 'verified' en 1 para todos los registros
cursor.execute("UPDATE users SET verified = 1")

# Guardar los cambios y cerrar la conexión
conn.commit()
conn.close()

print("Se han actualizado los valores de 'email_token' y 'verified' para todos los registros.")
