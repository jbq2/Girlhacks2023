# from application_properties import mongo_config
import certifi
from pymongo.mongo_client import MongoClient


class DbConnection:
    CA = certifi.where()
    # URI = f'mongodb+srv://host:{mongo_config["pass"]}@cluster0.v22zda7.mongodb.net/?retryWrites=true&w=majority&appName=AtlasApp'
    URI = f'mongodb+srv://host:IVvkndG0Q7NNw4Xp@cluster0.v22zda7.mongodb.net/?retryWrites=true&w=majority&appName=AtlasApp'
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
    
    def __init__(self, db_conn: DbConnection):
        self.DB_CONN = db_conn
        self.DB = self.DB_CONN.get_db()
        self.COLLECTION = self.DB['users']

    def insert_one(self, user):
        try:
            res = self.COLLECTION.insert_one(user)
            if not res.inserted_id:
                raise Exception
            return user
        except Exception as e:
            print(e)
            return None

    def find_any(self, user={}):
        return [user for user in self.COLLECTION.find(user)]


class ImagesDao:

    def __init__(self, db_conn: DbConnection):
        self.DB_CONN = db_conn
        self.DB = self.DB_CONN.get_db()
        self.COLLECTION = self.DB['images']
    
    def insert_one(self, image):
        try:
            res = self.COLLECTION.insert_one(image)
            if not res.inserted_id:
                raise Exception
            return image
        except Exception as e:
            print(e)
            return None

    
    def find_any(self, image={}):
        return [image for image in self.COLLECTION.find(image)]

class LeaderboardDao:

    def __init__(self, db_conn: DbConnection):
        self.DB_CONN = db_conn
        self.DB = self.DB_CONN.get_db()
        self.COLLECTION = self.DB['leaderboard']
    
    def insert_one(self, stat):
        try:
            res = self.COLLECTION.insert_one(stat)
            if not res.inserted_id:
                raise Exception
            return stat
        except Exception as e:
            print(e)
            return None


    def find_any(self, stat={}):
        return [stat for stat in self.COLLECTION.find(stat)]