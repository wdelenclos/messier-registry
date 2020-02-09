import json 
import pymongo
from pymongo import MongoClient
import os
import requests
from bs4 import BeautifulSoup
import re

client = MongoClient('mongodb://localhost:27017')
db = client['messier_registry']

page = requests.get("http://messier.obspm.fr/objects_f.html")

class PushArticlesToDB:
    """This class push all objects in the db """


    def __init__(self):
        self.objects_link = []
        self.get_links()

    def get_links(self):
        try:
            if page.status_code== 200:
                soup = BeautifulSoup(page.content, 'html.parser')
                a = soup.find_all('a')
              
                for i in a:
                    i = str(i)
                    if re.search("f/", i):
                        self.objects_link.append(i)
        except ValueError:
            print("Scraping failed")      
            print(ValueError)       


    def scrap_links(self):
        pass


PushArticlesToDB()