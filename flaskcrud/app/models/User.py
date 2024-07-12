from app.db import db
from datetime import datetime
from bson import ObjectId
class User:
    def __init__(self, name, email):

        self.name = name
        self.email = email
        self.created_at = datetime.now()

    def save(self):
        db.users.insert_one(self.__dict__)
    def findUserByEmail(email):
        return db.users.find_one({"email": email})
    def findUserById(id):
        return db.users.find_one({"_id": ObjectId(id)})
    
