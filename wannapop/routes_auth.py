from flask import Blueprint, redirect, render_template, url_for, flash
from flask_login import current_user, login_user, login_required, logout_user
from . import login_manager
from .models import User
from .forms import LoginForm, RegisterForm
from .helper_role import notify_identity_changed
from . import db_manager as db
from werkzeug.security import check_password_hash, generate_password_hash

# Blueprint
auth_bp = Blueprint(
    "auth_bp", __name__, template_folder="templates", static_folder="static"
)

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    # Si ya está autenticado, redirige a donde desees (en este caso, "main_bp.lista")
    if current_user.is_authenticated:
        return redirect(url_for("main_bp.init"))

    form = LoginForm()
    if form.validate_on_submit(): # si se ha enviado el formulario via POST y es correcto
        email = form.email.data
        plain_text_password = form.password.data

        user = load_user(email)
        if user and check_password_hash(user.password, plain_text_password):
            # aquí se crea la cookie y se inicia sesión
            login_user(user)
            # verifica identidad
            notify_identity_changed()
            flash('Inicio de sesión exitoso', 'success')
            return redirect(url_for("main_bp.init"))

        # si llega aquí, es que no se ha autenticado correctamente
        flash('Login Incorrecto. Porfavor revisa tus credenciales.', 'error')
        return redirect(url_for("auth_bp.login"))
    
    return render_template('/auth/login.html', form=form)


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    # Si ya está autenticado, redirige a donde desees
    if current_user.is_authenticated:
        return redirect(url_for("main_bp.init"))

    form = RegisterForm()
    if form.validate_on_submit():  # si se ha enviado el formulario via POST y es correcto
        name = form.name.data
        email = form.email.data
        plain_text_password = form.password.data

        # Verificar si ya existe un usuario con ese email
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Ya existe una cuenta con este correo electrónico.', 'error')
            return redirect(url_for('auth_bp.register'))

        # Crear un nuevo usuario
        hashed_password = generate_password_hash(plain_text_password)
        new_user = User(name=name, email=email, password=hashed_password, role="wanner")

        db.session.add(new_user)
        db.session.commit()

        flash('Registro exitoso. Ahora puedes iniciar sesión.', 'success')
        return redirect(url_for('auth_bp.login'))

    return render_template('/auth/register.html', form=form)

@auth_bp.route("/profile")
@login_required
def profile():
    # Aquí obtendrás la información del usuario autenticado
    user = current_user  # Supongo que estás utilizando Flask-Login para la gestión de usuarios

    # Renderiza la plantilla de perfil y pasa los datos del usuario a la plantilla
    return render_template('/auth/profile.html', user=user)

@login_manager.user_loader
def load_user(email):
    if email is not None:
        # select amb 1 resultat o cap
        user_or_none = db.session.query(User).filter(User.email == email).one_or_none()
        return user_or_none
    return None

@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for("auth_bp.login"))

@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth_bp.login"))