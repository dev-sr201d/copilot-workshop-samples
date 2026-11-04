# Data model

No persisted fields or migrations are added.

Item remains `{id: int, name: str, quantity: int}`. ItemStore remains a
per-application insertion-ordered map of integer IDs to Item models.

`name` is an optional request-only string. A derived normalized query is
`query.strip().casefold()`; comparison uses `item.name.casefold()`. These values
are not stored. No indexes, caches, new entities or lifecycle transitions are
introduced.
