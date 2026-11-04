from pydantic import BaseModel


class ItemCreate(BaseModel):
    name: str
    quantity: int = 1


class Item(ItemCreate):
    id: int
