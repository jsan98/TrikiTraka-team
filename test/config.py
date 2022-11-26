from secrets import token_urlsafe
from sqlalchemy.orm import sessionmaker

class Config():
    DEBUG = True
    SECRET_KEY = token_urlsafe(25)
    SQLALCHEMY_DATABASE_URI = "sqlite:///florenceTest.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    Session = sessionmaker(bind=SQLALCHEMY_DATABASE_URI)
    session = Session()
  