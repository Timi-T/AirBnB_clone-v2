#!/usr/bin/python3
"""
Render the hbnb static page
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
import os


app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """function to render the static filters page"""

    all_states = storage.all(State)
    all_amenities = storage.all(Amenity)
    st = []
    amn = []
    for k, v in all_states.items():
        st.append(v)
    for k, v in all_amenities.items():
        amn.append(v)
    return render_template('10-hbnb_filters.html', states=st, amenities=amn)


@app.teardown_appcontext
def close_session(response_or_exc):
    """close mysqlalchemy session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
