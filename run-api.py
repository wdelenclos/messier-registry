# -*- coding: utf-8 -*-

from datas.push_objects import PushObjectsToDB
from datas.push_articles import PushArticlesToDB
from app import app

objects = PushObjectsToDB()
articles = PushArticlesToDB()

if __name__ == '__main__':
    # Running app in debug mode
    app.run(debug=True)
    

