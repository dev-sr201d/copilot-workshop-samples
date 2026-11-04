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

    def list(self, name: str | None = None) -> list[Item]:
        normalized_name = name.strip().casefold() if name else ""
        return [
            item
            for item in self._items.values()
            if not normalized_name or normalized_name in item.name.casefold()
        ]

    def get(self, item_id: int) -> Item | None:
        return self._items.get(item_id)

    def delete(self, item_id: int) -> bool:
        return self._items.pop(item_id, None) is not None
