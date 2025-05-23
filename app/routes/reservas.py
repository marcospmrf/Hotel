from flask import Blueprint, render_template

bp = Blueprint('reservas', __name__, url_prefix = '/reservas')


@bp.route('/')
def reservas():
    return render_template('reservas.html')