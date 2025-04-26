from utils import SQLAlchemyRepository

from models import Dictionary

class DictionaryRepository(SQLAlchemyRepository):
    model = Dictionary