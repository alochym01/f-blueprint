from flask import Blueprint

cdr = Blueprint('cdr', __name__)

@cdr.route('/')
def cdr_index():
    return "cdr_index"

@cdr.route('/create')
def cdr_create():
    return "cdr_create"