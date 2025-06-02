from app import db

class Usuario(db.Model):
    __tablename__ = 'usuario'  

    cpf = db.Column(db.String(14), primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    rg = db.Column(db.String(20))
    telefone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), unique=True)
    data_nascimento = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f'<Usuario {self.nome} - CPF {self.cpf}>'
