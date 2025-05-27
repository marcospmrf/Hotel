from app import db

class Quarto(db.Model):
    __tablename__ = 'quarto'

    numero_quarto = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(50))
    descricao = db.Column(db.Text)
    preco_diaria = db.Column(db.Numeric(10, 2))
    imagem = db.Column(db.String(255))
    status = db.Column(db.String(20), default='disponivel')


    # Exemplo de relação inversa, se quiser acessar reservas: quarto.reservas
    reservas = db.relationship('Reserva', backref='quarto', lazy=True)
