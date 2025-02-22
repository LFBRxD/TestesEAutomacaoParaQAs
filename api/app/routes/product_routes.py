import logging
from flask import Blueprint
from app.controllers.product_controller import ProductController

product_bp = Blueprint("product", __name__)

product_bp.route("/", methods=["GET"])(ProductController.get_products)
product_bp.route("/", methods=["POST"])(ProductController.create_product)
product_bp.route("/<int:product_id>", methods=["GET"])(ProductController.get_product_by_id)
product_bp.route("/<string:name>", methods=["GET"])(ProductController.get_product_by_name)
product_bp.route("/<int:product_id>", methods=["PUT"])(ProductController.update_product)
product_bp.route("/<int:product_id>", methods=["DELETE"])(ProductController.delete_product)
product_bp.route("/<string:name>", methods=["DELETE"])(ProductController.delete_product_by_name)


