from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

import subprocess
 
db = SQLAlchemy()

from .logic.store import * 

#database atributes
DB_NAME = "database"

"""FOR POSTGRES
URL: postgresql+psycopg2://{POSTGRES_USER}:{PASSWORD}@localhost:{PORT}/{DB_NAME}"""

POSTGRES_USER = "postgres"
PASSWORD = "1234"
PORT = 5432

"""FOR SQLITE
URL: sqlite:///{DB_NAME}.db"""

UPLOAD_FOLDER = 'website/static/img/uploadedPrints'

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}.db'#conecta base de datos
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User
    
    with app.app_context():
        db.create_all()
        insertCategories()

    return app

