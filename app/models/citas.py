from app import db


class Cita(db.Model):
    __tablename__ = 'citas'
    id_cita = db.Column(db.Integer, primary_key=True, autoincrement=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario'))
    fechacita = db.Column(db.Date)
    usuario = db.relationship('Usuario', backref=db.backref('citas', lazy=True))