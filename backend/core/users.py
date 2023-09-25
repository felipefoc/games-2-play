from fastapi import APIRouter, Depends
from models.users import User, UserCreateSchema, UserRetrieveSchema# UserListSchema
from database import get_db
from sqlalchemy.orm import Session
from .authentication import bcrypt_context

router = APIRouter(
    prefix="/users",
    tags=["user"]
)

@router.post("", description="Create a simple user", status_code=201)
async def create_user(user: UserCreateSchema, db: Session = Depends(get_db)) -> UserRetrieveSchema:
    db_user = User(
        username=user.username,
        password=bcrypt_context.hash(user.password),
        is_active=True,
    )
    return db_user.save(db)

@router.get("", description="List of registred users")
async def get_users(db: Session = Depends(get_db)) -> list[UserRetrieveSchema]:
    return db.query(User).all()
