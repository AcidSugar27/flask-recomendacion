from flask import Blueprint


from .usuarios_ruta import usuarios_bp
from .recomendaciones_ruta import recomendaciones_bp
#from .neumaticos_routes import neumaticos_bp
from .citas_ruta import citas_bp


def register_routes(app):
    app.register_blueprint(usuarios_bp)
    app.register_blueprint(recomendaciones_bp)
   # app.register_blueprint(neumaticos_bp)
    app.register_blueprint(citas_bp)