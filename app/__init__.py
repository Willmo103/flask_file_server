from flask import Flask
import os

UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'uploaded_files') # this should be an env variable, but meh.

import os

def create_app():

    app = Flask(__name__)
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    from . import routes
    app.register_blueprint(routes.bp)
    return app

app = create_app()
