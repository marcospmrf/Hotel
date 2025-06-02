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

        # Busca o quarto
        quarto = Quarto.query.get(numero_quarto)
        if not quarto:
            return jsonify({"erro": "Quarto não encontrado"}), 404

        dias = (checkout - checkin).days
        if dias <= 0:
            return jsonify({"erro": "Período inválido"}), 400

        valor = dias * float(quarto.preco_diaria)

        # 🚨 Verificar conflito de datas
        conflito = Reserva.query.filter(
            Reserva.numero_quarto == numero_quarto,
            Reserva.checkin < checkout,
            Reserva.checkout > checkin
        ).first()

        if conflito:
            return jsonify({"erro": "Já existe uma reserva para esse quarto nesse período."}), 400

        # Cadastrar ou atualizar o usuário
        usuario = Usuario.query.get(cpf)
        if not usuario:
            usuario = Usuario(cpf=cpf, nome=nome, email=email, telefone=telefone)
            db.session.add(usuario)
        else:
            usuario.nome = nome
            usuario.email = email
            usuario.telefone = telefone
            db.session.add(usuario)

        # Criar nova reserva
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

        # ⚠️ REMOVE isso! Não vamos alterar o status do quarto!
        # quarto.status = "indisponivel"
        # db.session.add(quarto)

        db.session.commit()

        return jsonify({
            "mensagem": "✅ Reserva registrada com sucesso!",
            "quarto": numero_quarto,
            "valor": valor
        }), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"erro": str(e)}), 500
