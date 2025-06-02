from flask import Blueprint, render_template, request

bp = Blueprint('alugar', __name__, url_prefix='/alugar')

@bp.route('/')
def alugar():
    numero_quarto = request.args.get('quarto')
    cpf = request.args.get('cpf')
    return render_template('alugar.html', numero_quarto=numero_quarto, cpf=cpf)
