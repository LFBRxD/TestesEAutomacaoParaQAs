import logging
from flask import current_app
from app.db import db
from app.models.status import Status

class StatusRepository:
    @staticmethod
    def get_all():
        try:
            with current_app.app_context():
                statuses = Status.query.all()
                return [status.to_dict() for status in statuses]
        except Exception as e:
            logging.error("Error fetching statuses: %s", str(e), exc_info=True)
            return []

    @staticmethod
    def get_by_id(status_id: int):
        try:
            with current_app.app_context():
                status = Status.query.get(status_id)
                return status.to_dict() if status else None
        except Exception as e:
            logging.error("Error fetching status by ID: %s", str(e), exc_info=True)
            return None

    @staticmethod
    def create_status(status: Status):
        try:
            with current_app.app_context():
                db.session.add(status)
                db.session.commit()
                return status.to_dict()
        except Exception as e:
            logging.error("Error creating status: %s", str(e), exc_info=True)
            db.session.rollback()  
            return None

    @staticmethod
    def is_table_empty():
        try:
            with current_app.app_context():
                return Status.query.count() == 0
        except Exception as e:
            logging.error("Error checking if Status table is empty: %s", str(e), exc_info=True)
            return True  