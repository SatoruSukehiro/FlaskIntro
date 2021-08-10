# Put your app in here.
from flask import Flask
from flask.globals import request
from operations import add,sub,mult,div
app = Flask(__name__)

@app.route('/add')
def run_add():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return f'{add(a,b)}'


@app.route('/sub')
def run_sub():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return f'{sub(a,b)}'

@app.route('/mult')
def run_mult():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return f'{mult(a,b)}'
@app.route('/div')
def run_div():
    a = int(request.args.get('a'))
    b= int(request.args.get('b'))
    return f'{div(a,b)}'

operators = {
    'add' : add,
    'sub' : sub,
    'mult': mult,
    'div': div
}


""" would like to have a better understanding of looping through this did get this outcome without taking a peak at the solution. """
@app.route("/math/<operator>")
def run_math(operator):
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    ran = operators[operator](a,b)
    return str(ran)