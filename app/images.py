"""This module will serve the api request."""

from config import client
from app import app
from bson.json_util import dumps
from flask import request, jsonify
import json
import ast
import imp


# Import the helpers module
helper_module = imp.load_source('*', './app/helpers.py')

# Select the database
db = client.messier_registry
# Select the collection
catalog = db["catalog"]


@app.route("/api/v1/images/<objects_id>", methods=['GET'])
def fetch_image(objects_id):
    """
       Function to fetch the images.
       """
    try:
        if catalog.find_one({ "messier": objects_id }).count:
            return jsonify(json.loads(dumps(catalog.find_one({ "messier": objects_id })))['image']), 200
        else:
            return 'Not found', 404
    except ValueError:
        return "Internal server Error", 500
