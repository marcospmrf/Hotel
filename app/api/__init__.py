from .cadastro import api_bp as cadastro_api_bp
from .verificar_cpf import api_bp as verifica_cpf_api
from .quartos import api_bp as api_quartos
from .reservas import api_reserva
from .cancelar import api_cancelar_reserva

def register_api(app):
    app.register_blueprint(cadastro_api_bp)
    app.register_blueprint(verifica_cpf_api)
    app.register_blueprint(api_quartos)
    app.register_blueprint(api_reserva)
    app.register_blueprint(api_cancelar_reserva)