from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_add_expense():
    response = client.post("/expenses", json={
        "id": 1,
        "title": "Lunch",
        "amount": 150.0,
        "category": "Food",
        "date": "2026-06-01"
    })
    assert response.status_code == 201
    assert response.json()["expense"]["title"] == "Lunch"

def test_get_expenses():
    response = client.get("/expenses")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_total():
    response = client.get("/expenses/total")
    assert response.status_code == 200
    assert "overall_total" in response.json()