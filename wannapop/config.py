import os
from os import environ
SECRET_KEY = os.environ.get("SECRET_KEY", "default-secret-key")
SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
SQLALCHEMY_ECHO = os.environ.get("SQLALCHEMY_ECHO", "False").lower() in ['true', '1', 't']
DEBUG = os.environ.get("FLASK_ENV") == "development"
LOG_LEVEL = os.environ.get('LOG_LEVEL', 'DEBUG').upper()

MAIL_SENDER_NAME = os.environ.get("MAIL_SENDER_NAME")
MAIL_SENDER_ADDR = os.environ.get("MAIL_SENDER_ADDR")
MAIL_SENDER_PASSWORD = os.environ.get("MAIL_SENDER_PASSWORD")
MAIL_SMTP_SERVER = os.environ.get("MAIL_SMTP_SERVER")
MAIL_SMTP_PORT = os.environ.get("MAIL_SMTP_PORT")

CONTACT_ADDR = os.environ.get("CONTACT_ADDR")
EXTERNAL_URL = os.environ.get("EXTERNAL_URL")
