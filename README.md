![MIT](https://img.shields.io/badge/license-MIT-green "Licence")
![Python 3](https://img.shields.io/badge/python-v3.7-blue "Python")


# Space Object Registry 🚀
A fast and simple RESTful API for Messier objects in Python.

## What is Space Object Registry ? 
Available on https://space.wdelenclos.fr
SOR contains data provided by https://www.datastro.eu/explore/dataset/catalogue-de-messier/ 8 object type : Galaxy,Globular Cluster, Open Cluster, Emission Nebula, Planetary Nebula, Reflection Nebula, Double star, Supernova remnant.

Output is formated in JSON.

#### Routes
All routes are prefixed with /api/v1/

| Method  | Endpoint | Description |
| ------------- | ------------- | ----------|
| GET | /objects/ | return all messier objects data  (without articles) |
| GET | /objects/{messierid} | Return all data about a messier object (images, info, articles) |
| GET | /objects/q/{query} | return object corresponding to a specific attribute |
| GET | /articles/{messierid} | Return artivles about a specific messier object |
| GET | /articles/s/{text} | Return articles containing this data |
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
- Mongo (and pymongo)

## Requirements: 
Python 3
Docker
Docker-compose


## Install guide

#### Run mongo image
`` docker-compose up -d ``

#### Create Venv
`virtualenv -p python3 env`

#### Activate Venv
`source env/bin/activate`

#### Install dependecies
`pip3 install -r requirements.txt`
 
### Run migration
`python3 run-migration.py `

#### Run Api
`python3 run-api.py `
App running on http://127.0.0.1:5000/ 
Use Postman or an app to use it.


#### Desactivate Venv
`deactivate`


## Contributors: 
- Serhat YILDIRIM - @julioyildo
- Victor DARCEL - @darcelvictor
- Wladimir DELENCLOS - @wdelenclos

#### Next features
Ability to get articles associated on various databases (simbad, nasa ...)  
