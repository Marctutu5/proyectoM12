from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_principal import Principal
from .helper_mail import MailManager
from werkzeug.local import LocalProxy
from flask import current_app
from flask_debugtoolbar import DebugToolbarExtension
from logging.handlers import RotatingFileHandler
import logging


# https://stackoverflow.com/a/31764294
logger = LocalProxy(lambda: current_app.logger)

db_manager = SQLAlchemy()
login_manager = LoginManager()
principal = Principal()
mail_manager = MailManager()
toolbar = DebugToolbarExtension()

def create_app():
    # Construct the core app object
    app = Flask(__name__)
    app.config.from_pyfile("config.py")

    # Configurar RotatingFileHandler
    log_handler = RotatingFileHandler('app.log', maxBytes=10240, backupCount=3)
    log_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s '
        '[in %(pathname)s:%(lineno)d]'
    ))
    log_level = app.config.get("LOG_LEVEL", "DEBUG").upper()
    log_handler.setLevel(getattr(logging, log_level))
    app.logger.addHandler(log_handler)

    # Configurar el nivel de registro del logger de la aplicación
    if log_level not in ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']:
        raise ValueError('Nivel de registro no válido')
    app.logger.setLevel(getattr(logging, log_level))

    # Inicializa los plugins
    login_manager.init_app(app)
    db_manager.init_app(app)
    principal.init_app(app)
    mail_manager.init_app(app)
    toolbar.init_app(app)

    with app.app_context():
        from . import routes_main, routes_auth, routes_admin

        # Registra los blueprints
        app.register_blueprint(routes_main.main_bp)
        app.register_blueprint(routes_auth.auth_bp)
        app.register_blueprint(routes_admin.admin_bp)

    app.logger.info("Aplicación iniciada")

    return app