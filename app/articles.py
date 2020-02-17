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
collection = db["articles"]

# -------------------- GET article

@app.route("/api/v1/articles/s/<text_entry>", methods=['GET'])
def fetch_article(text_entry):
    """
       Function to search in the articles content.
       """
    try:
        if collection.find({"$text": {"$search": text_entry}}).count:
            return jsonify(json.loads(dumps(collection.find({"$text": {"$search": text_entry}})))), 200
        else:
            return 'Not found', 404
    except:
        return "Internal server error", 500

@app.route("/api/v1/articles", methods=['GET'])
def fetch_articles():
    """
       Function to fetch the articles.
       """
    try:
        if collection.find().count:
            return jsonify(json.loads(dumps(collection.find()))), 200
        else:
            return 'Not found', 404
    except:
        return "Internal server error", 500


@app.route("/api/v1/articles/<ngc_id>", methods=['GET'])
def get_articles(ngc_id):
    """
       Function to fetch the objects.
       """
    try:
        if collection.find_one({ "ngc": ngc_id }):
            return jsonify(json.loads(dumps(collection.find_one({ "ngc": ngc_id })))), 200
        else:
            return 'Not found', 404
    except ValueError:
        return "Internal server Error", 500


@app.route("/api/v1/articles/q/", methods=['GET'])
def get_articles_with_params():
    """
       Function to fetch articles with query params.
       """
    try:
        if request.args:
            queryDictionary = request.args.copy().to_dict()
            if collection.find(queryDictionary).count:
                return jsonify(json.loads(dumps(collection.find(queryDictionary)))), 200
            else: 
                return 'Not found', 404
    except ValueError:
        return "Internal server Error", 500

# -------------------- POST an article

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

# -------------------- DELETE an article

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

