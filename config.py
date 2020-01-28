"""This module is to configure app to connect with database."""

from pymongo import MongoClient

DATABASE = MongoClient()['sor'] 
DEBUG = True
client = MongoClient('localhost', 27017)
sources = ["https://www.datastro.eu/api/records/1.0/search/?dataset=catalogue-de-messier&sort=messier&facet=objet&facet=saison&facet=mag&facet=english_name_nom_en_anglais&facet=french_name_nom_francais&facet=latin_name_nom_latin&facet=decouvreur&facet=annee"]