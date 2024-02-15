import os


db_user = os.getenv("MARIADB_USER")
db_psswd = os.getenv("MARIADB_PASSWORD")
db_name = os.getenv("MARIADB_DATABASE")

class Config:
    SQLALCHEMY_DATABASE_URI = f"mariadb+mariadbconnector://{db_user}:{db_psswd}@db/{db_name}"
    SECRET_KEY = os.environ['SECRET_KEY']