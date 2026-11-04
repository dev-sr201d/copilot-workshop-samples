import pytest
from fastapi.testclient import TestClient


@pytest.mark.parametrize(
    ("query", "expected_names"),
    [
        ({}, ["Blue Pen", "Pencil", "Notebook", "Stra\u00dfe"]),
        ({"name": ""}, ["Blue Pen", "Pencil", "Notebook", "Stra\u00dfe"]),
        ({"name": "   "}, ["Blue Pen", "Pencil", "Notebook", "Stra\u00dfe"]),
        ({"name": "pen"}, ["Blue Pen", "Pencil"]),
        ({"name": "  PEN  "}, ["Blue Pen", "Pencil"]),
        ({"name": "ook"}, ["Notebook"]),
        ({"name": "STRASSE"}, ["Stra\u00dfe"]),
        ({"name": "missing"}, []),
        ({"name": "."}, []),
    ],
    ids=[
        "omitted",
        "empty",
        "whitespace",
        "substring",
        "trim-and-case",
        "middle-substring",
        "unicode",
        "no-match",
        "literal-not-regex",
    ],
)
def test_search_items(
    client: TestClient, query: dict[str, str], expected_names: list[str]
) -> None:
    for name, quantity in [
        ("Blue Pen", 2),
        ("Pencil", 5),
        ("Notebook", 0),
        ("Stra\u00dfe", 1),
    ]:
        created = client.post("/items", json={"name": name, "quantity": quantity})
        assert created.status_code == 201
    response = client.get("/items", params=query)
    assert response.status_code == 200
    assert [item["name"] for item in response.json()] == expected_names


def test_search_empty_store(client: TestClient) -> None:
    response = client.get("/items", params={"name": "pen"})
    assert response.status_code == 200
    assert response.json() == []


def test_search_does_not_mutate_items(client: TestClient) -> None:
    created = client.post("/items", json={"name": "  Blue PEN  ", "quantity": 3})
    assert created.status_code == 201
    original = created.json()
    searched = client.get("/items", params={"name": "pen"})
    assert searched.status_code == 200
    assert searched.json() == [original]
    fetched = client.get(f"/items/{original['id']}")
    assert fetched.status_code == 200
    assert fetched.json() == original
    all_items = client.get("/items")
    assert all_items.status_code == 200
    assert all_items.json() == [original]


def test_search_is_documented(client: TestClient) -> None:
    response = client.get("/openapi.json")
    assert response.status_code == 200
    parameters = response.json()["paths"]["/items"]["get"]["parameters"]
    name = next(parameter for parameter in parameters if parameter["name"] == "name")
    assert name["in"] == "query"
    assert name["required"] is False
    assert any(part.get("type") == "string" for part in name["schema"]["anyOf"])
