from shared import SQLAlchemyRepository

from models import Dictionary

class DictionaryRepository(SQLAlchemyRepository):
    model = Dictionary