#!/usr/bin/python3
"""
List all cities by their state
"""

from flask import Flask
from models.city import City
import os
from models import storage


app = Flask(__name__)

@app.route('/cities_by_states', strict_slashes)
def cities_by_state():
    """list cities by state"""
    all_cities = storage.all(City)
    if (os.getenv('HBNB_TYPE_STORAGE') == 'db'):
        use cities relationship
    else:

@app.teardown_appcontext
def close_session(request_or_smth):
    """close session"""
    storage.close()
