from flask import Blueprint, render_template
from app.models import Quarto

bp = Blueprint('hospedagem', __name__, url_prefix='/hospedagem')

@bp.route('/<int:numero_quarto>')
def hospedagem(numero_quarto):
    quarto = Quarto.query.get_or_404(numero_quarto)
    return render_template('hospedagem.html', quarto=quarto, numero_quarto=numero_quarto)

