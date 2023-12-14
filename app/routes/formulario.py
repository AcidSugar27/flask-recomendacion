from flask import Flask, render_template, request
from . import formulario_bp
from flask_sqlalchemy import SQLAlchemy
from app import db



class RespuestasNeumaticos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    frecuencia = db.Column(db.String(1))
    prioridad_manejo = db.Column(db.String(1))
    preferencia_vida_util = db.Column(db.String(1))
    preferencia_robustez = db.Column(db.String(1))
    porcentaje_rocoso = db.Column(db.Integer)
    porcentaje_solido = db.Column(db.Integer)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.ID_Usuario'))


@formulario_bp.route('/submit', methods=['POST'])

def submit():
    if request.method == 'POST':
        # Recopilar datos del formulario
        frecuencia = request.form['frecuencia']
        prioridad_manejo = request.form['prioridad_manejo']
        preferencia_vida_util = request.form['preferencia_vida_util']
        preferencia_robustez = request.form['preferencia_robustez']
        porcentaje_rocoso = int(request.form['porcentaje_rocoso'])
        porcentaje_solido = int(request.form['porcentaje_solido'])

        
        # Crear un nuevo objeto RespuestasNeumaticos
        nueva_respuesta = RespuestasNeumaticos(
            frecuencia=frecuencia,
            prioridad_manejo=prioridad_manejo,
            preferencia_vida_util=preferencia_vida_util,
            preferencia_robustez=preferencia_robustez,
            porcentaje_rocoso=porcentaje_rocoso,
            porcentaje_solido=porcentaje_solido
        )

        # Agregar la respuesta a la base de datos
        db.session.add(nueva_respuesta)
        db.session.commit()

        return 'Formulario enviado correctamente'



