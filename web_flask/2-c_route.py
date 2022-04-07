#!/usr/bin/python3
"""
Simple flask application
"""

from flask import Flask


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
    """take in a parameter from url"""
    return 'C ' + text.replace('_', ' ')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
