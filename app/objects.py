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
collection = db.objects

@app.route("/api/v1/objects", methods=['POST'])
def create_object():
    """
       Function to create new objects.
       """
    try:
        # Create new objects
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


@app.route("/api/v1/objects", methods=['GET'])
def fetch_object():
    """
       Function to fetch the objects.
       """
    try:
        query_params = helper_module.parse_query_params(request.query_string)
        if query_params:
            query = {k: int(v) if isinstance(v, str) and v.isdigit() else v for k, v in query_params.items()}
            records_fetched = collection.find(query)

            # Check if the records found
            if records_fetched.count() > 0:
                return dumps(records_fetched)
            else:
                return "", 404
        else:
            if collection.find().count > 0:
                return dumps(collection.find())
            else:
                return jsonify([])
    except:
        return "", 500

@app.route("/api/v1/objects/<objects_id>", methods=['POST'])
def update_object(objects_id):
    """
       Function to update the objects.
       """
    try:
        try:
            body = ast.literal_eval(json.dumps(request.get_json()))
        except:
            return "", 400

        records_updated = collection.update_one({"id": int(objects_id)}, body)

        if records_updated.modified_count > 0:

            return "", 200
        else:
            return "", 404
    except:
        return "", 500


@app.route("/api/v1/objects/<objects_id>", methods=['DELETE'])
def remove_object(objects_id):
    """
       Function to remove the objects.
       """
    try:
        delete_objects = collection.delete_one({"id": int(objects_id)})

        if delete_objects.deleted_count > 0 :
            return "", 204
        else:
            return "", 404
    except:
        return "", 500


@app.errorhandler(404)
def page_not_found(e):
    """Send message to the objects with notFound 404 status."""
    # Message to the objects
    message = {
        "err":
            {
                "msg": "This route is currently not supported. Please refer API documentation."
            }
    }
    # Making the message looks good
    resp = jsonify(message)
    # Sending OK response
    resp.status_code = 404
    # Returning the object
    return resp
