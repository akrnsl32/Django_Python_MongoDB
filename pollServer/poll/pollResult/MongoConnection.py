from pymongo import MongoClient
import datetime


class MongoConnection(object):

    client = MongoClient('mongodb://akrnsl32:qoffjstm5!@ds241570.mlab.com:41570/poll')

    # init! db, etc...
    def __init__(self):

        self.db = None
        self.collection = None
        self.post = {"code": "01",
                     "A_poll": {"1": "1", "2": "2", "3": "1", "4": "2", "5": "1", "6": "3", "7": "1", "8": "4", "9": "5", "10": "1"}
                     }

    def set_db(self, db_name='poll'):
        self.db = self.client[db_name]
        return

    # get collection
    def set_collection(self, coll_name='test'):
        self.collection = self.db[coll_name]
        return self.collection

    # insert document at test or some collection
    def insert_doc(self, data):
        result = self.collection.insert_one(data).inserted_id
        return result

    # get a document from the collection
    def get_doc(self, tag):
        collection = self.collection
        return collection.find_one({"tag": tag})

    def check_tag(self, tag):
        if self.get_doc(tag) is None:
            return True
        else:
            return False

    def insert_tag(self, tag, pw):
        result = self.collection.insert_one({"tag": tag, "password": pw}).inserted_id
        return result


#    def check_pw(self, tag, pw):
#        result = self.collection.find_one({"tag": tag})






