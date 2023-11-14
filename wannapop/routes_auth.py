from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import check_password_hash
from .models import User

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user and user.password == password:  # Simplemente comparar las contraseñas
            # Login successful, redirect to home page with success message
            flash('Login successful!', category='success')
            return redirect(url_for('main.index'))
        else:
            # Login failed, redirect to login page with error message
            flash('Invalid login credentials', category='error')
            return redirect(url_for('auth.login'))
    return render_template('auth/login.html')

