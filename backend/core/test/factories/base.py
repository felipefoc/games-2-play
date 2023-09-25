import factory
# Same session factory used by the previous fixture
from database import SessionLocal


class BaseFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        sqlalchemy_session = SessionLocal
        sqlalchemy_session_persistence = "commit"