import sqlite3
from werkzeug.security import generate_password_hash

# Conecta a la base de datos y recupera las contraseñas en texto plano
def retrieve_plain_text_passwords():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, password FROM users')
    password_data = cursor.fetchall()
    conn.close()
    return password_data

# Hashea las contraseñas en texto plano y actualiza la base de datos
def hash_and_update_passwords(password_data):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    for user_id, plain_text_password in password_data:
        hashed_password = generate_password_hash(plain_text_password)
        cursor.execute('UPDATE users SET password = ? WHERE id = ?', (hashed_password, user_id))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    password_data = retrieve_plain_text_passwords()
    hash_and_update_passwords(password_data)
    print("Contraseñas hasheadas y actualizadas en la base de datos.")

