from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/Hotel'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # Importações de rotas (BluePrints)
    from .routes.home import bp as home
    from .routes.quartos import bp as quartos
    from .routes.financeiro import bp as financeiro
    from .routes.configuracoes import bp as configuracoes
    from .routes.hospedagem import bp as hospedagem
    from .routes.hospedes import bp as hospedes
    from .routes.reservas import bp as reservas
    from .routes.sair import bp as sair
    from .routes.cadastrocliente import bp as cadastrocliente
    from .routes.alugar import bp as alugar
    from .routes.novoquarto import bp as quarto

    # Registro dos blueprints (rotas HTML)
    app.register_blueprint(home)
    app.register_blueprint(quartos)
    app.register_blueprint(financeiro)
    app.register_blueprint(configuracoes)
    app.register_blueprint(hospedagem)
    app.register_blueprint(hospedes)
    app.register_blueprint(reservas)
    app.register_blueprint(sair)
    app.register_blueprint(cadastrocliente)
    app.register_blueprint(alugar)
    app.register_blueprint(quarto)

    # ------------------ APIs REST (pasta /api) ------------------
    from app.api import register_api
    register_api(app)
    


    # ------------------ banco de dados (modelos) ------------------
    from app.models import Usuario
    from app.models import Quarto
    from app.models import Reserva

    return app
