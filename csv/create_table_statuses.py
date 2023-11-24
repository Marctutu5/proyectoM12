import sqlite3

# Conectar a la base de datos (o crearla si no existe)
conn = sqlite3.connect('database.db')

# Crear un cursor
cursor = conn.cursor()

# Ejecutar la instrucción de creación de la tabla
cursor.execute("""
CREATE TABLE statuses (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    slug TEXT NOT NULL
)
""")

# Confirmar los cambios y cerrar la conexión
conn.commit()
conn.close()
