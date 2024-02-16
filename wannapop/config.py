import os
from os import environ

# Secret key
SECRET_KEY = "Valor aleatori molt llarg i super secret"

# ruta absoluta d'aquesta carpeta
BASEDIR = os.path.abspath(os.path.dirname(__file__))

# Configuració per a MySQL
MYSQL_USERNAME = '2dd09'
MYSQL_PASSWORD = '0vOxXzRcjty38wSP'
MYSQL_HOST = '37.27.3.70'
MYSQL_PORT = '3306'
MYSQL_DB_NAME = '2dd09_flask4'
SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{MYSQL_USERNAME}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB_NAME}"

# Resta de la configuració ...
MAIL_SENDER_NAME="Administrador"
MAIL_SENDER_ADDR="2daw.equip09@fp.insjoaquimmir.cat"
MAIL_SENDER_PASSWORD="BCaIo5785@[="
MAIL_SMTP_SERVER="smtp.gmail.com"
MAIL_SMTP_PORT="587"

CONTACT_ADDR="matuvi@fp.insjoaquimmir.cat"
EXTERNAL_URL="http://127.0.0.1:5000"

# DEBUG TOOLBAR
DEBUG = True
DEBUG_TB_INTERCEPT_REDIRECTS = False

# Configuración del nivel de registro
LOG_LEVEL = environ.get('LOG_LEVEL', 'DEBUG').upper()
