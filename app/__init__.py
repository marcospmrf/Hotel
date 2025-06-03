from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app(testing=False):
    app = Flask(__name__)

    if testing:
        # Configuração para testes, banco de dados em memória
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    else:
        # Pega o DATABASE_URL do ambiente para produção
        database_url = os.environ.get('DATABASE_URL')
        if database_url:
            app.config['SQLALCHEMY_DATABASE_URI'] = database_url
        else:
            # Banco local, usado apenas para desenvolvimento na máquina
            app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/Hotel'

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['TESTING'] = testing

    db.init_app(app)

    # Registro dos Blueprints (rotas HTML)
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

    # Registro de APIs REST
    from app.api import register_api
    register_api(app)

    # Importação dos modelos (apenas garante carregamento)
    from app.models import Usuario, Quarto, Reserva

    return app
