# Put your app in here.
from flask import Flask, request
import operations

app = Flask(__name__)


@app.route('/add')
def add():
    """adds two query parameters together"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    sum = operations.add(a, b)

    return f"<html><body><h1>{sum}</h1></body></html>"


@app.route('/sub')
def sub():
    """subtracts two query parameters"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    sub = operations.sub(a, b)

    return f"<html><body><h1>{sub}</h1></body></html>"


@app.route('/mult')
def mult():
    """multiplies two query parameters"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    product = operations.mult(a, b)

    return f"<html><body><h1>{product}</h1></body></html>"


@app.route('/div')
def div():
    """divides two query parameters"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    div = operations.div(a, b)

    return f"<html><body><h1>{div}</h1></body></html>"


OPERATIONS = {
    "add": operations.add,
    "sub": operations.sub,
    "mult": operations.mult,
    "div": operations.div,
}


@app.route('/math/<operation>')
def math(operation):
    """calculates two query parameters based on operation requested"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    total = OPERATIONS[operation](a, b)

    return f"<html><body><h1>{total}</h1></body></html>"
