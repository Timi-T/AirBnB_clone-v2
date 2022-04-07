#!/usr/bin/python3
"""
Simple flask application
"""

from flask import Flask, render_template


app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    """index page for url"""
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """return HBNB for url"""
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """take in string as parameter from url"""
    return 'C ' + text.replace('_', ' ')

@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """take in string as parameter from url with default value"""
    return 'Python ' + text.replace('_', ' ')

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """take in integer as parameter from url"""
    return str(n) + ' is a number'

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """render a html template"""
    return render_template("5-number.html", num=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
