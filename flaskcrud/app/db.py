from pymongo import MongoClient
from config import Config


try:
    mongo = MongoClient(Config.MONGO_URL)
    db = mongo['test']
    print("successfully connected to mongoDB")
except Exception as e:
    print("something went wrong while connecting to mongoDB",e)