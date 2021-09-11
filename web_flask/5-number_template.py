#!/usr/bin/python3
"""Hello HBNB"""

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """ Show Hello HBNB!"""
    return ('Hello HBNB!')


@app.route('/hbnb', strict_slashes=False)
def index1():
    """Show HBNB"""
    return ('HBNB')


@app.route('/c/<text>', strict_slashes=False)
def index2(text):
    """Show C + text"""
    return ('C {}'.format(text.replace('_', ' ')))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def index3(text='is cool'):
    """Show Python + text"""
    return ('Python {}'.format(text.replace('_', ' ')))


@app.route('/number/<int:n>', strict_slashes=False)
def index4(n):
    """Show n is a number"""
    return ('{} is a number'.format(n))


@app.route('/number_template/<int:num>', strict_slashes=False)
def index5(num):
    """Show n is a number"""
    return render_template('5-number.html', n=num)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
