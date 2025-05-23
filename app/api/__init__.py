from .cadastro import api_bp as cadastro_api_bp
from .verificar_cpf import api_bp as verifica_cpf_api

def register_api(app):
    app.register_blueprint(cadastro_api_bp)
    app.register_blueprint(verifica_cpf_api)
