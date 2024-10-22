from transcribinoff.app import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_app():
    assert app.title == "TranscribinOff"
    assert app.description == "TranscribinOff is a web application that allows users to transcribe audio files."


def test_users_router():
    response = client.get("/users")
    assert response.status_code == 200
    assert "users" in response.json()