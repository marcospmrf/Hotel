from flask import Blueprint, render_template

bp = Blueprint('financeiro', __name__, url_prefix = '/financeiro')

@bp.route('/')
def financeiro():
    return render_template('financeiro.html')