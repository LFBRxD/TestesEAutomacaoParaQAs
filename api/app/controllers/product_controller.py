import logging

from flasgger import swag_from
from flask import request, jsonify
from typing import Literal, Tuple
from flask import Response

from app.services.product_service import ProductService


class ProductController:
    @staticmethod
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
    def get_product_by_id(product_id):
        try:
            product = ProductService.get_product_by_id(product_id)
            if not product:
                return jsonify({"error": "Product not found"}), 404

            return jsonify(product), 200
        except Exception as e:
            logging.error(f"Error in get_product_by_id: {str(e)}", exc_info=True)
            return jsonify({"error": "Internal Server Error"}), 500

    @staticmethod
    def get_product_by_name(name):
        try:
            product = ProductService.get_product_by_name(name)
            if not product:
                return jsonify({"error": "Product not found"}), 404

            return jsonify(product), 200
        except Exception as e:
            logging.error(f"Error in get_product_by_name: {str(e)}", exc_info=True)
            return jsonify({"error": "Internal Server Error"}), 500

    @staticmethod
    def update_product(product_id):
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
