import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Ya esta creada
# Añadir la columna 'category_id' a la tabla 'products'
#cursor.execute("""
#ALTER TABLE products
#ADD COLUMN category_id INTEGER;
#""")

# Añadir la columna 'status_id' a la tabla 'products'
cursor.execute("""
ALTER TABLE products
ADD COLUMN status_id INTEGER;
""")

# Confirmar los cambios
conn.commit()

# Cerrar la conexión
conn.close()

print("Columnas 'category_id' y 'status_id' añadidas a la tabla 'products'.")

