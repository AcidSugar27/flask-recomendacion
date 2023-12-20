from app import db

class Usuario(db.Model):
    __tablename__='usuarios'
    id_usuario = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100))
    numero_contacto = db.Column(db.String(15))




