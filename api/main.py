import logging
import os

from dotenv import load_dotenv

from app import create_app
from app.db import db

load_dotenv()

logging.basicConfig(level=logging.DEBUG)

app = create_app()

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['FLASK_DEBUG'] = os.getenv('FLASK_DEBUG') == 'True'
app.config['FLASK_RUN_PORT'] = os.getenv('FLASK_RUN_PORT', 5000)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=app.config['FLASK_DEBUG'], port=app.config['FLASK_RUN_PORT'])
