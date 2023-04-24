from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))
class Config:
    UPLOAD_FOLDER = os.path.join(basedir, "uploaded_files")
    SECRET_KEY = os.environ.get("SECRET_KEY") or "your_secret_key_here"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or "sqlite:///" + os.path.join(
        basedir, "survey.db"
    )


config = Config()
db = SQLAlchemy()


def create_app():
    # create and configure the app
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)

    if not os.path.exists(config.UPLOAD_FOLDER):
        os.makedirs(config.UPLOAD_FOLDER)

    with app.app_context():
        from .  import models
        from . import routes
        db.create_all()
        app.register_blueprint(routes.bp)

    return app


app = create_app()
