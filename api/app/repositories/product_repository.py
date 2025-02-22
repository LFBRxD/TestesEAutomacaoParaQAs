import logging

from flask import current_app

from app.db import db
from app.models.product import Product


class ProductRepository:
    @staticmethod
    def create(data):
        try:
            with current_app.app_context():
                new_product = Product(name=data["name"], price=data["price"], stock=data["stock"],
                                      description=data["description"])
                db.session.add(new_product)
                db.session.commit()
                return new_product.to_dict()
        except Exception as e:
            db.session.rollback()
            logging.error("Error in create_product: %s", str(e), exc_info=True)
            return {"error": "Internal Server Error"}, 500
    
    @staticmethod
    def get_all():
        try:
            with current_app.app_context():
                products = Product.query.all()
                logging.info("Fetched %d products", len(products))
                return [product.to_dict() for product in products]
        except Exception as e:
            logging.error("Error fetching products: %s", str(e), exc_info=True)
            return {"error": "Internal Server Error"}, 500

    @staticmethod
    def get_by_id(product_id):
        try:
            with current_app.app_context():
                product = Product.query.get(product_id)
                return product.to_dict() if product else None
        except Exception as e:
            logging.error("Error fetching product by ID: %s", str(e), exc_info=True)
            return None

    @staticmethod
    def get_by_name(name):
        try:
            with current_app.app_context():
                product = Product.query.filter_by(name=name).first()
                return product.to_dict() if product else None
        except Exception as e:
            logging.error("Error fetching product by name: %s", str(e), exc_info=True)
            return None

    @staticmethod
    def get_all_by_price(price):
        try:
            with current_app.app_context():
                products = Product.query.filter(Product.price == price).all()
                return [product.to_dict() for product in products]
        except Exception as e:
            logging.error("Error fetching products by price: %s", str(e), exc_info=True)
            return None

    @staticmethod
    def update_description(product_id, description):
        try:
            with current_app.app_context():
                product = Product.query.get(product_id)
                if not product:
                    return None

                product.description = description
                db.session.commit()
                return product.to_dict()
        except Exception as e:
            logging.error("Error in update_description: %s", str(e), exc_info=True)
            return None

    @staticmethod
    def update_by_id(product_id, data):
        try:
            with current_app.app_context():
                product = Product.query.get(product_id)
                if not product:
                    return None

                product.name = data["name"]
                product.price = data["price"]
                db.session.commit()
                return product.to_dict()
        except Exception as e:
            logging.error("Error in update_product: %s", str(e), exc_info=True)
            return None

    @staticmethod
    def delete_by_id(product_id):
        try:
            with current_app.app_context():
                product = Product.query.get(product_id)
                if not product:
                    return None

                db.session.delete(product)
                db.session.commit()
                return product.to_dict()
        except Exception as e:
            logging.error("Error in delete_product: %s", str(e), exc_info=True)
            return None

    @staticmethod
    def delete_by_name(name):
        try:
            with current_app.app_context():
                product = Product.query.filter_by(name=name).first()
                if not product:
                    return None

                db.session.delete(product)
                db.session.commit()
                return product.to_dict()
        except Exception as e:
            logging.error("Error in delete_product: %s", str(e), exc_info=True)
            return None

    @staticmethod
    def create_product(data):
        try:
            with current_app.app_context():
                new_product = Product(name=data["name"], price=data["price"], stock=data["stock"],
                                      description=data["description"])
                db.session.add(new_product)
                db.session.commit()
                return new_product.to_dict()
        except Exception as e:
            db.session.rollback()
            logging.error("Error in create_product: %s", str(e), exc_info=True)
            return None

    @staticmethod
    def update_stock(product_id, quantity):
        try:
            with current_app.app_context():
                product = Product.query.get(product_id)
                if not product:
                    return None

                product.stock = quantity
                db.session.commit()
                return product.to_dict()
        except Exception as e:
            logging.error("Error in update_stock: %s", str(e), exc_info=True)
            return None

    @staticmethod
    def update_name(product_id, name):
        try:
            with current_app.app_context():
                product = Product.query.get(product_id)
                if not product:
                    return None

                product.name = name
                db.session.commit()
                return product.to_dict()
        except Exception as e:
            logging.error("Error in update_name: %s", str(e), exc_info=True)
            return None

    @staticmethod
    def update_price(product_id, price):
        try:
            with current_app.app_context():
                product = Product.query.get(product_id)
                if not product:
                    return None

                product.price = price
                db.session.commit()
                return product.to_dict()
        except Exception as e:
            logging.error("Error in update_price: %s", str(e), exc_info=True)
            return None
