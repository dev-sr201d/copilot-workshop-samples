from inventory.models import Item, ItemCreate


class ItemStore:
    def __init__(self) -> None:
        self._items: dict[int, Item] = {}
        self._next_id = 1

    def create(self, payload: ItemCreate) -> Item:
        item = Item(id=self._next_id, **payload.model_dump())
        self._items[item.id] = item
        self._next_id += 1
        return item

    def list(self) -> list[Item]:
        return list(self._items.values())

    def get(self, item_id: int) -> Item | None:
        return self._items.get(item_id)

    def delete(self, item_id: int) -> bool:
        return self._items.pop(item_id, None) is not None
