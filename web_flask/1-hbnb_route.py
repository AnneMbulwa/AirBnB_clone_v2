#!/usr/bin/python3
"""display hello hbnb and hbnb"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """display hbnb"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """display hbnb"""
    return 'HBNB'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
