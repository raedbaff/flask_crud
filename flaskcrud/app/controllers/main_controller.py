from flask import jsonify, request
from app.db import db
from app.models.User import User
from bson import ObjectId
def get_users():
    users= list(db.users.find())
    if len(users) == 0:
        return jsonify({"error": "No users found"}),404
       
    for user in users:
        user['_id'] = str(user['_id'])
    return jsonify(users)


def save_user():
    user = request.get_json()
    if not user or not user.get("name") or not user.get("email"):
        return jsonify({"error": "name and email are required"}), 400

    userExists = User.findUserByEmail(user['email'])
    if userExists:
        return jsonify({"error": "User already exists"}), 400
    newUser = User(user['name'], user['email'])
    newUser.save()
    return jsonify({"message": "User added successfully", "user": {
        "name": newUser.name,
        "email": newUser.email
    }}), 201 
def update_user(id):
    if not ObjectId.is_valid(id):
        return jsonify({"error": "Invalid ID supplied"}), 400
    user = request.get_json()

    if not user or not user.get("name") or not user.get("email"):
        return jsonify({"error": "name and email are required"}), 400
    userExists = User.findUserById(id)
    if not userExists:
        return jsonify({"error": "User not found"}), 404
    db.users.update_one({"_id": ObjectId(id)}, {"$set": user})
    return jsonify({"message": "User updated successfully", "user": {
        "name": user['name'],
        "email": user['email']
    }}), 200
   
def delete_user(id):
    if not ObjectId.is_valid(id):
        return jsonify({"error": "Invalid ID supplied"}), 400
    user = User.findUserById(id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    db.users.delete_one({"_id": ObjectId(id)})
    return jsonify({"message": "User deleted successfully"}), 200
