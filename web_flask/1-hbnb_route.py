#!/usr/bin/python3
"""Hello HBNB"""

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """ Show Hello HBNB!"""
    return ('Hello HBNB!')


@app.route('/hbnb', strict_slashes=False)
def index1():
    """Show HBNB"""
    return ('HBNB')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
