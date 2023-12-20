from app import db

class Recomendacion(db.Model):
    __tablename__ = 'recomendaciones'
    id_recomendacion = db.Column(db.Integer, primary_key=True, autoincrement=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario'))
    dureza_caucho = db.Column(db.String(50))
    estilo_conduccion = db.Column(db.String(50))
    estructura_neumatico = db.Column(db.String(50))
    tipo_ambiente = db.Column(db.String(50))
    altura_anchura = db.Column(db.String(50))
    tipo_vehiculo = db.Column(db.String(50))





