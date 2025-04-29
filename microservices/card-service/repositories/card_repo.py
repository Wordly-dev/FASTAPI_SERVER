from shared.repository import SQLAlchemyRepository
from database import session, Card

class CardRepository(SQLAlchemyRepository):
    model = Card
    session = session