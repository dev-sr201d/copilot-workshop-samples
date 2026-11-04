import pytest
from fastapi.testclient import TestClient


@pytest.mark.parametrize(
    ("query", "expected_names"),
    [
        ("", ["Empty box", "Pencil", "Notebook"]),
        ("?max_quantity=0", ["Empty box"]),
        ("?max_quantity=2", ["Empty box", "Pencil"]),
        ("?max_quantity=99", ["Empty box", "Pencil", "Notebook"]),
    ],
    ids=["omitted", "zero", "inclusive", "all"],
)
def test_low_stock_filter(
    client: TestClient, query: str, expected_names: list[str]
) -> None:
    for name, quantity in [("Empty box", 0), ("Pencil", 2), ("Notebook", 8)]:
        created = client.post("/items", json={"name": name, "quantity": quantity})
        assert created.status_code == 201
    response = client.get(f"/items{query}")
    assert response.status_code == 200
    assert [item["name"] for item in response.json()] == expected_names


@pytest.mark.parametrize("threshold", ["-1", "abc", "1.5"])
def test_invalid_low_stock_threshold(client: TestClient, threshold: str) -> None:
    response = client.get("/items", params={"max_quantity": threshold})
    assert response.status_code == 422
    assert response.json()["detail"][0]["loc"] == ["query", "max_quantity"]


def test_no_low_stock_matches(client: TestClient) -> None:
    assert client.post("/items", json={"name": "Pen", "quantity": 5}).status_code == 201
    response = client.get("/items?max_quantity=0")
    assert response.status_code == 200
    assert response.json() == []
    unfiltered = client.get("/items")
    assert unfiltered.status_code == 200
    assert len(unfiltered.json()) == 1


def test_filter_empty_store(client: TestClient) -> None:
    response = client.get("/items?max_quantity=0")
    assert response.status_code == 200
    assert response.json() == []


def test_threshold_is_documented(client: TestClient) -> None:
    response = client.get("/openapi.json")
    assert response.status_code == 200
    parameters = response.json()["paths"]["/items"]["get"]["parameters"]
    threshold = next(param for param in parameters if param["name"] == "max_quantity")
    assert threshold["required"] is False
    variants = threshold["schema"]["anyOf"]
    assert any(part.get("minimum") == 0 for part in variants)
