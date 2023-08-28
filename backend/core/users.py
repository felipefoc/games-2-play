from fastapi import APIRouter
from models.users import User, UserBaseSchema, UserCreateSchema, UserListSchema
from .authentication import bcrypt_context

router = APIRouter(
    prefix="/users",
    tags=["user"]
)

@router.post("/", description="Create a simple user", status_code=201)
async def create_user(user: UserCreateSchema) -> UserBaseSchema:
    db_user = User(
        username=user.username,
        password=bcrypt_context.hash(user.password),
        is_active=True,
    )
    db_user.save()
    return UserBaseSchema(**db_user.to_dict())

@router.get("/", description="List of registred users")
async def get_users() -> UserListSchema:
    db_query = User.select()
    db_users = [UserBaseSchema(**user) for user in db_query.dicts()]
    return UserListSchema(users=db_users)