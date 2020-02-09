import json 
import pymongo
from pymongo import MongoClient
import os



client = MongoClient('mongodb://localhost:27017')
db = client['messier_registry']


class PushObjectsToBD:
    """This class push all objects in the db """


    def __init__(self):
        pass


    def get_objects(self):
        with open('catalogue-de-messier.json') as json_file:
            datas = json.load(json_file)
            for obj in datas:
                current_object = obj['fields']
                db.catalog.insert(current_object)


PushObjectsToBD = PushObjectsToBD()
PushObjectsToBD.get_objects()