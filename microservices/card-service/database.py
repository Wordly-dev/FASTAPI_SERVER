from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from app.config import settings

engine = create_engine(url=settings.SYNC_DB_URL)
session = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass