# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456789@localhost/tirepluss'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = 'elias'

    db.init_app(app)



    with app.app_context():
        # Crear las tablas en la base de datos si no existen
        db.create_all()

    return app
