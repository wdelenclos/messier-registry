import json 
import pymongo
from pymongo import MongoClient
import os
from config import client


# Select the database
db = client.messier_registry
# Select the collection
catalog = db["catalog"]
url = "http://messier.obspm.fr/"


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

        Loop in each element in catalogue-de-messier.json and add to Database

        Returns
        -------
        None

        """
        with open('./datas/catalogue-de-messier.json') as json_file:
            datas = json.load(json_file)
            for obj in datas:
                current_object = obj['fields']
                catalog.insert(current_object)