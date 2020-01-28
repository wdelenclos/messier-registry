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
db = client.restfulapi
# Select the collection
collection = db.images

@app.route("/api/v1/images", methods=['POST'])
def create_image():
    """
       Function to create new images.
       """
    try:
        # Create new images
        try:
            body = ast.literal_eval(json.dumps(request.get_json()))
        except:
            # Bad request as request body is not available
            # Add message for debugging purpose
            return "", 400

        record_created = collection.insert(body)

        # Prepare the response
        if isinstance(record_created, list):
            # Return list of Id of the newly created item
            return jsonify([str(v) for v in record_created]), 201
        else:
            # Return Id of the newly created item
            return jsonify(str(record_created)), 201
    except:
        # Error while trying to create the resource
        # Add message for debugging purpose
        return "", 500


@app.route("/api/v1/images", methods=['GET'])
def fetch_image():
    """
       Function to fetch the images.
       """
    try:
        query_params = helper_module.parse_query_params(request.query_string)
        if query_params:
            query = {k: int(v) if isinstance(v, str) and v.isdigit() else v for k, v in query_params.items()}
            records_fetched = collection.find(query)

            # Check if the records found
            if records_fetched.count():
                return dumps(records_fetched)
            else:
                return "", 404
        else:
            if collection.find().count:
                return dumps(collection.find())
            else:
                return jsonify([])
    except:
        return "Internal server error", 500

@app.route("/api/v1/images/<images_id>", methods=['POST'])
def update_image(images_id):
    """
       Function to update the images.
       """
    try:
        try:
            body = ast.literal_eval(json.dumps(request.get_json()))
        except:
            return "", 400

        records_updated = collection.update_one({"id": int(images_id)}, body)

        if records_updated.modified_count > 0:

            return "", 200
        else:
            return "image not found", 404
    except:
        return "Internal server error", 500


@app.route("/api/v1/images/<images_id>", methods=['DELETE'])
def remove_image(images_id):
    """
       Function to remove the images.
       """
    try:
        delete_images = collection.delete_one({"id": int(images_id)})

        if delete_images.deleted_count > 0 :
            return "", 204
        else:
            return "", 404
    except:
        return "Internal server error", 500

