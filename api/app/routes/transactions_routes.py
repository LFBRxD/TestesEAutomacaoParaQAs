from flask import Blueprint

from app.controllers.transaction_controller import TransactionController

transaction_bp = Blueprint("transaction", __name__)

transaction_bp.route("/transactions", methods=["GET"])(TransactionController.get_all_transactions)
transaction_bp.route("/transaction", methods=["POST"])(TransactionController.create_transaction)
transaction_bp.route("/transaction", methods=["PUT"])(TransactionController.update_transaction)
transaction_bp.route("/transaction/status", methods=["PUT"])(TransactionController.update_transaction_status)
transaction_bp.route("/transactions/<int:id>", methods=["GET"])(TransactionController.get_transaction_by_id)
transaction_bp.route("/transactions/user/<int:id>", methods=["GET"])(TransactionController.get_transaction_by_user_id)
transaction_bp.route("/transactions/<int:id>", methods=["DELETE"])(TransactionController.delete_transaction)
