![MIT](https://img.shields.io/badge/license-MIT-green "Licence")
![Python 3](https://img.shields.io/badge/python-v3.7-blue "Python")


# Space Object Registry 
A fast and simple RESTful API for Messier objects in Python.

## What is Space Object Registry ? 

SOR contains data provided by https://www.datastro.eu/explore/dataset/catalogue-de-messier/ 8 object type : Galaxy, Globular Cluster, Open Cluster, Emission Nebula, Planetary Nebula, Reflection Nebula, Double star, Supernova remnant.


#### Minimal functionnalities
Get more than 110 objects of the sky by NGC, Messier index, Season, Magnitude, Size, Distance (l.y / a. l.), RA, Dec, Constellation, Discoverer Year of discovery. Get images associated, and articles associated scrap on various databases (simbad, nasa ...).

The scientific attract is to facilitate access to scientific articles and correlation with scientific references. 

#### Stack
- Python 
- Flask
- FlaskPlus
- Mongo (and pymongo)
- Vue.JS
- Swagger

## Install guide
install dependencies

Run Mongo instance 
`` docker-compose up -d ``

Start python server
`` cd api && python run.py ``

Start app client
`` cd app && yarn install && yarn start ``

## Contributors: 
- Serhat YILDIRIM - @julioyildo
- Victor DARCEL - @darcelvictor
- Wladimir DELENCLOS - @wdelenclos