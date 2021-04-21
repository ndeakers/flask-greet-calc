# Put your app in here.
from flask import Flask, request
import operations

app = Flask(__name__)

@app.route('/add')
def add():
    """adds two query parameters together"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    sum = str(operations.add(a, b))

    return f"<html><body><h1>{sum}</h1></body></html>"

@app.route('/sub')
def sub():
    """subtracts two query parameters"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    sub = str(operations.sub(a, b))

    return f"<html><body><h1>{sub}</h1></body></html>"

@app.route('/mult')
def mult():
    """multiplies two query parameters"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    product = str(operations.mult(a, b))

    return f"<html><body><h1>{product}</h1></body></html>"

@app.route('/div')
def div():
    """divides two query parameters"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    div = str(operations.div(a, b))

    return f"<html><body><h1>{div}</h1></body></html>"
