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
collection = db.articles

@app.route("/api/v1/articles", methods=['POST'])
def create_article():
    """
       Function to create new articles.
       """
    try:
        # Create new articles
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

@app.route("/api/v1/articles/s/<text_entry>", methods=['GET'])
def fetch_article():
    """
       Function to search in the articles content.
       """
    try
        query_params = helper_module.parse_query_params(request.query_string)
        if query_params:
            query = {k: int(v) if isinstance(v, str) and v.isdigit() else v for k, v in query_params.items()}
            # To  add TODO
            records_fetched = collection.find({"$text": {"$search": text_entry}})

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

@app.route("/api/v1/articles", methods=['GET'])
def fetch_article():
    """
       Function to fetch the articles.
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

@app.route("/api/v1/articles/<articles_id>", methods=['POST'])
def update_article(articles_id):
    """
       Function to update the articles.
       """
    try:
        try:
            body = ast.literal_eval(json.dumps(request.get_json()))
        except:
            return "", 400

        records_updated = collection.update_one({"id": int(articles_id)}, body)

        if records_updated.modified_count > 0:

            return "", 200
        else:
            return "Article not found", 404
    except:
        return "Internal server error", 500


@app.route("/api/v1/articles/<articles_id>", methods=['DELETE'])
def remove_article(articles_id):
    """
       Function to remove the articles.
       """
    try:
        delete_articles = collection.delete_one({"id": int(articles_id)})

        if delete_articles.deleted_count > 0 :
            return "", 204
        else:
            return "", 404
    except:
        return "Internal server error", 500

