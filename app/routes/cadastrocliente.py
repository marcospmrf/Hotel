from flask import Blueprint, render_template

bp = Blueprint('cadastro', __name__, url_prefix='/cadastro')

@bp.route('/', methods=['GET', 'POST'])
def cadastro():
  
    return render_template('cadastrocliente.html')
