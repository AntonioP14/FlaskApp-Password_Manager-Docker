import pytest
from app import create_app, db
from app.models import Password

@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })

    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

def test_index(client):
    response = client.get("/")
    assert b"Password Manager" in response.data

def test_add(client):
    response = client.post("/add", data={
        "service": "GitHub",
        "username": "test_user",
        "password": "test_pass"
    }, follow_redirects=True)
    assert b"GitHub" in response.data
