import smtplib, ssl
from email.message import EmailMessage
from email.utils import formataddr

class MailManager:
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        # Configuración inicial del MailManager con los datos del archivo de configuración de la app
        self.sender_name = app.config['MAIL_SENDER_NAME']
        self.sender_addr = app.config['MAIL_SENDER_ADDR']
        self.sender_password = app.config['MAIL_SENDER_PASSWORD']
        self.smtp_server = app.config['MAIL_SMTP_SERVER']
        self.smtp_port = app.config['MAIL_SMTP_PORT']

    def send_verification_email(self, user_email, user_name, verification_url):
        # Configuración del correo de verificación
        subject = "Verificación de Correo Electrónico"
        content = f"""Hola {user_name},

Por favor, verifica tu correo electrónico haciendo clic en el siguiente enlace:

{verification_url}

Gracias."""

        # Envío del correo
        self.__send_mail(
            dst_name=user_name,
            dst_addr=user_email,
            subject=subject,
            content=content
        )

    def __send_mail(self, dst_name, dst_addr, subject, content):
        # Creación del contexto SSL para una conexión segura
        context = ssl.create_default_context()
        with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
            server.starttls(context=context)  # Iniciar TLS para una conexión segura
            server.login(self.sender_addr, self.sender_password)  # Iniciar sesión en el servidor SMTP

            # Crear el mensaje de correo electrónico
            msg = EmailMessage()
            msg['From'] = formataddr((self.sender_name, self.sender_addr))
            msg['To'] = formataddr((dst_name, dst_addr))
            msg['Subject'] = subject
            msg.set_content(content)

            # Enviar el correo
            server.send_message(msg, from_addr=self.sender_addr, to_addrs=dst_addr)
