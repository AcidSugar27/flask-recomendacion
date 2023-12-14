from flask import render_template, request
from flask_sqlalchemy import SQLAlchemy
from . import usuarios_bp
from app import db



class Usuarios(db.Model):
    ID_Usuario = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Nombre = db.Column(db.String(255))
    NumeroContacto = db.Column(db.String(20))
    respuestas = db.relationship('RespuestasNeumaticos', backref='usuario', lazy=True)

@usuarios_bp.route('/agregar_usuario', methods=['POST'])

def agregar_usuario():
    if request.method == 'POST':
        nombre = request.form['Nombre']
        numero_contacto = request.form['NumeroContacto']

        nuevo_usuario = Usuarios(Nombre=nombre, NumeroContacto=numero_contacto)
        db.session.add(nuevo_usuario)
        db.session.commit()

        return 'Usuario agregado con éxito'
