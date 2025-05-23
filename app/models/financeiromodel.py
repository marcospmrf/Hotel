from app import db

class Financeiro(db.Model):
    __tablename__ = 'financeiro'
    __table_args__ = {'extend_existing': True}

    reserva_id = db.Column(db.Integer, primary_key=True)
    hospede = db.Column(db.String(100))
    numero_quarto = db.Column(db.Integer)
    valor = db.Column(db.Numeric(10, 2))
    forma_pagamento = db.Column(db.String(20))
    data_pagamento = db.Column(db.Date)
    status_pagamento = db.Column(db.String(10))

    def __repr__(self):
        return f'<Financeiro reserva={self.reserva_id}>'
