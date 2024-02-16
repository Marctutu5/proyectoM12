import re

def convert_sqlite_to_mysql(sqlite_sql):
    # Remover líneas no soportadas por MySQL
    sqlite_sql = re.sub(r'^BEGIN TRANSACTION;$', '', sqlite_sql, flags=re.MULTILINE)
    sqlite_sql = re.sub(r'^COMMIT;$', '', sqlite_sql, flags=re.MULTILINE)
    sqlite_sql = re.sub(r'^sqlite_sequence.*$', '', sqlite_sql, flags=re.MULTILINE)
    sqlite_sql = re.sub(r'^CREATE UNIQUE INDEX.*$', '', sqlite_sql, flags=re.MULTILINE)
    
    # Reemplazar " por `
    sqlite_sql = sqlite_sql.replace('"', '`')

    # Reemplazar AUTOINCREMENT por AUTO_INCREMENT
    sqlite_sql = sqlite_sql.replace('AUTOINCREMENT', 'AUTO_INCREMENT')

    # Reemplazar 't' por 1 y 'f' por 0 (booleanos)
    sqlite_sql = re.sub(r"'t'", '1', sqlite_sql)
    sqlite_sql = re.sub(r"'f'", '0', sqlite_sql)

    # Reemplazar ; al final de las sentencias por \n
    sqlite_sql = re.sub(r';$', '\n', sqlite_sql, flags=re.MULTILINE)

    return sqlite_sql

# Ejemplo de uso
with open('export.sql', 'r') as f:
    sqlite_sql = f.read()

mysql_sql = convert_sqlite_to_mysql(sqlite_sql)

# Guardar el resultado en un archivo
with open('exportmysql.sql', 'w') as f:
    f.write(mysql_sql)

print("Archivo convertido exitosamente a MySQL.")
