import logging
from app.repositories.user_repository import UserRepository

class UserService:
    @staticmethod
    def get_all_users():
        try:
            users = UserRepository.get_all()
            logging.info("Fetched %d users", len(users))
            return users
        except Exception as e:
            logging.error("Error in get_all_users: %s", str(e), exc_info=True)
            return {"error": "Internal Server Error"}, 500

    @staticmethod
    def create_user(data):
        try:
            if not data or "name" not in data or "email" not in data:
                logging.warning("Invalid user data received: %s", data)
                return {"error": "Missing required fields (name, email)"}, 400

            logging.debug("Received data: %s", data)

            ## Verifica se o usuário já existe pelo e-mail (caso o banco tenha restrição única)
            #existing_user = UserRepository.get_by_email(data["email"])
            #if existing_user:
            #    logging.warning("Attempt to create duplicate user: %s", data["email"])
            #    return {"error": "User with this email already exists"}, 409

            new_user = UserRepository.create(data)
            logging.info("User created successfully: %s", new_user)
            
            return new_user  # O controller define o status 201

        except Exception as e:
            logging.error("Error in create_user: %s", str(e), exc_info=True)
            return {"error": "Internal Server Error"}, 500

    @staticmethod
    def get_user_by_id(user_id):
        try:
            user = UserRepository.get_by_id(user_id)
            return user
        except Exception as e:
            logging.error("Error in get_user_by_id: %s", str(e), exc_info=True)
            return None
    
    @staticmethod
    def get_user_by_name(name):
        try:
            user = UserRepository.get_by_name(name)
            return user
        except Exception as e:
            logging.error("Error in get_user_by_name: %s", str(e), exc_info=True)
            return None
        
    @staticmethod
    def get_user_by_email(email):
        try:
            user = UserRepository.get_by_email(email)
            return user
        except Exception as e:
            logging.error("Error in get_user_by_email: %s", str(e), exc_info=True)
            return None
        
    @staticmethod
    def update_user(user_id, data):
        try:
            user = UserRepository.update_by_id(user_id, data)
            return user
        except Exception as e:
            logging.error("Error in update_user: %s", str(e), exc_info=True)
            return None
    
    @staticmethod
    def delete_user(user_id):
        try:
            user = UserRepository.delete_by_id(user_id)
            return user
        except Exception as e:
            logging.error("Error in delete_user: %s", str(e), exc_info=True)
            return None
        
    @staticmethod
    def delete_user_by_document(document):
        try:
            user = UserRepository.delete_by_document(document)
            return user
        except Exception as e:
            logging.error("Error in delete_user_by_document: %s", str(e), exc_info=True)
            return None