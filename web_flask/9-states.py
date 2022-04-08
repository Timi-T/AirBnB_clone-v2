#!/usr/bin/python3
"""
Start airbnb web application with flask
"""


from flask import Flask, render_template
from models import storage
from models.state import State
import os


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def cities_in_state(id=None):
    """List all cities in a state"""
    all_states = storage.all(State)
    found = 0
    if id:
        for k, val in all_states.items():
            if val.id == id:
                state = val
                st_name = state.name
                found = 1
                break
        if found == 1:
            if os.getenv('HBNB_TYPE_STORAGE') != 'db':
                cities = state.cities()
            else:
                cities = state.cities
            ct_dict = {}
            for city in cities:
                ct_key = city.id
                ct_val = city.name
                ct_dict[ct_key] = ct_val
            ct_array = sorted(ct_dict.items(), key=lambda x: x[1])
            return render_template("9-states.html", cities=ct_array, state=st_name)
        else:
            return render_template("9-states.html", not_found='Not found!')
    else:
        dict_states = {}
        for key, val in all_states.items():
            st_key = val.id
            st_val = val.name
            dict_states[st_key] = st_val
        dict_states = sorted(dict_states.items(), key=lambda x: x[1])
        return render_template("9-states.html", states=dict_states)


@app.teardown_appcontext
def close_session(response_or_exc):
    """close sqlalchemy session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
