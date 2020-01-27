import pymongo

from routes.object import ObjectList, Object
from flask import Flask, request
from flask_restplus import Api, Resource

app = Flask(__name__)

@api.route("/object/")
objectList = ObjectList()

@api.route("/object/<string:title>")
object = Object()

api = Api(app=app, version='0.1', title='Space Object Registry Api', description='The Messier Space Object Registry based on Messier List.', validate=True)

app.run(port= 8887, host= 'localhost')