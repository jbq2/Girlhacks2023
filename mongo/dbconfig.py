import application_properties
import certifi
from pymongo.mongo_client import MongoClient

ca = certifi.where()
uri = f'mongodb+srv://host:{application_properties.mongo_config["pass"]}@cluster0.v22zda7.mongodb.net/?retryWrites=true&w=majority&appName=AtlasApp'

# Create a new client and connect to the server
client = MongoClient(uri, tlsCAFile=ca)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)