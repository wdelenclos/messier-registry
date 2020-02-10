"""This module will serve the api request."""

from config import client, sources
from index import index
from app import app
from bson.json_util import dumps
from flask import request, jsonify
import json
import ast
import imp

# set the project root directory as the static folder, you can set others.



# Import the helpers module
helper_module = imp.load_source('*', './app/helpers.py')

# Select the database
db = client.restfulapi
# Select the collection
collection = db.users

@app.route('/')
def root():
    return index

@app.route("/api/v1/")
def get_initial_response():
    """Welcome message for the Messier registry."""
    # Message to the user
    message = {
        'apiVersion': 'v1.0',
        'status': '200',
        'message': 'Welcome to the Space Object Registry API. Refer to the documentation on https://github.com/wdelenclos/messier-registry.',
        'sources' : sources
    }
    # Making the message looks good
    resp = jsonify(message)
    # Returning the object
    return resp

@app.errorhandler(404)
def page_not_found(e):
    """Send message to the articles with notFound 404 status."""
    # Message to the articles
    message = {
        "err":
            {
                "msg": "This route is currently not supported. Please refer API documentation (on Github https://github.com/wdelenclos/messier-registry.)"
            }
    }
    # Making the message looks good
    resp = jsonify(message)
    # Sending OK response
    resp.status_code = 404
    # Returning the article
    return resp
