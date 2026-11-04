from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Query, Request, Response
from fastapi.responses import JSONResponse

from inventory.models import Item, ItemCreate
from inventory.store import ItemStore

router = APIRouter(prefix="/items", tags=["items"])


def get_store(request: Request) -> ItemStore:
    return request.app.state.store


Store = Annotated[ItemStore, Depends(get_store)]


@router.post("", response_model=Item, status_code=201)
def create_item(payload: ItemCreate, store: Store) -> Item:
    return store.create(payload)


@router.get("", response_model=list[Item])
def list_items(
    store: Store,
    name: Annotated[
        str | None,
        Query(description="Case-insensitive substring; trim query; blank means all."),
    ] = None,
) -> list[Item]:
    return store.list(name=name)


@router.get("/{item_id}", response_model=Item)
def get_item(item_id: int, store: Store) -> Item | JSONResponse:
    item = store.get(item_id)
    if item is None:
        return JSONResponse(status_code=404, content={"error": "Item not found"})
    return item


@router.delete("/{item_id}", status_code=204)
def delete_item(item_id: int, store: Store) -> Response:
    if not store.delete(item_id):
        raise HTTPException(status_code=404, detail="Item not found")
    return Response(status_code=204)
