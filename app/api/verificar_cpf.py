from flask import Blueprint, jsonify
from app.models import Usuario  
from app import db  
import re  # para limpar o CPF

api_bp = Blueprint('api_verificar_cpf', __name__, url_prefix='/api')

@api_bp.route('/verificar-cpf/<cpf>', methods=['GET'])
def verificar_cpf(cpf):
    cpf_limpo = re.sub(r'\D', '', cpf)

    # Valida se tem exatamente 11 dígitos
    if len(cpf_limpo) != 11:
        return jsonify({'existe': False})

    # Consulta o banco com CPF limpo
    usuario = Usuario.query.filter_by(cpf=cpf_limpo).first()

    return jsonify({'existe': bool(usuario)})
