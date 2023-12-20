from app import db

class Neumatico(db.Model):
    __tablename__ = 'neumaticos'
    id_neumatico = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tipo = db.Column(db.String(50))
    c_dureza = db.Column(db.String(50))
    c_conduccion = db.Column(db.String(50))
    c_estructura = db.Column(db.String(50))
    c_ambiente = db.Column(db.String(50))
    c_alturaanchura = db.Column(db.String(50))
    c_tipovehiculo = db.Column(db.String(50))
