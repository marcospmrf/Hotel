from flask import Blueprint, render_template

bp = Blueprint('configuracoes', __name__, url_prefix = '/configuracoes')

@bp.route('/')
def configuracoes():
    return render_template('configuracao.html')