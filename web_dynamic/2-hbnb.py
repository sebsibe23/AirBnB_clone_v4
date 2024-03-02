#!/usr/bin/python3
"""
Description: Flask app to generate a complete HTML page containing
location/amenity dropdown menus and rental listings.

"""

from flask import Flask, render_template
from models import storage
import uuid

app = Flask('web_dynamic')
app.url_map.strict_slashes = False


@app.route('/2-hbnb')
def display_hbnb():
    """Generate a page with a dropdown menu of states/cities"""
    try:
        states = storage.all('State')
        amenities = storage.all('Amenity')
        places = storage.all('Place')
        cache_id = uuid.uuid4()
        return render_template('2-hbnb.html',
                               states=states,
                               amenities=amenities,
                               places=places,
                               cache_id=cache_id)
    except Exception as e:
        # Handle any exceptions that occur during execution
        return str(e)


@app.teardown_appcontext
def teardown_db(*args, **kwargs):
    """Close the database or file storage"""
    storage.close()


if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000)
    except Exception as e:
        # Handle any exceptions that occur during execution
        print(str(e))
