import json 
import pymongo
from pymongo import MongoClient
import os
import requests
from bs4 import BeautifulSoup
import re
import scholarly

client = MongoClient('mongodb://localhost:27017')
db = client['messier_registry']
url = "http://messier.obspm.fr/"



class PushArticlesToDB:
    """This class push all Articles in the db """


    def __init__(self):
        self.objects_link = []
        self.guery_scholar()


    def get_db_object(self):

        """ 
        PARAMS:
        -------
        None
        
        
        Function that return list of Messier Object present in MongoDb
        
        
        Return
        ------
        List:
            Messier objects
        
         """ 
        objects = list(db.catalog.find())
        return(objects)

    
    def guery_scholar(self):
        """ 
        PARAMS:
        ------
        None
        

        Function scrap Google Scholar and push i in MongoDb
        
        
        Return
        ------
        None
        
        """ 

        tab = self.get_db_object()
        indice  = 0

        while indice < len(tab):
            if 'ngc' in tab[indice]:
                search_query = scholarly.search_pubs_query(tab[indice]['ngc'])
                for i in range(50):
                    current_article = next(search_query) 
                    current_article = current_article.__dict__
                    current_article["biblio"] =  current_article.pop('bib')
                    current_article["biblio"]["file"] =  current_article["biblio"].pop('eprint')
                    current_article["ngc"]= tab[indice]["ngc"]
                    current_article["_object_id"]= tab[indice]["_id"]
                    print(current_article)
                    db.articles.insert(current_article)
                indice +=1

            indice +=1
            
            

PushArticlesToDB()