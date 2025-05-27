from flask import Blueprint, request, jsonify
from datetime import datetime, date
from app import db
from app.models import Reserva, Quarto, Usuario

api_reserva = Blueprint("api_reserva", __name__)

@api_reserva.route("/api/reservas", methods=["POST"])
def criar_reserva():
    try:
        data = request.get_json()

        nome = data["nome"]
        email = data["email"]
        telefone = data["telefone"]
        cpf = data["cpf"]
        numero_quarto = int(data["numero_quarto"])
        checkin = datetime.strptime(data["checkin"], "%Y-%m-%d").date()
        checkout = datetime.strptime(data["checkout"], "%Y-%m-%d").date()
        forma_pagamento = data["pagamento"]
        data_pagamento = date.today()
        status_pagamento = "Pendente"

        quarto = Quarto.query.get(numero_quarto)
        if not quarto:
            return jsonify({"erro": "Quarto não encontrado"}), 404

        if quarto.status != "disponivel":
            return jsonify({"erro": "Quarto não está disponível"}), 400

        dias = (checkout - checkin).days
        if dias <= 0:
            return jsonify({"erro": "Período inválido"}), 400

        valor = dias * float(quarto.preco_diaria)

        # Cria hóspede se não existir
        usuario = Usuario.query.get(cpf)
        if not usuario:
            usuario = Usuario(cpf=cpf, nome=nome, email=email, telefone=telefone)
            db.session.add(usuario)

        # Cria a reserva
        nova_reserva = Reserva(
            hospede_cpf=cpf,
            numero_quarto=numero_quarto,
            checkin=checkin,
            checkout=checkout,
            valor=valor,
            forma_pagamento=forma_pagamento,
            data_pagamento=data_pagamento,
            status_pagamento=status_pagamento
        )
        db.session.add(nova_reserva)

        # Atualiza status do quarto
        quarto.status = "indisponivel"
        db.session.add(quarto)

        db.session.commit()

        return jsonify({
            "mensagem": "✅ Reserva registrada com sucesso!",
            "quarto": numero_quarto,
            "valor": valor
        }), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"erro": str(e)}), 500
