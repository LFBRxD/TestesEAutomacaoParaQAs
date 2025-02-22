import logging
from app.models.user import User
from app.db import db
from flask import current_app

class UserRepository:
    @staticmethod
    def get_all():
        try:
            with current_app.app_context():
                users = User.query.all()
                logging.info("Fetched %d users", len(users))
                return [user.to_dict() for user in users]
        except Exception as e:
            logging.error("Error fetching users: %s", str(e), exc_info=True)
            return {"error": "Internal Server Error"}, 500
        
    @staticmethod
    def get_by_id(user_id):
        try:
            with current_app.app_context():
                user = User.query.get(user_id)
                return user.to_dict() if user else None
        except Exception as e:
            logging.error("Error fetching user by ID: %s", str(e), exc_info=True)
            return None
        
    @staticmethod
    def get_by_name(name):
        try:
            with current_app.app_context():
                user = User.query.filter_by(name=name).first()
                return user.to_dict() if user else None
        except Exception as e:
            logging.error("Error fetching user by name: %s", str(e), exc_info=True)
            return None

    @staticmethod
    def get_by_email(email):
        try:
            with current_app.app_context():
                user = User.query.filter_by(email=email).first()
                return user.to_dict() if user else None
        except Exception as e:
            logging.error("Error fetching user by email: %s", str(e), exc_info=True)
            return None  
        
    @staticmethod
    def update_by_id(user_id, data):
        try:
            with current_app.app_context():
                user = User.query.get(user_id)
                if not user:
                    return None
                
                user.name = data["name"]
                user.email = data["email"]
                db.session.commit()
                return user.to_dict()
        except Exception as e:
            db.session.rollback()
            logging.error("Error updating user: %s", str(e), exc_info=True)
            return None
    
    @staticmethod
    def delete_by_id(user_id):
        try:
            with current_app.app_context():
                user = User.query.get(user_id)
                if not user:
                    return None
                
                db.session.delete(user)
                db.session.commit()
                return user.to_dict()
        except Exception as e:
            db.session.rollback()
            logging.error("Error deleting user: %s", str(e), exc_info=True)
            return None
        
    @staticmethod
    def delete_by_document(document):
        try:
            with current_app.app_context():
                user = User.query.filter_by(document=document).first()
                if not user:
                    return None
                
                db.session.delete(user)
                db.session.commit()
                return user.to_dict()
        except Exception as e:
            db.session.rollback()
            logging.error("Error deleting user: %s", str(e), exc_info=True)
            return None

    @staticmethod
    def create(data):
        try:
            with current_app.app_context():
                new_user = User(name=data["name"], email=data["email"])
                db.session.add(new_user) 
                db.session.flush()
                db.session.commit() 
                
                logging.info("User created successfully: %s", new_user.to_dict()) 
                return new_user.to_dict() 
        except Exception as e:
            db.session.rollback() 
            logging.error("Error creating user: %s", str(e), exc_info=True)
            return {"error": "Internal Server Error"}, 500
