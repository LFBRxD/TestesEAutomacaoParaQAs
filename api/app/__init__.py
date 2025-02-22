import os

from flasgger import Swagger # type: ignore
from flask import Flask
from flask_migrate import Migrate

from app.db import db


def create_app():
    app = Flask(__name__)
    app.url_map.strict_slashes = False

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS') == 'False'
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI", "sqlite:///debug_database.db")
    app.config['FLASK_RUN_PORT'] = os.getenv('FLASK_RUN_PORT', 5000)

    db.init_app(app)
    Migrate(app, db)


    ## Import de rotas
    from app.routes.default_routes import default_bp
    from app.routes.user_routes import user_bp
    from app.routes.product_routes import product_bp


    # Configuração do Swagger
    swagger_template = {
        "swagger": "2.0",
        "info": {
            "title": "API de Testes para QAs",
            "contact": {
                "name": "Flavio Ramos",
                "email": "flavior.desouza@gmail.com"},
            "license": {
                "name": "MIT License",
                "url": "https://opensource.org/licenses/MIT"
            },
            "description": "API de Testes para QAs, com endpoints para usuários e produtos e documentação com Swagger, para treinamento de testes automatizados.",
            "version": "1.0.0"
        },
        "host": f"localhost:{app.config['FLASK_RUN_PORT']}",
        "basePath": "/",
        "schemes": ["http"],
        "paths": {},
    }

    Swagger(app, template=swagger_template)

    ## Registro de rotas
    
    app.register_blueprint(default_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(product_bp, url_prefix="/products")


    return app
#
#
## Importação e registro das rotas
# from app.routes.purchase_routes import purchase_bp
#
# app.register_blueprint(purchase_bp, url_prefix="/purchases")
# app.register_blueprint(default_bp)
#
