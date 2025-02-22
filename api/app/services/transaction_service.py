import logging

from app.repositories.transaction_repository import TransactionRepository
from app.models.transaction import Transaction

class TransactionService:
    @staticmethod
    def get_all_transactions():
        try:
            transactions = TransactionRepository.get_all()
            if transactions is not None:
                logging.info("Fetched %d transactions", len(transactions))
            else:
                logging.info("Fetched 0 transactions")
            return transactions
        except Exception as e:
            logging.error("Error in get_all_transactions: %s", str(e), exc_info=True)
            return {"error": "Internal Server Error"}, 500
        
    @staticmethod
    def get_transaction_by_id(transaction_id: int):
        try:
            transaction = TransactionRepository.get_by_id(transaction_id)
            return transaction
        except Exception as e:
            logging.error("Error in get_transaction_by_id: %s", str(e), exc_info=True)
            return None
        
    @staticmethod
    def get_transaction_by_user_id(user_id: int):
        try:
            transaction = TransactionRepository.get_by_user_id(user_id)
            return transaction
        except Exception as e:
            logging.error("Error in get_transaction_by_user_id: %s", str(e), exc_info=True)
            return None
        
    @staticmethod
    def create_transaction(data: dict):
        try:
            transaction = Transaction(**data)
            transaction = TransactionRepository.create_transaction(transaction)
            
            return transaction
        except Exception as e:
            logging.error("Error in create_transaction: %s", str(e), exc_info=True)
            return None
        
    @staticmethod
    def update_transaction(transaction_id: int, data: dict):
        try:
            transaction = TransactionRepository.update_by_id(transaction_id, data)
            return transaction
        except Exception as e:
            logging.error("Error in update_transaction: %s", str(e), exc_info=True)
            return None
        
    @staticmethod
    def delete_transaction(transaction_id: int):
        try:
            transaction = TransactionRepository.delete_by_id(transaction_id)
            return transaction
        except Exception as e:
            logging.error("Error in delete_transaction: %s", str(e), exc_info=True)
            return None
        
    @staticmethod
    def update_transaction_status(transaction_id: int, status: str):
        try:
            transaction = TransactionRepository.update_transaction_status(transaction_id, status)
            return transaction
        except Exception as e:
            logging.error("Error in update_transaction_status: %s", str(e), exc_info=True)
            return None