from pymongo import MongoClient
import datetime


class MongoConnection(object):

    client = MongoClient('mongodb://leejuhwan:leejuhwan123@ds241570.mlab.com:41570/poll')

    # init! db, etc...
    def __init__(self):
        self.db = None
        self.collection = None
        self.post = {"code": "01",
                     "A_poll": {"1": "1", "2": "2", "3": "1", "4": "2", "5": "1", "6": "3", "7": "1", "8": "4",
                                "9": "5", "10": "1"}
                     }

    def set_db(self, db_name='poll'):
        self.db = self.client[db_name]
        return

    # get collection
    def set_collection(self, coll_name='id'):
        self.collection = self.db[coll_name]
        return self.collection

    # insert document at test or some collection
    def insert_doc(self):
        result = self.collection.insert_one(self.post).inserted_id
        return result

     # get a document from the collection
    def get_doc(self):
        collection = self.collection
        return collection.find_one({"code":"1111"})

    def get_doc(self, id):
        collection = self.collection
        return collection.find_one({"id": ""})
    # check_tag [name='check_tag']

    def insert_id(self, id, pw):
        result = self.collection.insert_one({"id": id, "password": pw}).inserted_id
        return result

    def check_tag(self, id):
        if self.get_doc(id) is None:
            return True
        else:
            return False




