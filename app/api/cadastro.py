from flask import Blueprint, request, jsonify
from app import db
from app.models import Usuario
from datetime import datetime

api_bp = Blueprint('api_cadastro', __name__, url_prefix='/api/cadastro')

@api_bp.route('/', methods=['POST'])
def cadastrar_usuario():
    try:
        data = request.get_json()

        novo_usuario = Usuario(
            cpf=data.get('cpf'),
            nome=data.get('nome'),
            rg=data.get('rg'),
            telefone=data.get('telefone'),
            email=data.get('email'),
            data_nascimento=datetime.strptime(data.get('nascimento'), "%Y-%m-%d")
        )

        db.session.add(novo_usuario)
        db.session.commit()

        return jsonify({'mensagem': 'Cliente cadastrado com sucesso!', 'status': 'sucesso'}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'mensagem': f'Erro ao cadastrar: {str(e)}', 'status': 'erro'}), 400
