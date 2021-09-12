#!/usr/bin/python3
""" List all state """

from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/states_list', strict_slashes = False)
def states_list():
    """show a HTML all the states"""
    states = list(storage.all(State).values())
    return (render_template('7-states_list.html', all_states=states))


@app.teardown_appcontext
def close(self):
    """function that call close method"""
    storage.close()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
