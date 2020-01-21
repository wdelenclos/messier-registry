![MIT](https://img.shields.io/badge/license-MIT-green "Licence")
![Python 3](https://img.shields.io/badge/python-v3.7-blue "Python")


# Space Object Registry 
A fast and simple RESTful API for Messier objects in Python.

## What is Space Object Registry ? 

SOR contains data provided by https://www.datastro.eu/explore/dataset/catalogue-de-messier/ 8 object type : Galaxy,Globular Cluster, Open Cluster, Emission Nebula, Planetary Nebula, Reflection Nebula, Double star, Supernova remnant.

Output is formated in JSON.

#### Routes

| Method  | Endpoint | Description |
| ------------- | ------------- | ----------|
| GET | /all/ |  return all messier objects data  (without articles) |
| GET | /m/{messierid} | Return all data about a messier object (images, info, articles) |
| GET | /articles/{messierid} | Return artivles about a specific messier object |
| GET | /articles/search/{text} | Return articles containing this data |
| GET | /m/{attribute}/{value} | return object corresponding to a specific attribute value |
| GET | /images/{messierid} | return images url related to a specific messier |

#### Minimal functionnalities
Get more than 110 objects of the sky with NGC, Messier index, Season, Magnitude, Size, Distance (l.y / a. l.), RA, Dec, Constellation, Discover Year, Discoverer.
Filter with following parameters : NGC, Messier index, Season, Magnitude, Size, Distance, RA, Dec, Constellation, Discover Year.
Get images associated on nasa database.
Get Terlrad map associeted. 
Completion index on specific variable.
The scientific attract is to facilitate access to scientific articles and correlation with scientific references. 


#### Stack
- Python 
- Flask
- FlaskPlus
- Mongo (and pymongo)
- Swagger

## Install guide
install dependencies

Run docker image
`` docker-compose up -d ``

Start dev python server
`` cd api && python run.py ``

Start dev app client
`` cd app && yarn install && yarn start ``

## Contributors: 
- Serhat YILDIRIM - @julioyildo
- Victor DARCEL - @darcelvictor
- Wladimir DELENCLOS - @wdelenclos

#### Next features
Ability to get articles associated on various databases (simbad, nasa ...)  