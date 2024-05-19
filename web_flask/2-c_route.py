#!/usr/bin/python3
"""This module sets up a Flask application"""
from flask import Flask
from shlex import shlex

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """This is the home endpoint function"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """This is the hbnb endpoint function"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """This is the c endpoint function"""
    lexer = shlex(text)
    lexer.whitespace += '_'
    words = list(lexer)
    return "C " + " ".join(words)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
