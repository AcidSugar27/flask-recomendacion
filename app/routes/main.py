from flask import  render_template
from . import main_bp


@main_bp.route("/")
def index():

    return render_template("inicio.html")

@main_bp.route("/formulario")
def index1():

    return render_template("formulario.html")






