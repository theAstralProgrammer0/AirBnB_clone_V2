#!/usr/bin/python3
"""This module sets up a Flask app"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def show_states():
    """Render the states_list.html page to display State instances"""
    states = storage.all()
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(self):
    """Removes SQLAlchemy session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
