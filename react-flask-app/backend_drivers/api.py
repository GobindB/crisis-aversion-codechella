#!venv/bin/python3

# TODO: DOCUMENTATION!! && TESTS

from flask import (
    Flask,
    render_template,
    jsonify
)

from retrieve_tweets import get_tweets
import numpy as np
import tensorflow as tf
from tensorflow import keras

import os

reconstructed_model = keras.models.load_model("my_model")

# Create the application instance
app = Flask(__name__, template_folder="templates",
            static_folder="../build", static_url_path='/home')


@app.route("/home")
def index():
    return app.send_static_file('index.html')


@app.errorhandler(404)
def not_found(e):
    return app.send_static_file('index.html')

# Create a URL route in our application for "/"


@app.route('/request/location=<string:location>&keywords=<string:keyword>&languages=<string:languages>', methods=['GET'])
def home(location, keyword, languages):
    """
    This function responds to the browser ULR
    localhost:5000/request/<location>/<keyword%20keyword%20keyword>

    where <______> represents a parameter passed to url
    and %20 is a delimeter splitting keywords and hashtags

    :return:        '
    """
    # return json serialized response and status code
    # return error code if json is NULL
    keywords = keyword.split("%20")
    location = [float(coordinate) for coordinate in location.split(",")]
    languages = languages.split(",")

    response = get_tweets(keywords, languages, location, reconstructed_model)

    if len(response) > 0:
        status_code = 200
    else:
        status_code = 500

    return jsonify(response), status_code


# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, port=os.environ.get('PORT', 80))
