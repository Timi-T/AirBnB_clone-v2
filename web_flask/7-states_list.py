#!/usr/bin/python3
"""
Start airbnb web application with flask
"""


from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """List all the states in the database"""
    all_states = storage.all(State)
    dict_states = {}
    for key, val in all_states.items():
        st_key = val.id
        st_val = val.name
        dict_states[st_key] = st_val
    dict_states = sorted(dict_states.items(), key=lambda x: x[1])
    return render_template("7-states_list.html", states=dict_states)


@app.teardown_appcontext
def close_session(response_or_exc):
    """close sqlalchemy session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
