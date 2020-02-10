import json 
import pymongo
from pymongo import MongoClient
import os



client = MongoClient('mongodb://localhost:27017')
db = client['messier_registry']


class PushObjectsToDB:
    """This class push all objects in the db """


    def __init__(self):
        self.get_objects()


    def get_objects(self):
        """
        FUNCTION THAT GET  MESSIER OBJECT
        
        Parameters
        ----------
        None

        Loop in each element in catalogue-de-messier.json and add to Data base

        Returns
        -------
        None

        """
        with open('./datas/catalogue-de-messier.json') as json_file:
            datas = json.load(json_file)
            for obj in datas:
                current_object = obj['fields']
                db.catalog.insert(current_object)