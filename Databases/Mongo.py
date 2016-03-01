from pymongo import MongoClient

class Database:
    def __init__(self):
        mongo = MongoClient('localhost', 27017)
        self.db = mongo["pydoro"]

    def create(self, collection, document):
        return self.db[collection].insert_one(document).inserted_id

    def read(self, collection, query):
        return self.db[collection].find_one(query)

    def update(self, collection, query, document):
        return self.db[collection].update_one(query, {'$set': document})


