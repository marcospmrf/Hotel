from flask import Blueprint, render_template

bp = Blueprint('hospedagem', __name__, url_prefix = '/hospedagem')

@bp.route('/')
def hospedagem():
    return render_template('hospedagem.html')