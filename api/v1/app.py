#!/usr/bin/python3
"""
Flask Application: AirBnB clone Restful API

"""

from models import storage
from api.v1.views import app_views
from os import environ
from flask import Flask, render_template, make_response, jsonify
from flask_cors import CORS
from flasgger import Swagger
from flasgger.utils import swag_from

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def close_db(error):
    """Close the database connection"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """Handle 404 Error"""
    return make_response(jsonify({'error': "Not found"}), 404)


app.config['SWAGGER'] = {
    'title': 'AirBnB clone Restful API',
    'uiversion': 3
}

Swagger(app)


if __name__ == "__main__":
    """Main Function"""
    try:
        host = environ.get('HBNB_API_HOST')
        port = environ.get('HBNB_API_PORT')
        if not host:
            host = '0.0.0.0'
        if not port:
            port = '5000'
        app.run(host=host, port=port, threaded=True)
    except Exception as e:
        # Handle any exceptions that occur during execution
        print(str(e))
