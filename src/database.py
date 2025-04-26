from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from config import app_config

engine = create_engine(url=app_config.SYNC_DB_URL)
session = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass