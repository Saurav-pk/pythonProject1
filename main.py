from flask import Flask
from db import db
from controllers.note_controller import note_controller
from controllers.auth_controller import auth_controller
from models.models import User
from flask_login import LoginManager
from os import path

DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'THIS IS SECRET KEY'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:1234@localhost/python'
    db.init_app(app)

    app.register_blueprint(note_controller, url_prefix='/')
    app.register_blueprint(auth_controller, url_prefix='/')

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth_controller.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()
        print('Created Database!')

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
