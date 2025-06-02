from flask import Blueprint, jsonify
from app import db
from app.models import Reserva, Quarto

api_cancelar_reserva = Blueprint("api_cancelar_reserva", __name__)

@api_cancelar_reserva.route("/api/reservas/<int:reserva_id>/cancelar", methods=["POST"])
def cancelar_reserva(reserva_id):
    try:
        reserva = Reserva.query.get(reserva_id)
        if not reserva:
            return jsonify({"erro": "Reserva não encontrada"}), 404

        # Busca o quarto reservado
        quarto = Quarto.query.get(reserva.numero_quarto)
        if quarto:
            quarto.disponivel = True  # <- Aqui libera o quarto
            db.session.add(quarto)

        # Deleta a reserva
        db.session.delete(reserva)
        db.session.commit()

        return jsonify({"mensagem": "✅ Reserva cancelada e quarto liberado!"}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"erro": str(e)}), 500
