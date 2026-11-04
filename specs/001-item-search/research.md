# Research and clarification decisions

Prepared reasoning, not an external research transcript.

* **Substring rather than exact match:** matches the worker's partial-name task;
  "pen" must match both "Blue Pen" and "Pencil".
* **Unicode casefold rather than lower:** caseless matching should handle
  sharp-s expanding to "ss". No locale/transliteration service is needed.
* **Trim query only:** forgiving input without silently modifying inventory data.
* **Empty means no filter:** optional input should not accidentally hide all data.
* **Store-level filtering:** keep filtering in ItemStore.list next to the data;
  keep HTTP parsing and OpenAPI documentation in the router.
* **No regex:** user text is literal; punctuation such as "." has no special meaning.

Evidence: existing list_items and ItemStore.list on m3-complete, Item model and the
per-app TestClient fixture. No external API or MCP dependency.
