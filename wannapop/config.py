import os

# Secret key
SECRET_KEY = "Valor aleatori molt llarg i super secret"

# ruta absoluta d'aquesta carpeta
BASEDIR = os.path.abspath(os.path.dirname(__file__))

# paràmetre que farà servir SQLAlchemy per a connectar-se
SQLALCHEMY_DATABASE_URI = "sqlite:///" + BASEDIR + "/../database.db"

# mostre als logs les ordres SQL que s'executen
SQLALCHEMY_ECHO = True
