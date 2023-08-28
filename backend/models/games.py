from .users import User
from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel, Field, validator, PositiveInt
from database import db
from playhouse.shortcuts import model_to_dict
import peewee

STATUS_CHOICES = (
    (1, "Não iniciado"),
    (2, "Em andamento"),
    (3, "Zerado"),
    (4, "Abondonado"),
)

class Games(peewee.Model):
    title = peewee.CharField()
    photo = peewee.CharField()
    added_on = peewee.DateTimeField(default=datetime.now)
    finished_at = peewee.DateTimeField(null=True)
    buyed = peewee.BooleanField(default=False)
    owner = peewee.ForeignKeyField(User, backref="games")
    status = peewee.IntegerField(choices=STATUS_CHOICES)

    class Meta:
        database = db
        indexes = (
                    (('title', 'owner'), True),
                )

    @property
    def is_finished(self):
        return bool(self.finished_at)
    
    def to_dict(self):
        return model_to_dict(self)

class _GameBaseSchema(BaseModel):
    title: str
    photo: str
    added_on: datetime = Field(default_factory=datetime.now)
    finished_at: Optional[datetime]
    buyed: bool = False
    owner: PositiveInt
    status: int

class GameBaseSchema(BaseModel):
    title: str
    photo: str
    added_on: datetime = Field(default_factory=datetime.now)
    status: int

class GameCreateSchema(BaseModel):
    title: str
    photo: str
    added_on: datetime = Field(default_factory=datetime.now)
    status: Optional[int] = None

class ListGameBaseSchema(BaseModel):
    games: List[GameBaseSchema]