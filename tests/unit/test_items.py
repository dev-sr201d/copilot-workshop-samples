from fastapi.testclient import TestClient


def test_health(client: TestClient) -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_and_get_item(client: TestClient) -> None:
    response = client.post("/items", json={"name": "Notebook", "quantity": 3})
    assert response.status_code == 201
    assert response.json() == {"id": 1, "name": "Notebook", "quantity": 3}
    fetched = client.get("/items/1")
    assert fetched.status_code == 200
    assert fetched.json() == response.json()


def test_list_items_starts_empty(client: TestClient) -> None:
    response = client.get("/items")
    assert response.status_code == 200
    assert response.json() == []
