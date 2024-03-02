#!/usr/bin/python3
"""
Flask app to generate a complete HTML page
containing location/amenity
dropdown menus and rental listings.
"""

from flask import Flask, render_template
from models import storage
import uuid

app = Flask('web_dynamic')
app.url_map.strict_slashes = False


@app.route('/100-hbnb')
def display_hbnb():
    """
    Generate a page with dropdown menus of
    states/cities and amenities.

    This route handler generates a complete
      HTML page with dropdown menus for selecting
      states/cities and amenities.
      It fetches the necessary data from the storage module,
        which is responsible for interacting
        with the underlying database or file storage.

    The `storage.all` method is used to retrieve all the states
      and amenities from the database. These data,
        along with a randomly generated `cache_id`,
        are then passed as arguments to the `render_template` function.

    Returns:
        str: The rendered HTML page with the dynamic data injected.
    """
    try:
        states = storage.all('State')
        amenities = storage.all('Amenity')
        cache_id = uuid.uuid4()
        return render_template('100-hbnb.html',
                               states=states,
                               amenities=amenities,
                               cache_id=cache_id)
    except Exception as e:
        # Handle any exceptions that occur during execution
        return str(e)


@app.teardown_appcontext
def teardown_db(*args, **kwargs):
    """
    Close the database or file storage.

    This function is called when the
      Flask application context is torn down.
      It ensures that the database connection or
        file storage is properly closed,
          preventing resource leaks.

    Args:
        *args: Variable-length argument list.
        **kwargs: Arbitrary keyword arguments.
    """
    storage.close()


if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000)
    except Exception as e:
        # Handle any exceptions that occur during execution
        print(str(e))
