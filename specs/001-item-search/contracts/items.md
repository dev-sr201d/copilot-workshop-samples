# GET /items contract

| Parameter | Type | Required | Behavior |
|---|---|---|---|
| name | string | No | Trim query, casefold substring; blank means no filter |

Preserve insertion order.

Success: 200, JSON array of Item objects with id/name/quantity. Empty array is
valid. Stored spelling and quantities are unchanged. No new error envelope is
introduced.

Examples, given Blue Pen quantity 2 (id 1), Pencil quantity 5 (id 2):

* `/items?name=pen`: both items, id 1 then id 2.
* `/items?name=%20%20PEN%20%20`: both items (trimmed, case-insensitive).
* `/items?name=cil`: only id 2.
* `/items?name=notebook`: [].
* `/items?name=`: both items, unchanged from `/items`.

Runtime OpenAPI (`/openapi.json`) is the executable schema; tests verify the
optional name query and preserve the existing Item response.
