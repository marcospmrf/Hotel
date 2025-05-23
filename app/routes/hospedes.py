from flask import Blueprint, render_template

bp = Blueprint('hospedes', __name__, url_prefix = '/hospedes')

@bp.route('/')
def hospedes():
    return render_template('hospedes.html')