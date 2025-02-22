import logging

from flasgger import swag_from
from flask import request, jsonify
from typing import Literal, Tuple
from flask import Response

from app.services.product_service import ProductService


class ProductController:
    @staticmethod
    @swag_from({
        'tags': ['Product'],
        'summary': 'Get all products',
        'description': 'Get all products',
        'responses': {
            200: {
                'description': 'List of products'
            },
            500: {
                'description': 'Internal Server Error'
            }
        }
    })
    def get_products():
        try:
            products = ProductService.get_all_products()
            if isinstance(products, dict) and "error" in products:
                return jsonify(products), 500

            logging.info(f"Fetched {len(products)} products")
            return jsonify(products), 200
        except Exception as e:
            logging.error(f"Error in get_products: {str(e)}", exc_info=True)
            return jsonify({"error": "Internal Server Error"}), 500

    @staticmethod
    @swag_from({
        'tags': ['Product'],
        'summary': 'Create a product',
        'description': 'Create a product',
        'parameters': [
            {
                'in': 'body',
                'name': 'body',
                'description': 'Product data',
                'required': True,
                'schema': {
                    'type': 'object',
                    'properties': {
                        'name': {
                            'type': 'string',
                            'example': 'Product 1'
                        },
                        'description': {
                            'type': 'string',
                            'example': 'Description of Product 1'
                        },
                        'price': {
                            'type': 'number',
                            'example': 100.0
                        },
                        'stock': {
                            'type': 'integer',
                            'example': 100
                        }
                    }
                }
            }
        ],
        'responses': {
            201: {
                'description': 'Product created'
            },
            400: {
                'description': 'Invalid request'
            },
            409: {
                'description': 'Product already exists'
            },
            500: {
                'description': 'Internal Server Error'
            }
        }
    })
    def create_product():
        try:
            data = request.json
            logging.debug(f"Request Data: {data}")

            if not data:
                return jsonify({"error": "Invalid request, no JSON received"}), 400

            product = ProductService.create_product(data)

            if isinstance(product, dict) and "error" in product:
                return jsonify(product), 400 if "Missing" in product["error"] else 409

            return jsonify(product), 201
        except Exception as e:
            logging.error(f"Error in create_product: {str(e)}", exc_info=True)
            return jsonify({"error": "Internal Server Error"}), 500

    @staticmethod
    @swag_from({
        'tags': ['Product'],
        'summary': 'Get product by ID',
        'description': 'Get product by ID',
        'parameters': [
            {
                'in': 'path',
                'name': 'product_id',
                'description': 'Product ID',
                'required': True,
                'schema': {
                    'type': 'integer',
                    'example': 1
                }
            }
        ],
        'responses': {
            200: {
                'description': 'Product found'
            },
            404: {
                'description': 'Product not found'
            },
            500: {
                'description': 'Internal Server Error'
            }
        }
    })
    def get_product_by_id(product_id : int) -> Tuple[Response, Literal[200, 404, 500]]:
        try:
            product = ProductService.get_product_by_id(product_id)
            if not product:
                return jsonify({"error": "Product not found"}), 404

            return jsonify(product), 200
        except Exception as e:
            logging.error(f"Error in get_product_by_id: {str(e)}", exc_info=True)
            return jsonify({"error": "Internal Server Error"}), 500

    @staticmethod
    @swag_from({
        'tags': ['Product'],
        'summary': 'Get product by name',
        'description': 'Get product by name',
        'parameters': [
            {
                'in': 'path',
                'name': 'name',
                'description': 'Product name',
                'required': True,
                'schema': {
                    'type': 'string',
                    'example': 'Product 1'
                }
            }
        ],
        'responses': {
            200: {
                'description': 'Product found'
            },
            404: {
                'description': 'Product not found'
            },
            500: {
                'description': 'Internal Server Error'
            }
        }
    })
    def get_product_by_name(name : str) -> Tuple[Response, Literal[200, 404, 500]]:
        try:
            product = ProductService.get_product_by_name(name)
            if not product:
                return jsonify({"error": "Product not found"}), 404

            return jsonify(product), 200
        except Exception as e:
            logging.error(f"Error in get_product_by_name: {str(e)}", exc_info=True)
            return jsonify({"error": "Internal Server Error"}), 500

    @staticmethod
    @swag_from({
        'tags': ['Product'],
        'summary': 'Update product',
        'description': 'Update product',
        'parameters': [
            {
                'in': 'body',
                'name': 'body',
                'description': 'Product data',
                'required': True,
                'schema': {
                    'type': 'object',
                    'properties': {
                        'id': {
                            'type': 'integer',
                            'example': 1
                        },
                        'name': {
                            'type': 'string',
                            'example': 'Product 1'
                        },
                        'description': {
                            'type': 'string',
                            'example': 'Description of Product 1'
                        },
                        'price': {
                            'type': 'number',
                            'example': 100.0
                        },
                        'stock': {
                            'type': 'integer',
                            'example': 100
                        }
                    }
                }
            }
        ],
        'responses': {
            200: {
                'description': 'Product updated'
            },
            400: {
                'description': 'Invalid request'
            },
            404: {
                'description': 'Product not found'
            },
            500: {
                'description': 'Internal Server Error'
            }
        }
    })
    def update_product() -> Tuple[Response, Literal[200, 404, 500 ,400]]:
        try:
            data = request.json
            logging.debug(f"Request Data: {data}")

            if not data:
                return jsonify({"error": "Invalid request, no JSON received"}), 400

            product = ProductService.update_product(data["id"], data)

            if not product:
                return jsonify({"error": "Product not found"}), 404

            return jsonify(product), 200
        except Exception as e:
            logging.error(f"Error in update_product: {str(e)}", exc_info=True)
            return jsonify({"error": "Internal Server Error"}), 500

    @staticmethod
    @swag_from({
        'tags': ['Product'],
        'summary': 'Delete product',
        'description': 'Delete product',
        'parameters': [
            {
                'in': 'path',
                'name': 'product_id',
                'description': 'Product ID',
                'required': True,
                'schema': {
                    'type': 'integer',
                    'example': 1
                }
            }
        ],
        'responses': {
            200: {
                'description': 'Product deleted'
            },
            404: {
                'description': 'Product not found'
            },
            500: {
                'description': 'Internal Server Error'
            }
        }
    })
    def delete_product(product_id : int) -> Tuple[Response, Literal[200, 404, 500]]:
        try:
            product = ProductService.delete_product(product_id)
            if not product:
                return jsonify({"error": "Product not found"}), 404

            return jsonify(product), 200
        except Exception as e:
            logging.error(f"Error in delete_product: {str(e)}", exc_info=True)
            return jsonify({"error": "Internal Server Error"}), 500

    @staticmethod
    @swag_from({
        'tags': ['Product'],
        'summary': 'Delete product by name',
        'description': 'Delete product by name',
        'parameters': [
            {
                'in': 'path',
                'name': 'name',
                'description': 'Product name',
                'required': True,
                'schema': {
                    'type': 'string',
                    'example': 'Product 1'
                }
            }
        ],
        'responses': {
            200: {
                'description': 'Product deleted'
            },
            404: {
                'description': 'Product not found'
            },
            500: {
                'description': 'Internal Server Error'
            }
        }
    })
    def delete_product_by_name(name : str) -> Tuple[Response, Literal[200, 404, 500]]:
        try:
            product = ProductService.delete_product_by_name(name)
            if not product:
                return jsonify({"error": "Product not found"}), 404

            return jsonify(product), 200
        except Exception as e:
            logging.error(f"Error in delete_product_by_name: {str(e)}", exc_info=True)
            return jsonify({"error": "Internal Server Error"}), 500

    @staticmethod
    @swag_from({
        'tags': ['Product'],
        'summary': 'Update product description',
        'description': 'Update product description',
        'parameters': [
            {
                'in': 'path',
                'name': 'product_id',
                'description': 'Product ID',
                'required': True,
                'schema': {
                    'type': 'integer',
                    'example': 1
                }
            }
        ],
        'responses': {
            200: {
                'description': 'Product description updated'
            },
            400: {
                'description': 'Invalid request'
            },
            404: {
                'description': 'Product not found'
            },
            500: {
                'description': 'Internal Server Error'
            }
        }
    })
    def update_product_description(product_id : int) -> Tuple[Response, Literal[200, 404, 500 ,400]]:
        try:
            data = request.json
            logging.debug(f"Request Data: {data}")

            if not data:
                return jsonify({"error": "Invalid request, no JSON received"}), 400

            product = ProductService.update_product_description(product_id, data)

            if not product:
                return jsonify({"error": "Product not found"}), 404

            return jsonify(product), 200
        except Exception as e:
            logging.error(f"Error in update_product_description: {str(e)}", exc_info=True)
            return jsonify({"error": "Internal Server Error"}), 500

    @staticmethod
    @swag_from({
        'tags': ['Product'],
        'summary': 'Update product price',
        'description': 'Update product price',
        'parameters': [
            {
                'in': 'path',
                'name': 'product_id',
                'description': 'Product ID',
                'required': True,
                'schema': {
                    'type': 'integer',
                    'example': 1
                }
            }
        ],
        'responses': {
            200: {
                'description': 'Product price updated'
            },
            400: {
                'description': 'Invalid request'
            },
            404: {
                'description': 'Product not found'
            },
            500: {
                'description': 'Internal Server Error'
            }
        }
    })
    def update_product_price(product_id : int) -> Tuple[Response, Literal[200, 404, 500 , 400]]:
        try:
            data = request.json
            logging.debug(f"Request Data: {data}")

            if not data:
                return jsonify({"error": "Invalid request, no JSON received"}), 400

            product = ProductService.update_product_price(product_id, data)

            if not product:
                return jsonify({"error": "Product not found"}), 404

            return jsonify(product), 200
        except Exception as e:
            logging.error(f"Error in update_product_price: {str(e)}", exc_info=True)
            return jsonify({"error": "Internal Server Error"}), 500

    @staticmethod
    @swag_from({
        'tags': ['Product'],
        'summary': 'Update product stock',
        'description': 'Update product stock',
        'parameters': [
            {
                'in': 'path',
                'name': 'product_id',
                'description': 'Product ID',
                'required': True,
                'schema': {
                    'type': 'integer',
                    'example': 1
                }
            }
        ],
        'responses': {
            200: {
                'description': 'Product stock updated'
            },
            400: {
                'description': 'Invalid request'
            },
            404: {
                'description': 'Product not found'
            },
            500: {
                'description': 'Internal Server Error'
            }
        }
    })
    def update_product_stock(product_id : int) -> Tuple[Response, Literal[200, 404, 500 , 400]]:
        try:
            data = request.json
            logging.debug(f"Request Data: {data}")

            if not data:
                return jsonify({"error": "Invalid request, no JSON received"}), 400

            product = ProductService.update_product_stock(product_id, data)

            if not product:
                return jsonify({"error": "Product not found"}), 404

            return jsonify(product), 200
        except Exception as e:
            logging.error(f"Error in update_product_stock: {str(e)}", exc_info=True)
            return jsonify({"error": "Internal Server Error"}), 500
