from flask import render_template, request, redirect , url_for,session, Blueprint
from app import db
from app.models.usuarios import Usuario


usuarios_bp = Blueprint('usuarios', __name__)

@usuarios_bp.route('/')
def index():

    return render_template('inicio.html')



@usuarios_bp.route('/agregar_usuario', methods=['POST'])

def agregar_usuario():
    if request.method == 'POST':
        nombre = request.form['nombre']
        numero_contacto = request.form['numero_contacto']

        nuevo_usuario = Usuario(nombre=nombre, numero_contacto=numero_contacto)
        db.session.add(nuevo_usuario)
        db.session.commit()



        return render_template('formulario.html',nuevo_usuario=nuevo_usuario)



