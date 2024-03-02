#!/usr/bin/python3
"""
Flask app to generate a complete HTML
page containing location/amenity dropdown
menus and rental listings.

This Flask application serves as a backend
for generating a dynamic HTML page with location/amenity
dropdown menus and rental listings.
The page is rendered using the Flask `render_template` function,
which takes an HTML template file and injects dynamic data into it.
"""

from flask import Flask, render_template
from models import storage
import uuid

app = Flask('web_dynamic')
app.url_map.strict_slashes = False

@app.route('/4-hbnb')
def display_hbnb():
    """
    Generate a page with a dropdown menu of states/cities.

    This route handler generates a complete HTML page with
    a dropdown menu for selecting states and cities.
    It fetches the necessary data from the storage module,
      which is responsible for interacting with the
      underlying database or file storage.

    The `storage.all` method is used to retrieve all the states,
    amenities, and places from the database. These data are then passed
    as arguments to the `render_template` function, along with
      a randomly generated `cache_id`,
      which ensures that the page is reloaded with fresh data.

    Returns:
        str: The rendered HTML page with the dynamic data injected.
    """
    try:
        # Retrieve data from storage
        states = storage.all('State')
        amenities = storage.all('Amenity')
        places = storage.all('Place')

        # Generate cache_id for cache-busting
        cache_id = uuid.uuid4()

        # Render the HTML template with the dynamic data
        return render_template('4-hbnb.html',
                               states=states,
                               amenities=amenities,
                               places=places,
                               cache_id=cache_id)
    except Exception as e:
        # Handle any exceptions that occur during execution
        return str(e)


@app.teardown_appcontext
def teardown_db(*args, **kwargs):
    """
    Close the database or file storage.

    This function is called when the Flask application
    context is torn down. It ensures that the database
      connection or file storage is properly closed,
      preventing resource leaks.

    Args:
        *args: Variable-length argument list.
        **kwargs: Arbitrary keyword arguments.
    """
    storage.close()


if __name__ == '__main__':
    try:
        # Start the Flask development server
        app.run(host='0.0.0.0', port=5000)
    except Exception as e:
        # Handle any exceptions that occur during execution
        print(str(e))
