from shared import SQLAlchemyRepository
from database import session
from models import Card

class CardRepository(SQLAlchemyRepository):
    model = Card
    session = session

