from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, DecimalField, SubmitField, SelectField, FileField, TextAreaField
from wtforms.validators import DataRequired, NumberRange, InputRequired, Email, Length
import decimal

class RegisterForm(FlaskForm):
    name = StringField(
        validators = [DataRequired()]
    )
    email = StringField(
        validators = [Email(), DataRequired()]
    )
    password = PasswordField(
        validators=[ DataRequired()]
    )
    submit = SubmitField()

class ProductForm(FlaskForm):
    title = StringField(
        validators = [DataRequired()]
    )
    description = StringField(
        validators = [DataRequired()]
    )
    photo_file = FileField()
    price = DecimalField(
        places = 2, 
        rounding = decimal.ROUND_HALF_UP, 
        validators = [DataRequired(), NumberRange(min = 0)]
    )
    category_id = SelectField(
        validators = [InputRequired()]
    )
    submit = SubmitField()

# Formulari generic per esborrar i aprofitar la CSRF Protection
class DeleteForm(FlaskForm):
    submit = SubmitField()

class LoginForm(FlaskForm):
    email = StringField(
        validators = [Email(), DataRequired()]
    )
    password = PasswordField(
        validators=[ DataRequired()]
    )
    submit = SubmitField()

class ResendVerificationForm(FlaskForm):
    email = StringField(
        validators = [Email(), DataRequired()]
    )
    submit = SubmitField()


class ProfileForm(FlaskForm):
    name = StringField(
        validators=[DataRequired()]
    )
    email = StringField(
        validators=[Email(), DataRequired()]
    )
    password = PasswordField(
        'Nueva Contraseña'
    )
    submit = SubmitField()

class UserBlockForm(FlaskForm):
    user_id = SelectField(
        "Usuari", 
        coerce=int,  # Assegura que el valor sigui un enter
        validators=[DataRequired()]
    )
    message = TextAreaField(
        "Raó del Bloqueig",
        validators=[DataRequired(), Length(max=255)]  # Limita la longitud del missatge
    )
    submit = SubmitField("Enviar")