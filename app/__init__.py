from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:123456789@localhost/recomendacion'

    db.init_app(app)

    # Registrar blueprints
    from app.routes.main import main_bp
    from app.routes.usuarios import usuarios_bp
    from app.routes.formulario import formulario_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(usuarios_bp)
    app.register_blueprint(formulario_bp)

    return app
