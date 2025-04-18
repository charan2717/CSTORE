import os

class Config:
    SECRET_KEY = 'charan123'
    UPLOAD_FOLDER = 'uploads'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
