from flask import Blueprint, render_template

bp = Blueprint('alugar', __name__, url_prefix = '/alugar')

@bp.route('/')
def alugar():
    return render_template('alugar.html')