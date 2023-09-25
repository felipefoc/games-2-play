from enum import Enum
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, validator, PositiveInt
from database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

class StatusChoices(Enum):
    NOT_STARTED = "Não iniciado"
    IN_PROGRESS = "Em andamento"
    COMPLETED = "Zerado"
    ABANDONED = "Abandonado"

class Games(Base):
    __tablename__ = "games"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, unique=True)
    description = Column(String, index=True, nullable=True)
    photo = Column(String)
    added_on = Column(DateTime, server_default=func.now())
    finished_at = Column(DateTime, nullable=True)
    buyed = Column(Boolean, nullable=True, default=False)
    owner_id = Column(ForeignKey("users.id"))
    owner = relationship("User", back_populates="games")
    status = Column(String)

    @property
    def is_finished(self):
        return bool(self.finished_at)
    
    def save(self, db):
        db.add(self)
        db.commit()
        db.refresh(self)
        return self


class GameBaseSchema(BaseModel):
    title: str
    photo: str
    added_on: datetime = Field(default_factory=datetime.now)
    status: Optional[str] = None

class GameCreateSchema(GameBaseSchema):
    ...

class GameRetrieveSchema(GameBaseSchema):
    id: int


# class ListGameBaseSchema(BaseModel):
#     games: List[GameBaseSchema]