import os

from flasgger import Swagger
from flask import Flask
from flask_migrate import Migrate

from api.app.db import db


def create_app():
    app = Flask(__name__)
    app.url_map.strict_slashes = False

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS') == 'False'
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI", "sqlite:///debug_database.db")

    db.init_app(app)
    Migrate(app, db)


    ## Import de rotas
    from api.app.routes.default_routes import default_bp
    from api.app.routes.user_routes import user_bp
    from api.app.routes.product_routes import product_bp

    ## Registro de rotas
    app.register_blueprint(default_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(product_bp, url_prefix="/products")

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
        "host": "localhost:5000",
        "basePath": "/",
        "schemes": ["http"],
        "paths": {},
    }

    Swagger(app, template=swagger_template)
    return app
#
#
## Importação e registro das rotas
# from app.routes.purchase_routes import purchase_bp
#
# app.register_blueprint(purchase_bp, url_prefix="/purchases")
# app.register_blueprint(default_bp)
#
