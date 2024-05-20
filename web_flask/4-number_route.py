#!/usr/bin/python3
"""This module sets up a Flask application"""
from flask import Flask
from shlex import shlex


def shlx(txt, delim=' ', prefix='', suffix=''):
    """This function splits strings and prefixes or suffixes strings"""
    lexer = shlex(txt)
    lexer.whitespace += delim
    words = list(lexer)
    return prefix + ' '.join(words) + suffix


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
    return shlx(text, '_', 'C ')


@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    """This is the python endpoint function"""
    return shlx(text, '_', 'Python ')


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """This is the number endpoint function"""
    return str(n) + " is a number" if isinstance(n, int) else None



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
