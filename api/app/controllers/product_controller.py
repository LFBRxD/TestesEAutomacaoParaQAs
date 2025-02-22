import logging
from flask import request, jsonify
from flasgger import swag_from
from app.services.product_service import ProductService

class ProductController:
    @staticmethod
    @swag_from({
        "responses": {
            200: {
                "description": "Lista todos os produtos disponíveis.",
                "schema": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "id": {"type": "integer"},
                            "name": {"type": "string"},
                            "price": {"type": "number"}
                        }
                    }
                }
            }
        }
    })
    def get_products():
        """
        Fetches all products from the ProductService.
        Returns:
            Response: A JSON response containing the list of products and a status code.
                      If an error occurs, returns a JSON response with an error message and a 500 status code.
        """

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
        "parameters": [
            {
                "name": "body",
                "in": "body",
                "required": True,
                "schema": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string"},
                        "price": {"type": "number"}
                    }
                }
            }
        ],
        "responses": {
            201: {
                "description": "Produto criado com sucesso.",
                "schema": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "integer"},
                        "name": {"type": "string"},
                        "price": {"type": "number"}
                    }
                }
            },
            400: {"description": "Requisição inválida"}
        }
    })
    def create_product():
        """
        Cria um novo produto.
        ---
        tags:
          - Produtos
        parameters:
          - name: body
            in: body
            required: True
            schema:
              type: object
              properties:
                name:
                  type: string
                price:
                  type: number
        responses:
          201:
            description: Produto criado com sucesso
            schema:
              type: object
              properties:
                id:
                  type: integer
                name:
                  type: string
                price:
                  type: number
          400:
            description: Requisição inválida
        """
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
        "parameters": [
            {
                "name": "product_id",
                "in": "path",
                "required": True,
                "type": "integer"
            }
        ],
        "responses": {
            200: {
                "description": "Produto encontrado.",
                "schema": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "integer"},
                        "name": {"type": "string"},
                        "price": {"type": "number"}
                    }
                }
            },
            404: {"description": "Produto não encontrado."}
        }
    })
    def get_product_by_id(product_id):
        """
        Retrieve a product by its ID.
        Args:
            product_id (int): The ID of the product to retrieve.
        Returns:
            Response: A JSON response containing the product data if found, 
                      or an error message if not found or if an exception occurs.
        Raises:
            Exception: If an error occurs during the retrieval process.
        """

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
        "parameters": [
            {
                "name": "name",
                "in": "path",
                "required": True,
                "type": "string"
            }
        ],
        "responses": {
            200: {
                "description": "Produto encontrado.",
                "schema": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "integer"},
                        "name": {"type": "string"},
                        "price": {"type": "number"}
                    }
                }
            },
            404: {"description": "Produto não encontrado."}
        }
    })
    def get_product_by_name(name):
        """ Retrieve a product by its name.
        Args:
            name (str): The name of the product to retrieve.
        Returns:
            Response: A JSON response containing the product data if found, 
                      or an error message if not found or if an exception occurs.
                      """
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
        "parameters": [
            {
                "name": "product_id",
                "in": "path",
                "required": True,
                "type": "integer"
            },
            {
                "name": "body",
                "in": "body",
                "required": True,
                "schema": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string"},
                        "price": {"type": "number"}
                    }
                }
            }
        ],
        "responses": {
            200: {
                "description": "Produto atualizado com sucesso.",
                "schema": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "integer"},
                        "name": {"type": "string"},
                        "price": {"type": "number"}
                    }
                }
            },
            400: {"description": "Requisição inválida"},
            404: {"description": "Produto não encontrado."}
        }
    })
    def update_product(product_id):
        """
        Update an existing product with the provided data.
        Args:
            product_id (int): The ID of the product to update.
        Returns:
            Response: A JSON response containing the updated product data and a status code of 200 if successful.
                      A JSON response with an error message and a status code of 400 if the request data is invalid.
                      A JSON response with an error message and a status code of 404 if the product is not found.
                      A JSON response with an error message and a status code of 500 if an internal server error occurs.
        Raises:
            Exception: If an error occurs during the update process.
        """
        
        try:
            data = request.json
            logging.debug(f"Request Data: {data}")  

            if not data:
                return jsonify({"error": "Invalid request, no JSON received"}), 400

            product = ProductService.update_product(product_id, data)

            if not product:
                return jsonify({"error": "Product not found"}), 404

            return jsonify(product), 200
        except Exception as e:
            logging.error(f"Error in update_product: {str(e)}", exc_info=True)
            return jsonify({"error": "Internal Server Error"}), 500
        
    @staticmethod
    def delete_product(product_id):
        try:
            product = ProductService.delete_product(product_id)
            if not product:
                return jsonify({"error": "Product not found"}), 404

            return jsonify(product), 200
        except Exception as e:
            logging.error(f"Error in delete_product: {str(e)}", exc_info=True)
            return jsonify({"error": "Internal Server Error"}), 500
    
    @staticmethod
    def delete_product_by_name(name):
        try:
            product = ProductService.delete_product_by_name(name)
            if not product:
                return jsonify({"error": "Product not found"}), 404

            return jsonify(product), 200
        except Exception as e:
            logging.error(f"Error in delete_product_by_name: {str(e)}", exc_info=True)
            return jsonify({"error": "Internal Server Error"}), 500
        
    @staticmethod
    def update_product_description(product_id):
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
    def update_product_price(product_id):
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
    def update_product_stock(product_id):
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
        