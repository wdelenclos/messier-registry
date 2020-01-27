import pymongo
from flask import request
from flask_restplus import Resource

myclient = pymongo.MongoClient("mongodb://localhost:27018/")
mydb = myclient["sor"]

class ObjectList(Resource):
    def get(self):
        """
        returns a list of stars
        """
        cursor = mydb.books.find({}, {"_id": 0})
        data = []
        for book in cursor:
            data.append(book)
        return {"response": data}
    def post(self):
        """
        Add a new space object to the list
        """
        data = request.get_json()
        if not data:
            data = {"response": "ERROR"}
            return data, 404
        else:
            title = data.get('title')
            if title:
                if mydb.books.find_one({"title": title}):
                    return {"response": "book already exists."}, 403
                else:
                    mydb.insert(data)

class Object(Resource):
    def put(self, title):
        """
        Edits a selected space object
        """
        data = request.get_json()
        mydb.books.update({'title': title}, {'set': data})
    def delete(self, title):
        """
    delete a selected space object
    """
        mydb.books.delete({'title': title})