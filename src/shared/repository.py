from abc import abstractmethod, ABC
from sqlalchemy import insert, update, delete, select
from typing import Any


class AbstractRepository(ABC):
    @abstractmethod
    def get_many(self, *, where: Any | None, options: Any | None):
        pass
    
    @abstractmethod
    def get_one(self, *, instance_id: Any, options: Any | None = None):
        pass
    
    @abstractmethod
    def create(self, *, instance_data: Any):
        pass
    
    @abstractmethod
    def update(self, *, instance_id: Any, instance_data: Any):
        pass
    
    @abstractmethod
    def delete(self, *, instance_id: Any):
        pass


class SQLAlchemyRepository(AbstractRepository):
    model = None
    session = None

    def get_many(self, *, where: Any | None, options: list | None):
        where_clause = where if where is not None else {}
        options_clause = options if isinstance(options, list) else []
        
        with self.session() as sess:
            stmt = select(self.model).where(**where_clause).options(*options_clause)
            result = sess.scalars(stmt)

            return result.all()

    def get_one(self, *, instance_id: Any, options: list | None = None):
        with self.session() as sess:
            stmt = select(self.model).where(self.model.id == instance_id).options(*options if isinstance(options, list) else {})
            result = sess.scalars(stmt)

            return result.first()

    def create(self, *, instance_data: Any):
        with self.session() as sess:
            stmt = insert(self.model).values(**instance_data)
            sess.execute(stmt)
            sess.commit()

            return "Successfully added"
        
    def update(self, *, instance_id: Any, instance_data: Any):
        with self.session() as sess:
            stmt = update(self.model).values(**instance_data).where(self.model.id == instance_id)
            sess.execute(stmt)
            sess.commit()

            return "Successfully updated"

    def delete(self, instance_id: Any):
        with self.session() as sess:
            stmt = delete(self.model).where(self.model.id == instance_id)

            sess.execute(stmt)
            sess.commit()

            return "Successfully deleted"
