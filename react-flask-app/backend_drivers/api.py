#!flask/bin/python

from flask import (
    Flask,
    render_template,
    jsonify
)

from retrieve_tweets import get_tweets

# Create the application instance
app = Flask(__name__, template_folder="templates")

@app.before_request
def before():
    print("This is executed BEFORE each request.")

# Create a URL route in our application for "/"
@app.route('/request/<string:location>/<string:keyword>/', methods=['GET'])
def home(location, keyword):
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
    hashtags = []
    
    # TODO: response will always be an empty object; must store tweets on stream from on_status method
    response = get_tweets(keywords)
    
    if len(response) > 0:
        status_code = 200
    else:
        status_code = 500

    return jsonify(response), status_code


# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(debug=True)