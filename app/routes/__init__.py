from flask import Blueprint

main_bp = Blueprint('main', __name__)
usuarios_bp = Blueprint('usuarios', __name__)
formulario_bp = Blueprint('formulario', __name__)


from . import main, usuarios, formulario
