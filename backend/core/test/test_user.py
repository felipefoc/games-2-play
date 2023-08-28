import sys
sys.path.append('/home/felipe/toplay')
from httpx import AsyncClient
from main import app
from models.users import User
import pytest
import peewee

database = peewee.SqliteDatabase("AAAAAAAAAAAAAAAAA.db", check_same_thread=False)

@pytest.fixture
def db():
    database.connect()
    database.create_tables([User])
    yield 
    database.drop_tables([User])
    database.close()

@pytest.mark.anyio
async def test_create_user(db):
    async with AsyncClient(app=app, base_url="http://") as ac:
        data = {
            "username": "__TheTestUser",
            "password": "123456"
        }
        response = await ac.post("/users/", json=data)
    assert response.status_code == 201
    assert response.json() == {"username": data["username"]}

@pytest.mark.anyio
async def test_list_users(db):
    async with AsyncClient(app=app, base_url="http://") as ac:
        users = [
            User.create(
                username=f"TestUser{i}", password=f"hashed{i}", is_active=True
            ) for i in range(2)
        ]
        response = await ac.get("/users/")

    assert response.status_code == 200
    resp = {"users": []}
    for u in users:
        resp["users"].append(
            {
                "username": u.username
            }
        )
    assert response.json() == resp

@pytest.mark.anyio
async def test_validate_username(db):
    async with AsyncClient(app=app, base_url="http://") as ac:
        User.create(username="TestUser", password="hashed123")
        data = {
            "username": "TestUser",
            "password": "123456"
        }
        response = await ac.post("/users/", json=data)
    assert response.status_code == 422
    assert response.json()["detail"][0]["loc"] == ["body", "username"]
    assert response.json()["detail"][0]["msg"] == "Value error, User with username 'TestUser' already exists"
    assert response.json()["detail"][0]["type"] == "value_error"