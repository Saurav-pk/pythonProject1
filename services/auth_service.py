from flask_login import login_user
from werkzeug.security import generate_password_hash, check_password_hash
from models.models import User
from db import db


class AuthService:
    @staticmethod
    def login(email, password):
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            login_user(user, remember=True)
            return True, 'Logged in successfully!'
        return False, 'Incorrect email or password.'

    @staticmethod
    def logout():
        from flask_login import logout_user
        logout_user()

    @staticmethod
    def sign_up(email, first_name, password1, password2):
        user = User.query.filter_by(email=email).first()
        if user:
            return False, 'Email already exists.'
        elif len(email) < 4:
            return False, 'Email must be greater than 3 characters.'
        elif len(first_name) < 2:
            return False, 'First name must be greater than 1 characters.'
        elif password1 != password2:
            return False, 'Passwords do not match.'
        elif len(password1) < 4:
            return False, 'Password must be at least 4 characters.'
        else:
            new_user = User(email=email,
                            first_name=first_name,
                            password=generate_password_hash(password1, method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            return True, 'Account created successfully.'
