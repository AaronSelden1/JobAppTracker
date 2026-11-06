import secrets

class Config:
    SECRET_KEY = secrets.token_hex(32)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///JobAppTracker.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False