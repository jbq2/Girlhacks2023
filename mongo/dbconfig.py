from application_properties import mongo_config
import certifi
from pymongo.mongo_client import MongoClient

class DbConnection:
    CA = certifi.where()
    URI = f'mongodb+srv://host:{mongo_config["pass"]}@cluster0.v22zda7.mongodb.net/?retryWrites=true&w=majority&appName=AtlasApp'
    client = MongoClient(URI, tlsCAFile=CA)

    def __init__(self):
        try:
            self.client.admin.command('ping')
            print("Ping succcess")
        except Exception as e:
            print(f'Failed to ping and connect: {e}')
    
    def get_db(self):
        return self.client['girlhacks2023db']


class UsersDao:
    
    def __init__(self):
        self.DB_CONN = DbConnection()
        self.DB = self.DB_CONN.get_db()
        self.COLLECTION = self.DB['users']

    def insert_one(self, user):
        self.COLLECTION.insert_one(user)
        return user

    def find_any(self, user):
        return [user for user in self.COLLECTION.find(user)]
    