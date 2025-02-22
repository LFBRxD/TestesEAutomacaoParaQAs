import logging

from flask import request, jsonify
from typing import Literal, Tuple
from flask import Response
from flasgger import swag_from

from app.services.user_service import UserService


class UserController:
    @staticmethod
    @swag_from({
        'tags': ['User'],
        'responses': {
            200: {
                'description': 'A list of users',
                'schema': {
                    'type': 'array',
                    'items': {
                        'type': 'object',
                        'properties': {
                            'id': {'type': 'integer'},
                            'name': {'type': 'string'},
                            'email': {'type': 'string'}
                        }
                    }
                }
            },
            500: {
                'description': 'Internal Server Error',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'error': {'type': 'string'}
                    }
                }
            }
        }
    })
    def get_users():
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
    @swag_from({
        'tags': ['User'],
        'parameters': [
            {
                'name': 'body',
                'in': 'body',
                'required': True,
                'schema': {
                    'type': 'object',
                    'properties': {
                        'name': {'type': 'string'},
                        'email': {'type': 'string'},
                        'document': {'type': 'string'}
                    },
                    'required': ['name', 'email', 'document']
                }
            }
        ],
        'responses': {
            201: {
                'description': 'User created successfully',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'id': {'type': 'integer'},
                        'name': {'type': 'string'},
                        'email': {'type': 'string'},
                        'document': {'type': 'string'}
                    }
                }
            },
            400: {
                'description': 'Invalid request',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'error': {'type': 'string'}
                    }
                }
            },
            409: {
                'description': 'Conflict',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'error': {'type': 'string'}
                    }
                }
            },
            500: {
                'description': 'Internal Server Error',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'error': {'type': 'string'}
                    }
                }
            }
        }
    })
    def create_user():
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
    @swag_from({
        'tags': ['User'],
        'parameters': [
            {
                'name': 'user_id',
                'in': 'path',
                'required': True,
                'type': 'integer'
            }
        ],
        'responses': {
            200: {
                'description': 'User found',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'id': {'type': 'integer'},
                        'name': {'type': 'string'},
                        'email': {'type': 'string'}
                    }
                }
            },
            404: {
                'description': 'User not found',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'error': {'type': 'string'}
                    }
                }
            },
            500: {
                'description': 'Internal Server Error',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'error': {'type': 'string'}
                    }
                }
            }
        }
    })
    def get_user_by_id(user_id: int) -> Tuple[Response, Literal[404, 200, 500]]:
        try:
            user = UserService.get_user_by_id(user_id)
            if not user:
                return jsonify({"error": "User not found"}), 404

            return jsonify(user), 200
        except Exception as e:
            logging.error(f"Error in get_user_by_id: {str(e)}", exc_info=True)
            return jsonify({"error": "Internal Server Error"}), 500

    @staticmethod
    @swag_from({
        'tags': ['User'],
        'parameters': [
            {
                'name': 'name',
                'in': 'path',
                'required': True,
                'type': 'string'
            }
        ],
        'responses': {
            200: {
                'description': 'User found',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'id': {'type': 'integer'},
                        'name': {'type': 'string'},
                        'email': {'type': 'string'}
                    }
                }
            },
            404: {
                'description': 'User not found',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'error': {'type': 'string'}
                    }
                }
            },
            500: {
                'description': 'Internal Server Error',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'error': {'type': 'string'}
                    }
                }
            }
        }
    })
    def get_user_by_name(name : str) -> Tuple[Response, Literal[404, 200, 500]]:
        try:
            user = UserService.get_user_by_name(name)
            if not user:
                return jsonify({"error": "User not found"}), 404

            return jsonify(user), 200
        except Exception as e:
            logging.error(f"Error in get_user_by_name: {str(e)}", exc_info=True)
            return jsonify({"error": "Internal Server Error"}), 500

    @staticmethod
    @swag_from({
        'tags': ['User'],
        'parameters': [
            {
                'name': 'email',
                'in': 'path',
                'required': True,
                'type': 'string'
            }
        ],
        'responses': {
            200: {
                'description': 'User found',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'id': {'type': 'integer'},
                        'name': {'type': 'string'},
                        'email': {'type': 'string'}
                    }
                }
            },
            404: {
                'description': 'User not found',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'error': {'type': 'string'}
                    }
                }
            },
            500: {
                'description': 'Internal Server Error',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'error': {'type': 'string'}
                    }
                }
            }
        }
    })
    def get_user_by_email(email : str) -> Tuple[Response, Literal[404, 200, 500]]:
        try:
            user = UserService.get_user_by_email(email)
            if not user:
                return jsonify({"error": "User not found"}), 404

            return jsonify(user), 200
        except Exception as e:
            logging.error(f"Error in get_user_by_email: {str(e)}", exc_info=True)
            return jsonify({"error": "Internal Server Error"}), 500

    @staticmethod
    @swag_from({
        'tags': ['User'],
        'parameters': [
            {
                'name': 'body',
                'in': 'body',
                'required': True,
                'schema': {
                    'type': 'object',
                    'properties': {
                        'id': {'type': 'integer'},
                        'name': {'type': 'string'},
                        'email': {'type': 'string'},
                        'document': {'type': 'string'}
                    },
                    'required': ['id', 'name', 'email']
                }
            }
        ],
        'responses': {
            200: {
                'description': 'User updated successfully',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'id': {'type': 'integer'},
                        'name': {'type': 'string'},
                        'email': {'type': 'string'},
                        'document': {'type': 'string'}
                    }
                }
            },
            400: {
                'description': 'Invalid request',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'error': {'type': 'string'}
                    }
                }
            },
            404: {
                'description': 'User not found',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'error': {'type': 'string'}
                    }
                }
            },
            500: {
                'description': 'Internal Server Error',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'error': {'type': 'string'}
                    }
                }
            }
        }
    })
    def update_user() -> Tuple[Response, Literal[400, 404, 200, 500]]:
        try:
            data = request.json
            logging.debug(f"Request Data: {data}")

            if not data:
                return jsonify({"error": "Invalid request, no JSON received"}), 400

            user = UserService.update_user(data["id"], data)

            if not user:
                return jsonify({"error": "User not found"}), 404

            return jsonify(user), 200
        except Exception as e:
            logging.error(f"Error in update_user: {str(e)}", exc_info=True)
            return jsonify({"error": "Internal Server Error"}), 500

    @staticmethod
    @swag_from({
        'tags': ['User'],
        'parameters': [
            {
                'name': 'user_id',
                'in': 'path',
                'required': True,
                'type': 'integer'
            }
        ],
        'responses': {
            200: {
                'description': 'User deleted successfully',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'id': {'type': 'integer'},
                        'name': {'type': 'string'},
                        'email': {'type': 'string'}
                    }
                }
            },
            404: {
                'description': 'User not found',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'error': {'type': 'string'}
                    }
                }
            },
            500: {
                'description': 'Internal Server Error',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'error': {'type': 'string'}
                    }
                }
            }
        }
    })
    def delete_user(user_id : int) -> Tuple[Response, Literal[404, 200, 500]]:
        try:
            user = UserService.delete_user(user_id)
            if not user:
                return jsonify({"error": "User not found"}), 404

            return jsonify({"user": user["name"], "status":"deleted"}), 200
        except Exception as e:
            logging.error(f"Error in delete_user: {str(e)}", exc_info=True)
            return jsonify({"error": "Internal Server Error"}), 500

    @staticmethod
    @swag_from({
        'tags': ['User'],
        'parameters': [
            {
                'name': 'document',
                'in': 'path',
                'required': True,
                'type': 'string'
            }
        ],
        'responses': {
            200: {
                'description': 'User found',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'id': {'type': 'integer'},
                        'name': {'type': 'string'},
                        'email': {'type': 'string'}
                    }
                }
            },
            404: {
                'description': 'User not found',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'error': {'type': 'string'}
                    }
                }
            },
            500: {
                'description': 'Internal Server Error',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'error': {'type': 'string'}
                    }
                }
            }
        }
    })  
    def get_user_by_document(document : str) -> Tuple[Response, Literal[404, 200, 500]]:
        try:
            user = UserService.get_user_by_document(document)
            if not user:
                return jsonify({"error": "User not found"}), 404

            return jsonify(user), 200
        except Exception as e:
            logging.error(f"Error in get_user_by_document: {str(e)}", exc_info=True)
            return jsonify({"error": "Internal Server Error"}), 500
