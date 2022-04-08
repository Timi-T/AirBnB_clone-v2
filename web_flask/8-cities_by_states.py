#!/usr/bin/python3
"""
List all cities by their state
"""

from flask import Flask, render_template
from models.city import City
from models.state import State
from models import storage
import os


app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_state():
    """list cities by state"""
    all_states = storage.all(State)
    states_cities = []
    for key, val in all_states.items():
        st_ct = []
        cities = []
        st_id = val.id
        st_name = val.name
        if os.getenv('HBNB_TYPE_STORAGE') != 'db':
            ct = []
            i = 0
            dict_ct = val.cities()
            for k, v in dict_ct.items():
                ct[i] = v
                i += 1
        else:
            ct = val.cities
        for city in ct:
            each_city = []
            each_city.append(city.id)
            each_city.append(city.name)
            cities.append(each_city)
        st_ct.append(st_id)
        st_ct.append(st_name)
        st_ct.append(cities)
        states_cities.append(st_ct)
    for each_cities in states_cities:
        if len(each_cities[2]) > 1:
            each_cities[2] = sorted(each_cities[2], key=lambda x: x[1])
    states_cities = sorted(states_cities, key=lambda x: x[1])
    return render_template("8-cities_by_states.html", states=states_cities)


@app.teardown_appcontext
def close_session(response_or_exc):
    """close session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
