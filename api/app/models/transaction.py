import stat
from app.db import db

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    total = db.Column(db.Float, nullable=False)
    transaction_date = db.Column(db.DateTime,  nullable=False)
    
    status_id = db.Column(db.Integer, db.ForeignKey("status.id"), nullable=False)
    status = db.relationship("Status", back_populates="transactions")

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "product_id": self.product_id,
            "quantity": self.quantity,
            "total": self.total,
            "transaction_date": self.transaction_date,
            "status": self.status.name if self.status else None
        }