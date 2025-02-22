import logging

from flask import request
from typing import Literal, Tuple
from flask import jsonify, Response
from flasgger import swag_from

from app.services.transaction_service import TransactionService

class TransactionController:
    @staticmethod
    @swag_from({
        'tags': ['Transaction'],
        'parameters': [],
        'responses': {
            200: {
                'description': 'Get all transactions',
                'content': {
                    'application/json': {
                        'schema': {
                            'type': 'array',
                            'items': {
                                'type': 'object',
                                'properties': {
                                    'id': {'type': 'integer'},
                                    'user_id': {'type': 'integer'},
                                    'amount': {'type': 'number'},
                                    'type': {'type': 'string'},
                                    'status': {'type': 'string'},
                                    'created_at': {'type': 'string'},
                                    'updated_at': {'type': 'string'}
                                }
                            }
                        }
                    }
                }
            },
            500: {
                'description': 'Internal Server Error',
                'content': {
                    'application/json': {
                        'schema': {
                            'type': 'object',
                            'properties': {
                                'error': {'type': 'string'}
                            }
                        }
                    }
                }
            }
        }
    })  
    def get_all_transactions():
        try:
            transactions = TransactionService.get_all_transactions()
            return jsonify(transactions), 200
        except Exception as e:
            logging.error(f"Error in Transaction.get_all_transactions: {str(e)}")
            return jsonify({"error": "Internal Server Error"}), 500
    
    @staticmethod
    @swag_from({
        'tags': ['Transaction'],
        'parameters': [
            {
                'in': 'path',
                'name': 'transaction_id',
                'schema': {
                    'type': 'integer'
                },
                'required': True
            }
        ],
        'responses': {
            200: {
                'description': 'Get transaction by id',
                'content': {
                    'application/json': {
                        'schema': {
                            'type': 'object',
                            'properties': {
                                'id': {'type': 'integer'},
                                'user_id': {'type': 'integer'},
                                'amount': {'type': 'number'},
                                'type': {'type': 'string'},
                                'status': {'type': 'string'},
                                'created_at': {'type': 'string'},
                                'updated_at': {'type': 'string'}
                            }
                        }
                    }
                }
            },
            404: {
                'description': 'Transaction not found',
                'content': {
                    'application/json': {
                        'schema': {
                            'type': 'object',
                            'properties': {
                                'error': {'type': 'string'}
                            }
                        }
                    }
                }
            },
            500: {
                'description': 'Internal Server Error',
                'content': {
                    'application/json': {
                        'schema': {
                            'type': 'object',
                            'properties': {
                                'error': {'type': 'string'}
                            }
                        }
                    }
                }
            }
        }
    })
    def get_transaction_by_id(transaction_id: int):
        try:
            transaction = TransactionService.get_transaction_by_id(transaction_id)
            if transaction:
                return jsonify(transaction), 200
            return jsonify({"error": "Transaction not found"}), 404
        except Exception as e:
            logging.error(f"Error in Transaction.get_transaction_by_id: {str(e)}")
            return jsonify({"error": "Internal Server Error"}), 500
    
    @staticmethod
    @swag_from({
        'tags': ['Transaction'],
        'parameters': [
            {
                'in': 'path',
                'name': 'user_id',
                'schema': {
                    'type': 'integer'
                },
                'required': True
            }
        ],
        'responses': {
            200: {
                'description': 'Get transaction by user id',
                'content': {
                    'application/json': {
                        'schema': {
                            'type': 'object',
                            'properties': {
                                'id': {'type': 'integer'},
                                'user_id': {'type': 'integer'},
                                'amount': {'type': 'number'},
                                'type': {'type': 'string'},
                                'status': {'type': 'string'},
                                'created_at': {'type': 'string'},
                                'updated_at': {'type': 'string'}
                            }
                        }
                    }
                }
            },
            404: {
                'description': 'Transaction not found',
                'content': {
                    'application/json': {
                        'schema': {
                            'type': 'object',
                            'properties': {
                                'error': {'type': 'string'}
                            }
                        }
                    }
                }
            },
            500: {
                'description': 'Internal Server Error',
                'content': {
                    'application/json': {
                        'schema': {
                            'type': 'object',
                            'properties': {
                                'error': {'type': 'string'}
                            }
                        }
                    }
                }
            }
        }
    })
    def get_transaction_by_user_id(user_id: int):
        try:
            transaction = TransactionService.get_transaction_by_user_id(user_id)
            if transaction:
                return jsonify(transaction), 200
            return jsonify({"error": "Transaction not found"}), 404
        except Exception as e:
            logging.error(f"Error in Transaction.get_transaction_by_user_id: {str(e)}")
            return jsonify({"error": "Internal Server Error"}), 500
        
    @staticmethod
    def create_transaction():
        try:
            data = request.get_json()
            if data is None:
                return jsonify({"error": "Bad Request: JSON não fornecido"}), 400

            transaction = TransactionService.create_transaction(data)

            if transaction:
                return jsonify(transaction), 201
            
            return jsonify({"error": "Bad Request"}), 400
        except Exception as e:
            logging.error(f"Error in Transaction.create_transaction: {str(e)}")
            return jsonify({"error": "Internal Server Error"}), 500

    @staticmethod
    @swag_from({ 
        'tags': ['Transaction'],
        'parameters': [
            {
                'in': 'path',
                'name': 'transaction_id',
                'schema': {
                    'type': 'integer'
                },
                'required': True
            },
            {
                'in': 'body',
                'name': 'data',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'user_id': {'type': 'integer'},
                        'amount': {'type': 'number'},
                        'type': {'type': 'string'},
                        'status': {'type': 'string'}
                    }
                },
                'required': True
            }
        ],
        'responses': {
            200: {
                'description': 'Update transaction',
                'content': {
                    'application/json': {
                        'schema': {
                            'type': 'object',
                            'properties': {
                                'id': {'type': 'integer'},
                                'user_id': {'type': 'integer'},
                                'amount': {'type': 'number'},
                                'type': {'type': 'string'},
                                'status': {'type': 'string'},
                                'created_at': {'type': 'string'},
                                'updated_at': {'type': 'string'}
                            }
                        }
                    }
                }
            },
            400: {
                'description': 'Bad Request',
                'content': {
                    'application/json': {
                        'schema': {
                            'type': 'object',
                            'properties': {
                                'error': {'type': 'string'}
                            }
                        }
                    }
                }
            },
            404: {
                'description': 'Transaction not found',
                'content': {
                    'application/json': {
                        'schema': {
                            'type': 'object',
                            'properties': {
                                'error': {'type': 'string'}
                            }
                        }
                    }
                }
            },
            500: {
                'description': 'Internal Server Error',
                'content': {
                    'application/json': {
                        'schema': {
                            'type': 'object',
                            'properties': {
                                'error': {'type': 'string'}
                            }
                        }
                    }
                }
            }
        }
    })
    def update_transaction():
        try:
            data = request.get_json()
            if data is None:
                return jsonify({"error": "Bad Request: JSON não fornecido"}), 400
            transaction = TransactionService.update_transaction(data['transaction_id'], data)
            if transaction:
                return jsonify(transaction), 200
            return jsonify({"error": "Transaction not found"}), 404
        except Exception as e:
            logging.error(f"Error in Transaction.update_transaction: {str(e)}")
            return jsonify({"error": "Internal Server Error"}), 500
    
    @staticmethod
    @swag_from({ 
        'tags': ['Transaction'],
        'parameters': [
            {
                'in': 'path',
                'name': 'transaction_id',
                'schema': {
                    'type': 'integer'
                },
                'required': True
            }
        ],
        'responses': {
            200: {
                'description': 'Delete transaction',
                'content': {
                    'application/json': {
                        'schema': {
                            'type': 'object',
                            'properties': {
                                'id': {'type': 'integer'},
                                'user_id': {'type': 'integer'},
                                'amount': {'type': 'number'},
                                'type': {'type': 'string'},
                                'status': {'type': 'string'},
                                'created_at': {'type': 'string'},
                                'updated_at': {'type': 'string'}
                            }
                        }
                    }
                }
            },
            404: {
                'description': 'Transaction not found',
                'content': {
                    'application/json': {
                        'schema': {
                            'type': 'object',
                            'properties': {
                                'error': {'type': 'string'}
                            }
                        }
                    }
                }
            },
            500: {
                'description': 'Internal Server Error',
                'content': {
                    'application/json': {
                        'schema': {
                            'type': 'object',
                            'properties': {
                                'error': {'type': 'string'}
                            }
                        }
                    }
                }
            }
        }
    })
    def delete_transaction(transaction_id: int):
        try:
            transaction = TransactionService.delete_transaction(transaction_id)
            if transaction:
                return jsonify(transaction), 200
            return jsonify({"error": "Transaction not found"}), 404
        except Exception as e:
            logging.error(f"Error in Transaction.delete_transaction: {str(e)}")
            return jsonify({"error": "Internal Server Error"}), 500
        
    @staticmethod
    @swag_from({
        'tags': ['Transaction'],
        'parameters': [
            {
                'in': 'path',
                'name': 'transaction_id',
                'schema': {
                    'type': 'integer'
                },
                'required': True
            },
            {
                'in': 'body',
                'name': 'status',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'status': {'type': 'string'}
                    }
                },
                'required': True
            }
        ],
        'responses': {
            200: {
                'description': 'Update transaction status',
                'content': {
                    'application/json': {
                        'schema': {
                            'type': 'object',
                            'properties': {
                                'id': {'type': 'integer'},
                                'user_id': {'type': 'integer'},
                                'amount': {'type': 'number'},
                                'type': {'type': 'string'},
                                'status': {'type': 'string'},
                                'created_at': {'type': 'string'},
                                'updated_at': {'type': 'string'}
                            }
                        }
                    }
                }
            },
            404: {
                'description': 'Transaction not found',
                'content': {
                    'application/json': {
                        'schema': {
                            'type': 'object',
                            'properties': {
                                'error': {'type': 'string'}
                            }
                        }
                    }
                }
            },
            500: {
                'description': 'Internal Server Error',
                'content': {
                    'application/json': {
                        'schema': {
                            'type': 'object',
                            'properties': {
                                'error': {'type': 'string'}
                            }
                        }
                    }
                }
            }
        }
    })
    def update_transaction_status(transaction_id: int, status: str):
        try:
            transaction = TransactionService.update_transaction_status(transaction_id, status)
            if transaction:
                return jsonify(transaction), 200
            return jsonify({"error": "Transaction not found"}), 404
        except Exception as e:
            logging.error(f"Error in Transaction.update_transaction_status: {str(e)}")
            return jsonify({"error": "Internal Server Error"}), 500