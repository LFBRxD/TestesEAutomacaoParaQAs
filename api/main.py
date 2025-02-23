import logging
import os

from dotenv import load_dotenv
from app.models.status import Status
from app.seed.seed_db import seed_status
from flask_cors import CORS

from app import create_app
from app.db import db

load_dotenv()

logging.basicConfig(level=logging.DEBUG)

app = create_app()
CORS(app)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['FLASK_DEBUG'] = os.getenv('FLASK_DEBUG') == 'True'
app.config['FLASK_RUN_PORT'] = os.getenv('FLASK_RUN_PORT', '8080')
app.config['FLASK_RUN_HOST'] = os.getenv('FLASK_RUN_HOST', '127.0.0.1')

if __name__ == "__main__":
    #app.run(debug=app.config['FLASK_DEBUG'], port=app.config['FLASK_RUN_PORT'])
    app.run(debug=app.config['FLASK_DEBUG'], port=int(app.config['FLASK_RUN_PORT']), host=app.config['FLASK_RUN_HOST'])
