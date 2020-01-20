import pymongo
from flask import Flask, request
from flask_restplus import Api, Resource

myclient = pymongo.MongoClient("mongodb://localhost:27018/")
mydb = myclient["sor"]

app = Flask(__name__)

api = Api(app=app, version='0.1', title='Space Object Registry Api', description='The Messier Space Object Registry based on Messier List.', validate=True)

@api.route("/stars/")
class BooksList(Resource):
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
@api.route("/stars/<string:title>")
class Book(Resource):
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

app.run(port= 8887, host= 'localhost')