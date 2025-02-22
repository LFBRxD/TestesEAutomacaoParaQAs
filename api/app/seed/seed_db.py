import logging
from app.repositories.status_repository import StatusRepository
from app.models.status import Status
from app.db import db

def seed_status():
    status_list = ["pending", "approved", "rejected", "canceled", "concluded"]

    try:
        if not StatusRepository.is_table_empty():
            logging.debug("The table Status is already populated.")
            return

        for status_name in status_list:
            status = Status(name=status_name)
            db.session.add(status)

        db.session.commit()
        logging.debug("The table Status has been populated.")

    except Exception as e:
        logging.error("Error seeding status table: %s", str(e), exc_info=True)
        db.session.rollback()  