import logging
from flask import Blueprint
from app.controllers.user_controller import UserController


user_bp = Blueprint("user", __name__)

user_bp.route("/user", methods=["POST"])(UserController.create_user)

user_bp.route("/user/<int:user_id>", methods=["GET"])(UserController.get_user_by_id)
user_bp.route("/user/<string:name>", methods=["GET"])(UserController.get_user_by_name)
user_bp.route("/user/<string:email>", methods=["GET"])(UserController.get_user_by_email)
user_bp.route("/users", methods=["GET"])(UserController.get_users)

user_bp.route("/user/<int:user_id>", methods=["PUT"])(UserController.update_user)

user_bp.route("/user/<int:user_id>", methods=["DELETE"])(UserController.delete_user)
