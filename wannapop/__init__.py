from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_principal import Principal
from .helper_mail import MailManager
from werkzeug.local import LocalProxy
from flask import current_app
from flask_debugtoolbar import DebugToolbarExtension

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