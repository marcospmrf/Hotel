from flask import Blueprint, render_template
from app.models import Reserva, Usuario
from datetime import date

bp = Blueprint('hospedes', __name__, url_prefix='/hospedes')

@bp.route('/')
def hospedes():
    reservas = Reserva.query.join(Usuario, Reserva.hospede_cpf == Usuario.cpf).all()

    return render_template('hospedes.html', reservas=reservas)
