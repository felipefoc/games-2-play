from core.test.factories.users import UserFactory
from database import SessionLocal

db = SessionLocal()

def test_create_user(client):
    data = {
        "username": 'TestUser2',
        "password": 'SecretPass'
    }
    response = client.post("/users", json=data)
    assert response.status_code == 201
    assert response.json() == {
        "username": data['username'],
        "id": 1
    }

def test_list_user(client, factory_boy):
    user1 = UserFactory().save(db)
    user2 = UserFactory().save(db)
    user3 = UserFactory().save(db)
    db.session.refresh()

    response = client.get("/users")
    assert response.status_code == 200
    assert response.json() == [
        {
            'username': user1.username,
            'id': user1.id
        },
        {
            'username': user2.username,
            'id': user2.id
        },
        {
            'username': user3.username,
            'id': user3.id
        },
    ]