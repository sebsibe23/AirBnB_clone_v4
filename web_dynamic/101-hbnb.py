#!/usr/bin/python3
"""
Flask App that integrates with
AirBnB static HTML Template

"""

from flask import Flask, render_template, url_for
from models import storage
import uuid

# Flask setup
app = Flask(__name__)
app.url_map.strict_slashes = False
port = 5000
host = '0.0.0.0'


@app.teardown_appcontext
def teardown_db(exception):
    """
    After each request, this method calls .close() (i.e. .remove()) on
    the current SQLAlchemy Session.
    """
    try:
        storage.close()
    except Exception as e:
        # Handle any exceptions that occur during execution
        print(str(e))


@app.route('/101-hbnb')
def hbnb_filters(the_id=None):
    """
    Handles request to custom template with states, cities, and amenities.
    """
    try:
        # Retrieve data from the storage module
        state_objs = storage.all('State').values()
        states = dict([state.name, state] for state in state_objs)
        amens = storage.all('Amenity').values()
        places = storage.all('Place').values()
        users = dict([user.id, "{} {}".format(user.first_name, user.last_name)]
                     for user in storage.all('User').values())

        # Render the HTML template with the dynamic data
        return render_template('101-hbnb.html',
                               cache_id=uuid.uuid4(),
                               states=state_objs,
                               amens=amens,
                               places=places,
                               users=users)
    except Exception as e:
        # Handle any exceptions that occur during execution
        return str(e)


if __name__ == "__main__":
    """
    Main Flask App
    """
    try:
        app.run(host=host, port=port)
    except Exception as e:
        # Handle any exceptions that occur during execution
        print(str(e))
