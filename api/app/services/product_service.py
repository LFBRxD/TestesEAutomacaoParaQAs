import logging

from app.repositories.product_repository import ProductRepository


class ProductService:
    @staticmethod
    def get_all_products():
        try:
            products = ProductRepository.get_all()
            logging.info("Fetched %d Products", len(products))
            return products
        except Exception as e:
            logging.error("Error in get_all_products: %s", str(e), exc_info=True)
            return {"error": "Internal Server Error"}, 500

    @staticmethod
    def create_product(data : dict[str, str]):
        try:
            new_product = ProductRepository.create(data)
            return new_product
        except Exception as e:
            logging.error("Error in create_product: %s", str(e), exc_info=True)
            return {"error": "Internal Server Error"}, 500

    @staticmethod
    def get_product_by_id(product_id : int):
        try:
            product = ProductRepository.get_by_id(product_id)
            return product
        except Exception as e:
            logging.error("Error in get_product_by_id: %s", str(e), exc_info=True)
            return None

    @staticmethod
    def get_product_by_name(name : str):
        try:
            product = ProductRepository.get_by_name(name)
            return product
        except Exception as e:
            logging.error("Error in get_product_by_name: %s", str(e), exc_info=True)
            return None

    @staticmethod
    def update_product(product_id : int, data : dict[str, str]):
        try:
            product = ProductRepository.update_by_id(product_id, data)
            return product
        except Exception as e:
            logging.error("Error in update_product: %s", str(e), exc_info=True)
            return None

    @staticmethod
    def delete_product(product_id : int):
        try:
            product = ProductRepository.delete_by_id(product_id)
            return product
        except Exception as e:
            logging.error("Error in delete_product: %s", str(e), exc_info=True)
            return None

    @staticmethod
    def delete_product_by_name(name : str):
        try:
            product = ProductRepository.delete_by_name(name)
            return product
        except Exception as e:
            logging.error("Error in delete_product_by_name: %s", str(e), exc_info=True)
            return None

    @staticmethod
    def update_product_stock(product_id : int, quantity : int):
        try:
            product = ProductRepository.update_stock(product_id, quantity)
            return product
        except Exception as e:
            logging.error("Error in update_product_stock: %s", str(e), exc_info=True)
            return None

    @staticmethod
    def update_product_price(product_id : int, price : float):
        try:
            product = ProductRepository.update_price(product_id, price)
            return product
        except Exception as e:
            logging.error("Error in update_product_price: %s", str(e), exc_info=True)
            return None

    @staticmethod
    def update_product_name(product_id : int, name : str):
        try:
            product = ProductRepository.update_name(product_id, name)
            return product
        except Exception as e:
            logging.error("Error in update_product_name: %s", str(e), exc_info=True)
            return None

    @staticmethod
    def update_product_description(product_id: int, description : str):
        try:
            product = ProductRepository.update_description(product_id, description)
            return product
        except Exception as e:
            logging.error("Error in update_product_description: %s", str(e), exc_info=True)
            return None
