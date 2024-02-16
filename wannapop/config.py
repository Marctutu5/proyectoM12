import os
from os import environ

# Secret key
SECRET_KEY = "Valor aleatori molt llarg i super secret"

# ruta absoluta d'aquesta carpeta
BASEDIR = os.path.abspath(os.path.dirname(__file__))

# postgres amb docker-compose
SQLALCHEMY_DATABASE_URI = "postgresql://user:patata@127.0.0.1:5432/userdb"

# paràmetre que farà servir SQLAlchemy per a connectar-se
# SQLALCHEMY_DATABASE_URI = "postgresql://2dd09:0vOxXzRcjty38wSP@37.27.3.70:5432/2dd09_pg"

# mostre als logs les ordres SQL que s'executen
SQLALCHEMY_ECHO = True

SECRET_KEY="Valor aleatori molt llarg i super secret"
# SQLITE_FILE_RELATIVE_PATH="sqlite/database.db"

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