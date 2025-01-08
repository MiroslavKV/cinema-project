import os


class Config:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DEBUG = True
    DB_USER = os.getenv("DB_USER")
    DB_PASS = os.getenv("DB_PASS")
    DB_NAME = os.getenv("DB_NAME")
    PATH_TO_DB = os.path.join(BASE_DIR, "instance", "cinema.db")

    SQLALCHEMY_DATABASE_URI = f'sqlite:///{PATH_TO_DB}'
    SECRET_KEY = os.getenv("SECRET_KEY", "123_secret")


print(Config.SQLALCHEMY_DATABASE_URI)