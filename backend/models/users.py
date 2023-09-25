from datetime import timedelta
from typing import List
from pydantic import BaseModel, field_validator
from database import Base, SessionLocal
from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship, scoped_session, sessionmaker

db = SessionLocal()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, index=True)
    password = Column(String(255))
    is_active = Column(Boolean, default=True)

    games = relationship("Games", back_populates="owner")

    def __str__(self) -> str:
        return self.username
    
    def save(self, db):
        db.add(self)
        db.commit()
        db.refresh(self)
        return self


class UserBaseSchema(BaseModel):
    username: str
    
class UserRetrieveSchema(UserBaseSchema):
    id: int

class UserCreateSchema(UserBaseSchema):
    password: str
    
    @field_validator("username")
    def validate_username(cls, value):
        if db.query(User).filter(User.username==value).one_or_none():
            raise ValueError(f"User with username '{value}' already exists")
        return value
    