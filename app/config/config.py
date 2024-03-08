"""Contains database configuration settings for the application"""

import sqlalchemy
from sqlalchemy import orm
from sqlalchemy.ext import declarative

PATH_TO_DB_FILE = ".\\app\\resources\\data.db"

DATABASE_URL = f"sqlite:///{PATH_TO_DB_FILE}"

engine = sqlalchemy.create_engine(DATABASE_URL)
SessionLocal = orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative.declarative_base()
