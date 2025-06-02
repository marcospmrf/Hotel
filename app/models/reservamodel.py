from app import db
from app.models.usuariomodel import Usuario    
from app.models.quartomodel import Quarto      

class Reserva(db.Model):
    __tablename__ = 'reservas'

    id = db.Column(db.Integer, primary_key=True)
    hospede_cpf = db.Column(db.String(14), db.ForeignKey('usuario.cpf'), nullable=False)
    numero_quarto = db.Column(db.Integer, db.ForeignKey('quarto.numero_quarto'), nullable=False)
    checkin = db.Column(db.Date, nullable=False)
    checkout = db.Column(db.Date, nullable=False)
    valor = db.Column(db.Numeric(10, 2))
    forma_pagamento = db.Column(db.String(20))
    data_pagamento = db.Column(db.Date)
    status_pagamento = db.Column(db.String(10))

    hospede = db.relationship(Usuario, backref='reservas', lazy=True)
