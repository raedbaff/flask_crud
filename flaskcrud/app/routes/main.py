from flask import Blueprint
from app.controllers.main_controller import delete_user, get_users, save_user,update_user

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return get_users()

@main.route("/", methods=["POST"])
def add_user():
    return save_user()
    
@main.route("/<id>", methods=["PUT"])
def update(id):
    return update_user(id)
@main.route("/<id>", methods=["DELETE"])
def delete(id):
    return delete_user(id)