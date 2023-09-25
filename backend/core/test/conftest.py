import sys
import os
TEST_DB = "sqlite:///./pytest.sqlite"
os.environ['DATABASE_URL'] = TEST_DB
sys.path.append('/home/felipe/games-2-play/backend')
from pytest_factoryboy import register
from core.test.factories.users import UserFactory
import pytest
from typing import Generator
from fastapi.testclient import TestClient
from database import Base, engine
from main import app

@pytest.fixture(scope="function")
def factory_boy():
    register(UserFactory)

@pytest.fixture(scope="session", autouse=True)
def test_db():
    Base.metadata.create_all(bind=engine)
    yield # CODIGO DO TESTE
    Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="function")
def client() -> Generator:
    with TestClient(app) as c:
        yield c