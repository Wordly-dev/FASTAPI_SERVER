from utils import SQLAlchemyRepository

from models import Word

class WordRepository(SQLAlchemyRepository):
    model = Word