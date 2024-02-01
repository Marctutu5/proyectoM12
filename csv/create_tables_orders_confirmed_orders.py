import sqlite3

# Conectar a la base de datos SQLite
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Script SQL para crear la tabla 'orders'
create_orders_table_script = """
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY,
    product_id INTEGER,
    buyer_id INTEGER,
    offer MONEY,
    created DATETIME,
    FOREIGN KEY (product_id) REFERENCES products(id),
    FOREIGN KEY (buyer_id) REFERENCES users(id)
);
"""

# Script SQL para crear la tabla 'confirmed_orders'
create_confirmed_orders_table_script = """
CREATE TABLE IF NOT EXISTS confirmed_orders (
    order_id INTEGER,
    created DATETIME,
    PRIMARY KEY (order_id),
    FOREIGN KEY (order_id) REFERENCES orders(id)
);
"""

try:
    # Ejecutar el script para crear la tabla 'orders'
    cursor.execute(create_orders_table_script)
    # Ejecutar el script para crear la tabla 'confirmed_orders'
    cursor.execute(create_confirmed_orders_table_script)
    # Guardar los cambios
    conn.commit()
    print("Tablas 'orders' y 'confirmed_orders' creadas con éxito.")
except sqlite3.Error as e:
    print(f"Ha ocurrido un error: {e}")
finally:
    # Cerrar la conexión a la base de datos
    conn.close()
