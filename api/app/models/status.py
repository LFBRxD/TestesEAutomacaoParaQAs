from datetime import datetime
from app.db import db

class Status(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    
    transactions = db.relationship("Transaction", back_populates="status")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }

