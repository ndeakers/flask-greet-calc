from flask import Flask
app = Flask(__name__)


@app.route('/welcome')
def welcome():
    """returns a greeting"""
    return '<html><body><h1>welcome</h1></body></html>'


@app.route('/welcome/<greet>')
def greeting(greet):
    """returns a greeting based on endpoint"""
    return f"<html><body><h1>welcome {greet}</h1></body></html>"
