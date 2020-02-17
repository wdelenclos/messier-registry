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
articles = db["articles"]

# -------------------- GET messier object

@app.route("/api/v1/objects", methods=['GET'])
def fetch_object():
    """
       Function to fetch the objects.
       """
    try:
        mydoc = catalog.find()
        for x in mydoc:
            print(x)
        if catalog.find().count:
            return jsonify(json.loads(dumps(catalog.find()))), 200
        else:
            return 'Not found', 404
    except ValueError:
        return "Internal server Error", 500


@app.route("/api/v1/objects/<objects_id>", methods=['GET'])
def get_object(objects_id):
    """
       Function to fetch the objects.
       """
    try:
        if catalog.find_one({ "messier": objects_id }):
            return jsonify(json.loads(dumps({'object' : catalog.find_one({ "messier": objects_id }), 'articles' : articles.find({"ngc" : catalog.find_one({ "messier": objects_id })['ngc']})}))), 200
        else:
            return 'Not found', 404
    except ValueError:
        return "Internal server Error", 500


@app.route("/api/v1/objects/q/", methods=['GET'])
def get_object_with_params():
    """
       Function to fetch object with query params.
       """
    try:
        if request.args:
            queryDictionary = request.args.copy().to_dict()
            if catalog.find(queryDictionary).count:
                return jsonify(json.loads(dumps(catalog.find(queryDictionary)))), 200
            else: 
                return 'Not found', 404
    except ValueError:
        return "Internal server Error", 500


# -------------------- POST a messier object

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

        records_updated = catalog.update_one({"id": int(objects_id)}, body)

        if records_updated.modified_count > 0:

            return "", 200
        else:
            return 'Not found', 404
    except:
        return "Internal server error", 500

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

        record_created = catalog.insert(body)

        # Prepare the response
        if isinstance(record_created, list):
            # Return list of Id of the newly created item
            return dumps([str(v) for v in record_created]), 201
        else:
            # Return Id of the newly created item
            return jsonify(str(record_created)), 201
    except:
        # Error while trying to create the resource
        # Add message for debugging purpose
        return "", 500


# -------------------- DELETE a messier object

@app.route("/api/v1/objects/<objects_id>", methods=['DELETE'])
def remove_object(objects_id):
    """
       Function to remove the objects.
       """
    try:
        delete_objects = catalog.delete_one({"id": int(objects_id)})

        if delete_objects.deleted_count > 0 :
            return "", 204
        else:
            return "", 404
    except:
        return "Internal server error", 500
