from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import current_user

from services.auth_service import AuthService

auth_controller = Blueprint('auth_controller', __name__)


@auth_controller.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        success, message = AuthService.login(email, password)
        if success:
            flash(message, category='success')
            return redirect(url_for('note_controller.home'))
        else:
            flash(message, category='error')

    return render_template("login.html", user=current_user)


@auth_controller.route('/logout')
def logout():
    AuthService.logout()
    return redirect(url_for('auth_controller.login'))


@auth_controller.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        success, message = AuthService.sign_up(email, first_name, password1, password2)
        if success:
            flash(message, category='success')
            return redirect(url_for('note_controller.home'))
        else:
            flash(message, category='error')

    return render_template("signup.html", user=current_user)
