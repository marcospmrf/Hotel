from flask import Blueprint, render_template
from datetime import date
from app import db
from app.models import Quarto, Reserva

bp = Blueprint('home', __name__)

@bp.route('/')
def home():
    hoje = date.today()

    
    total_quartos = Quarto.query.count()

    subquery = db.session.query(Reserva.numero_quarto).filter(
        Reserva.checkin <= hoje,
        Reserva.checkout >= hoje
    )
    quartos_disponiveis = Quarto.query.filter(~Quarto.numero_quarto.in_(subquery)).count()

    
    reservas_hoje = Reserva.query.filter(Reserva.checkin == hoje).count()

    
    hospedes_no_hotel = Reserva.query.filter(
        Reserva.checkin <= hoje,
        Reserva.checkout >= hoje
    ).count()

    return render_template(
        "principal.html",
        total_disponiveis=quartos_disponiveis,
        total_quartos=total_quartos,
        reservas_hoje=reservas_hoje,
        hospedes_no_hotel=hospedes_no_hotel
    )
