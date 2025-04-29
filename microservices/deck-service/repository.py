from shared import SQLAlchemyRepository
from database import Dictionary, session

class DictionaryRepository(SQLAlchemyRepository):
    model = Dictionary
    session = session