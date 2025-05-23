from flask import Blueprint, render_template

bp = Blueprint('quartos', __name__, url_prefix='/quartos')

@bp.route('/')
def quartos():
    return render_template('quartos.html')
