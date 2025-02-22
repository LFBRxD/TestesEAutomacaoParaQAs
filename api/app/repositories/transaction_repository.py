import logging

from flask import current_app

from app.db import db
from app.models.transaction import Transaction
from app.models.product import Product
from app.repositories.product_repository import ProductRepository

class TransactionRepository:
    @staticmethod
    def get_by_id(transaction_id : int):
        try:
            with current_app.app_context():
                transaction : Transaction = Transaction.query.get(transaction_id)
                return transaction.to_dict() if transaction else None
        except Exception as e:
            logging.error("Error fetching transaction by ID: %s", str(e), exc_info=True)
            return None
        
    @staticmethod
    def get_by_user_id(user_id : int):
        try:
            with current_app.app_context():
                transactions = Transaction.query.filter_by(user_id=user_id).all()
                return [transaction.to_dict() for transaction in transactions]
        except Exception as e:
            logging.error("Error fetching transactions by user ID: %s", str(e), exc_info=True)
            return None
    
    @staticmethod
    def get_all():
        try:
            with current_app.app_context():
                transactions = Transaction.query.all()
                return [transaction.to_dict() for transaction in transactions]
        except Exception as e:
            logging.error("Error fetching transactions: %s", str(e), exc_info=True)
            return None
    
    @staticmethod
    def create_transaction(transaction : Transaction):
        try:
            with current_app.app_context():
                product_price = ProductRepository.get_by_id(transaction.product_id)["price"]
                
                transaction.transaction_date = db.func.now()
                transaction.total = product_price * transaction.quantity

                db.session.add(transaction)
                db.session.commit()
                return transaction.to_dict()
        except Exception as e:
            logging.error("Error creating transaction: %s", str(e), exc_info=True)
            return None
        
    @staticmethod
    def update_by_id(transaction_id : int, data : dict[str, str]):
        try:
            with current_app.app_context():
                transaction : Transaction = Transaction.query.get(transaction_id)
                if not transaction:
                    return None
                
                transaction.user_id = data["user_id"]
                transaction.product_id = data["product_id"]
                transaction.quantity = data["quantity"]
                transaction.total = data["total"]
                db.session.commit()
                return transaction.to_dict()
        except Exception as e:
            db.session.rollback()
            logging.error("Error updating transaction: %s", str(e), exc_info=True)
            return None
        
    @staticmethod
    def check_stock(product_id : int, quantity : int):
        try:
            with current_app.app_context():
                product : Product = Product.query.get(product_id)
                if not product:
                    return False
                
                return product.stock >= quantity
        except Exception as e:
            logging.error("Error checking stock: %s", str(e), exc_info=True)
            return False
        
    @staticmethod
    def delete_by_id(transaction_id : int):
        try:
            with current_app.app_context():
                transaction : Transaction = Transaction.query.get(transaction_id)
                if not transaction:
                    return None
                
                db.session.delete(transaction)
                db.session.commit()
                return transaction.to_dict()
        except Exception as e:
            db.session.rollback()
            logging.error("Error deleting transaction: %s", str(e), exc_info=True)
            return None
    
    @staticmethod
    def update_transaction_status(transaction_id : int, status : str):
        try:
            with current_app.app_context():
                transaction : Transaction = Transaction.query.get(transaction_id)
                if not transaction:
                    return None
                
                transaction.status = status
                db.session.commit()
                return transaction.to_dict()
        except Exception as e:
            db.session.rollback()
            logging.error("Error updating transaction status: %s", str(e), exc_info=True)
            return None
