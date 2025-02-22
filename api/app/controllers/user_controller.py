import logging

from flask import request, jsonify

from api.app.services.user_service import UserService


class UserController:
    @staticmethod
    def get_users():
        """
        Fetches all users from the UserService and returns them as a JSON response.
        Returns:
            tuple: A tuple containing a JSON response and an HTTP status code.
                - If successful, returns a JSON list of users and a 200 status code.
                - If an error occurs, returns a JSON error message and a 500 status code.
        """

        try:
            users = UserService.get_all_users()
            if isinstance(users, dict) and "error" in users:
                return jsonify(users), 500

            logging.info(f"Fetched {len(users)} users")
            return jsonify(users), 200
        except Exception as e:
            logging.error(f"Error in get_users: {str(e)}", exc_info=True)
            return jsonify({"error": "Internal Server Error"}), 500

    @staticmethod
    def create_user():
        """
        Create a new user.
        This function handles the creation of a new user by processing the incoming JSON request data.
        It validates the request data, attempts to create a user using the UserService, and returns
        appropriate JSON responses based on the outcome.
        Returns:
            Response: A JSON response with the created user data and a 201 status code if successful.
                      A JSON response with an error message and a 400 status code if the request data is invalid.
                      A JSON response with an error message and a 409 status code if there is a conflict.
                      A JSON response with an error message and a 500 status code if an internal server error occurs.
        """

        try:
            data = request.json
            logging.debug(f"Request Data: {data}")

            if not data:
                return jsonify({"error": "Invalid request, no JSON received"}), 400

            user = UserService.create_user(data)

            if isinstance(user, dict) and "error" in user:
                return jsonify(user), 400 if "Missing" in user["error"] else 409

            return jsonify(user), 201
        except Exception as e:
            logging.error(f"Error in create_user: {str(e)}", exc_info=True)
            return jsonify({"error": "Internal Server Error"}), 500

    @staticmethod
    def get_user_by_id(user_id):
        """
        Retrieve a user by their ID.
        Args:
            user_id (int): The ID of the user to retrieve.
        Returns:
            Response: A JSON response containing the user data if found, 
                    or an error message if the user is not found or an 
                    internal server error occurs.
        Raises:
            Exception: If an error occurs during the retrieval process.
        """
        try:
            user = UserService.get_user_by_id(user_id)
            if not user:
                return jsonify({"error": "User not found"}), 404

            return jsonify(user), 200
        except Exception as e:
            logging.error(f"Error in get_user_by_id: {str(e)}", exc_info=True)
            return jsonify({"error": "Internal Server Error"}), 500

    @staticmethod
    def get_user_by_name(name):
        try:
            user = UserService.get_user_by_name(name)
            if not user:
                return jsonify({"error": "User not found"}), 404

            return jsonify(user), 200
        except Exception as e:
            logging.error(f"Error in get_user_by_name: {str(e)}", exc_info=True)
            return jsonify({"error": "Internal Server Error"}), 500

    @staticmethod
    def get_user_by_email(email):
        try:
            user = UserService.get_user_by_email(email)
            if not user:
                return jsonify({"error": "User not found"}), 404

            return jsonify(user), 200
        except Exception as e:
            logging.error(f"Error in get_user_by_email: {str(e)}", exc_info=True)
            return jsonify({"error": "Internal Server Error"}), 500

    @staticmethod
    def update_user(user_id):
        try:
            data = request.json
            logging.debug(f"Request Data: {data}")

            if not data:
                return jsonify({"error": "Invalid request, no JSON received"}), 400

            user = UserService.update_user(user_id, data)

            if not user:
                return jsonify({"error": "User not found"}), 404

            return jsonify(user), 200
        except Exception as e:
            logging.error(f"Error in update_user: {str(e)}", exc_info=True)
            return jsonify({"error": "Internal Server Error"}), 500

    @staticmethod
    def delete_user(user_id):
        try:
            user = UserService.delete_user(user_id)
            if not user:
                return jsonify({"error": "User not found"}), 404

            return jsonify(user), 200
        except Exception as e:
            logging.error(f"Error in delete_user: {str(e)}", exc_info=True)
            return jsonify({"error": "Internal Server Error"}), 500

    @staticmethod
    def get_user_by_document(document):
        try:
            user = UserService.get_user_by_document(document)
            if not user:
                return jsonify({"error": "User not found"}), 404

            return jsonify(user), 200
        except Exception as e:
            logging.error(f"Error in get_user_by_document: {str(e)}", exc_info=True)
            return jsonify({"error": "Internal Server Error"}), 500
