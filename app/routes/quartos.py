from flask import Blueprint, request, jsonify, render_template
from app.models import Quarto
from app import db

bp = Blueprint('quartos', __name__, url_prefix='/quartos')

# Rota GET → usada por HTML (navegador)
@bp.route('/quartos', methods=["GET"])
def quartos():
    quartos_disponiveis = Quarto.query.all()  # Mostra todos, inclusive os indisponíveis
    return render_template('quartos.html', quartos=quartos_disponiveis)

# Rota POST → usada pela API
@bp.route('/', methods=["POST"])
def criar_quarto():
    dados = request.get_json()
    numero = dados.get("numero")
    tipo = dados.get("tipo")
    preco = dados.get("preco")

    return jsonify({
        "numero": numero,
        "tipo": tipo,
        "preco": preco
    }), 201
