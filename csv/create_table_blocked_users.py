import sqlite3

# Conectar a la base de datos SQLite
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Script SQL para crear la tabla 'blocked_users'
create_table_script = """
CREATE TABLE IF NOT EXISTS blocked_users (
    user_id INTEGER,
    message TEXT,
    created DATETIME,
    PRIMARY KEY (user_id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);
"""

try:
    # Ejecutar el script para crear la tabla
    cursor.execute(create_table_script)
    # Guardar los cambios
    conn.commit()
    print("Taula 'blocked_users' creada amb èxit.")
except sqlite3.Error as e:
    print(f"Ha ocorregut un error: {e}")
finally:
    # Cerrar la conexión a la base de datos
    conn.close()
