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
        # self.get_links()
        self.guery_scholard()

    # def get_links(self):
    #     try:
    #         page = requests.get("http://messier.obspm.fr/objects_f.html")
    #         if page.status_code== 200:
    #             soup = BeautifulSoup(page.content, 'html.parser')
    #             a = soup.find_all('a')
              
    #             for i in a:
    #                 str_i= str(i)
    #                 if re.search("f/", str_i):
    #                     self.objects_link.append(i.get('href'))
    #     except ValueError:
    #         print("Scraping failed")      
    #         print(ValueError)       


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

    
    def guery_scholard(self):
        """ 
        PARAMS:
        ------
        None
        

        Function scrap Google Scholar and push i in MongoDb
        
        
        Return
        ------
        List:
            Messier objects
        
        """ 



        # Ce code permet de récupéré les 2 premiers articles de chaque objet sur Google Scholar.
        # Dans l'idéal il faudrait récupérer une 50e d'articles par objet pour pouvoir faire des filtres
        #  ATTENTION : Une fois les articles récupérés : ne pas oublier de mettre une clé étrangère lian l'article à l'objet dans mongodb!!
        # VOIR FICHIER : datas/articles.json

        
        tab = self.get_db_object()
        indice  = 0
        articles = []
        while indice < len(tab):
            if tab[indice]['ngc']==False:
                indice +=1
            else:
                search_query = scholarly.search_pubs_query(tab[indice]['ngc'])
                for i in range(2):
                    articles.append(next(search_query))

        #Une fois ce bou de code vaidé. Push sur Mongodb.
            
            

PushArticlesToDB()