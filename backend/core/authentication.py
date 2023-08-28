from datetime import timedelta, datetime
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Request
from jose import JWTError, jwt
from models.users import User, LoginSchema, UserCreateTokenSchema
from models.token import Token
from utils.user import get_current_user
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from dotenv import load_dotenv
import os

load_dotenv()

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = "HS256"

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/token")


@router.post('/token', response_model=Token)
async def get_token(request: Request, form: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = authenticate_user(form.username, form.password)

    if user:
        token = create_access_token(user.username, user.id, timedelta(minutes=20))
        return {"access_token": token, "token_type" : "bearer"}
    return HTTPException(status_code=401, detail="Could not validated user.")

def authenticate_user(username: str, password: str):
    current_user = User.get_or_none(User.username == username)
    if current_user:
       bcrypt_context.verify(password, current_user.password)
       return current_user
    raise HTTPException(status_code=401, detail="Could not validated user.")

def create_access_token(username: str, id: int, expires: timedelta):
    encode = {'sub': username, 'id': id}
    expires = datetime.utcnow() + expires
    encode.update({'exp': expires})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)

async def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get('sub')
        user_id: int = payload.get('id')
        if username is None or user_id is None:
            return HTTPException(status_code=401, detail="Could not validated user.")
        return {'username': username, 'id': user_id}
    except JWTError:
        return HTTPException(status_code=401, detail="Could not validated user.")
        
    
