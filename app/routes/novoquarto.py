from flask import Blueprint, render_template

bp = Blueprint ('novoquarto', __name__, url_prefix = '/quarto')

@bp.route('/')
def novoquarto():
    return render_template ('cadastrarquarto.html')