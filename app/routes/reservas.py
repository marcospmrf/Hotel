from flask import Blueprint, render_template
from app.models import Reserva  # <-- Importa o model correto

bp = Blueprint('reservas', __name__, url_prefix='/reservas')

@bp.route('/')
def reservas():
    reservas = Reserva.query.all()   # <-- Busca as reservas
    return render_template('reservas.html', reservas=reservas)  # <-- Passa para o template
