from secrets import token_urlsafe

class Config():
    DEBUG = True
    SECRET_KEY = token_urlsafe(25)
    SQLALCHEMY_DATABASE_URI = "sqlite:///florence.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
  