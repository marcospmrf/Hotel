from flask import Blueprint, render_template

bp = Blueprint('sair', __name__, url_prefix = '/sair')

@bp.route('/')
def sair():
    return render_template('login.html')