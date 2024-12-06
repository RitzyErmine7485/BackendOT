from pymongo import MongoClient
from app.config import Config

client = None

def init_db(app):
    global client
    client = MongoClient(Config.MONGO_URI)

def get_collection(collection_name):
    db = client["onetap"]
    return db[collection_name]
