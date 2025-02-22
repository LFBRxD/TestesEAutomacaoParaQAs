from flask import Blueprint, jsonify
from flasgger import swag_from

default_bp = Blueprint("default", __name__)


@default_bp.route("/", methods=["GET"])
def home():
    """
    Home route that returns a welcome message and API version.

    Returns:
        Response: JSON response containing a welcome message and the API version.
    """
    return jsonify({"message": "It works, welcome to QA API", "api_ver": "1.0.0.0"}), 200
