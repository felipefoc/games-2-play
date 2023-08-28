from datetime import timedelta
from typing import List
import peewee
from playhouse.shortcuts import model_to_dict
from pydantic import BaseModel, field_validator
from database import db, PeeweeGetterDict


class User(peewee.Model):
    username = peewee.CharField(unique=True, index=True)
    password = peewee.CharField(max_length=255)
    is_active = peewee.BooleanField(default=True)

    class Meta:
        database = db

    def __str__(self) -> str:
        return self.username
    
    def to_dict(self):
        return model_to_dict(self)

    def get_by_token(self, token):
        return self.get_or_none(User.api_token==token)


class UserBaseSchema(BaseModel):
    username: str

    class ConfigDict:
        orm_mode = True
        getter_dict = PeeweeGetterDict
    
class UserCreateSchema(UserBaseSchema):
    password: str
    
    @field_validator("username")
    def validate_username(cls, value):
        if bool(User.get_or_none(User.username==value)):
            raise ValueError(f"User with username '{value}' already exists")
        return value

class UserListSchema(BaseModel):
    users: List[UserBaseSchema]

    class ConfigDict:
        orm_mode = True
        getter_dict = PeeweeGetterDict
        

class LoginSchema(UserBaseSchema):
    password: str

class UserCreateTokenSchema(UserBaseSchema):
    id: int
    expires: timedelta


    