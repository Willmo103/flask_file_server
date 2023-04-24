# here will be the model for the file information to be stroed in the database, and updated each time a new file is uploaded, deleted, or modified
import os
from . import db
from . import config
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref
from flask_login import UserMixin
import datetime


class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(100), nullable=False)
    last_modified = db.Column(db.DateTime, nullable=False)
    date_uploaded = db.Column(db.DateTime, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    size = db.Column(db.Integer, nullable=False)


    def __init__(self, filename, last_modified, date_uploaded, owner, size):
        self.filename = filename
        self.last_modified = last_modified
        self.date_uploaded = date_uploaded
        self.owner = owner
        self.size = size

    def __repr__(self):
        return f"File('{self.filename}', '{self.last_modified}', '{self.date_uploaded}', '{self.owner}', '{self.size}')"

    @staticmethod
    def build_files():
        files = os.listdir(config.UPLOAD_FOLDER)
        for file in files:
            file_path = os.path.join(config.UPLOAD_FOLDER, file)
            last_modified = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
            date_uploaded = datetime.datetime.fromtimestamp(os.path.getctime(file_path))

            size = os.stat(file_path).st_size
            new_file = File(file, last_modified, date_uploaded, owner, size)
            db.session.add(new_file)
            db.session.commit()
