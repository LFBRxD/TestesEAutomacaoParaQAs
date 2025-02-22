from flask import Blueprint, jsonify

default_bp = Blueprint("default", __name__)


@default_bp.route("/", methods=["GET"])
def home():
    """
    Home route that returns a welcome message and API version.
    ---
    responses:
      200:
        description: Rota principal da API
        schema:
          type: object
          properties:
            message:
              type: string
              example: "It works, welcome to QA API"
            api_ver:
              type: string
              example: "1.0.0.0"
    """
    return jsonify({"message": "It works, welcome to QA API", "api_ver": "1.0.0.0"}), 200
