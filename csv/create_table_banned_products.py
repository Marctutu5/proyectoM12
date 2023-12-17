import sqlite3

# Conectar a la base de datos SQLite
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Script SQL para crear la tabla 'banned_products'
create_table_script = """
CREATE TABLE IF NOT EXISTS banned_products (
    product_id INTEGER,
    reason TEXT,
    created DATETIME,
    PRIMARY KEY (product_id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);
"""

try:
    # Ejecutar el script para crear la tabla
    cursor.execute(create_table_script)
    # Guardar los cambios
    conn.commit()
    print("Tabla 'banned_products' creada con éxito.")
except sqlite3.Error as e:
    print(f"Ha ocurrido un error: {e}")
finally:
    # Cerrar la conexión a la base de datos
    conn.close()
