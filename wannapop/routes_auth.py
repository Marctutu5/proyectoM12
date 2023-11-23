from flask import Blueprint, redirect, render_template, url_for, flash
from flask_login import current_user, login_user, login_required, logout_user
from . import login_manager, mail_manager  # Importa mail_manager desde tu paquete
from .models import User
from .forms import LoginForm, RegisterForm, ResendVerificationForm
from .helper_role import notify_identity_changed
from . import db_manager as db
from werkzeug.security import check_password_hash, generate_password_hash
import secrets

# Blueprint
auth_bp = Blueprint(
    "auth_bp", __name__, template_folder="templates", static_folder="static"
)

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main_bp.init"))

    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        plain_text_password = form.password.data

        # Cargar el usuario basado en el correo electrónico
        user = load_user(email)

        # Verifica primero si el usuario existe y la contraseña es correcta
        if user and check_password_hash(user.password, plain_text_password):
            # Si el usuario no ha verificado su correo electrónico
            if not user.verified:  # Asegúrate de usar 'verified' en lugar de 'email_verified'
                flash('Debes verificar tu correo electrónico antes de iniciar sesión. Por favor, revisa tu correo electrónico y haz clic en el enlace de verificación.', 'warning')
                return redirect(url_for("auth_bp.login"))

            # Iniciar sesión y redirigir si el usuario está verificado
            login_user(user)
            notify_identity_changed()
            flash('Inicio de sesión exitoso', 'success')
            return redirect(url_for("main_bp.init"))

        # Si las credenciales no son correctas
        flash('Login Incorrecto. Por favor revisa tus credenciales.', 'error')
        return redirect(url_for("auth_bp.login"))
    
    return render_template('/auth/login.html', form=form)



@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        # Si el usuario actual ya está autenticado, redirige a la página principal.
        return redirect(url_for("main_bp.init"))

    form = RegisterForm()
    if form.validate_on_submit():
        # Extrae los datos del formulario.
        name = form.name.data
        email = form.email.data
        plain_text_password = form.password.data

        # Comprueba si ya existe un usuario con ese email.
        user = User.query.filter_by(email=email).first()
        if user:
            # Si el usuario ya existe, muestra un mensaje y redirige al formulario de registro.
            flash('Ya existe una cuenta con este correo electrónico.', 'error')
            return redirect(url_for('auth_bp.register'))

        # Si el usuario no existe, crea uno nuevo.
        hashed_password = generate_password_hash(plain_text_password)
        email_token = secrets.token_urlsafe(20)  # Genera un token seguro para el email.

        new_user = User(
            name=name, 
            email=email, 
            password=hashed_password, 
            role="wanner",
            email_token=email_token  # Guarda el token en el usuario.
        )
        db.session.add(new_user)
        db.session.commit()

        # Envía un correo electrónico con el enlace de verificación.
        verification_link = url_for('auth_bp.verify_email', name=name, token=email_token, _external=True)
        mail_manager.send_verification_email(email, name, verification_link)

        # Muestra un mensaje de éxito y redirige a la página de inicio de sesión.
        flash('Registro exitoso. Revisa tu correo electrónico para verificar tu cuenta.', 'success')
        return redirect(url_for('auth_bp.login'))

    # Si el formulario no se ha enviado o no es válido, muestra el formulario de registro.
    return render_template('/auth/register.html', form=form)


@auth_bp.route("/verify_email/<name>/<token>")
def verify_email(name, token):
    user = User.query.filter_by(email_token=token).first()
    if user and user.name == name:  # Asegúrate de que tanto el token como el nombre coincidan
        user.verified = True  # Cambia 'email_verified' a 'verified' según tu modelo
        db.session.commit()
        flash('Tu cuenta ha sido verificada. Ahora puedes iniciar sesión.', 'success')
        return redirect(url_for('auth_bp.login'))
    else:
        # Si el token no es válido o el nombre no coincide
        flash('El enlace de verificación no es válido o ha expirado, o el nombre de usuario no coincide.', 'error')
        return redirect(url_for('auth_bp.register'))


@auth_bp.route("/profile", methods=["GET", "POST"])
@login_required
def profile():
    form = ProfileForm(obj=current_user)

    if form.validate_on_submit():
        current_user.name = form.name.data

        if current_user.email != form.email.data:
            # Si el correo electrónico ha cambiado
            current_user.email = form.email.data
            current_user.verified = False  # Marca el usuario como no verificado
            email_token = secrets.token_urlsafe(20)
            current_user.email_token = email_token
            verification_link = url_for('auth_bp.verify_email', name=current_user.name, token=email_token, _external=True)
            mail_manager.send_verification_email(form.email.data, current_user.name, verification_link)

        # Actualiza la contraseña solo si se ha ingresado una nueva
        if form.password.data:
            hashed_password = generate_password_hash(form.password.data)
            current_user.password = hashed_password

        db.session.commit()
        flash('Perfil actualizado con éxito.', 'success')
        return redirect(url_for('auth_bp.profile'))

    return render_template('/auth/profile.html', form=form)



@login_manager.user_loader
def load_user(email):
    if email is not None:
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

@auth_bp.route("/resend", methods=["GET", "POST"])
def resend_verification_email():
    form = ResendVerificationForm()

    if form.validate_on_submit():
        email = form.email.data
        user = User.query.filter_by(email=email).first()

        if user and not user.verified:
            # Aquí puedes colocar la lógica directa para enviar el correo de verificación
            verification_link = url_for('auth_bp.verify_email', name=user.name, token=user.email_token, _external=True)
            mail_manager.send_verification_email(user.email, user.name, verification_link)

            flash("Se ha reenviado el correo de verificación. Por favor, revisa tu bandeja de entrada.", "success")
            return redirect(url_for("auth_bp.login"))
        else:
            flash("No se pudo reenviar el correo de verificación. Verifica que la dirección de correo sea correcta o que la cuenta ya esté verificada.", "error")

    return render_template("auth/resend_verification.html", form=form)