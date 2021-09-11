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
    """Display a page only if n is a num"""
    return render_template('5-number.html', n=num)


@app.route('/number_odd_or_even/<int:num>', strict_slashes=False)
def index6(num):
    """Show if num is odd or even in the page html"""
    if num % 2 == 0:
        return render_template('6-number_odd_or_even.html', n=num, m='is even')
    else:
        return render_template('6-number_odd_or_even.html', n=num, m='is odd')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
