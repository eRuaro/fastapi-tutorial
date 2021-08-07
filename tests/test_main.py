from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() ==  {"Greetings": "Welcome to FastAPI!"}

def test_post_method_add():
    key = "FastAPI"
    value = "tutorial"
    response = client.post(f"/add/{key}-{value}")
    assert response.status_code == 200
    assert response.json() == f"Key-value pair {key}-{value} added"

def test_get_method_get():
    key = "FastAPI"
    expected_value = "tutorial"
    response = client.get(f"/get/{key}")
    assert response.status_code == 200
    assert response.json() == expected_value

def test_get_method_get2():
    key = "Flask"
    expected_value = None
    response = client.get(f"/get/{key}")
    assert response.status_code == 200
    assert response.json() == expected_value