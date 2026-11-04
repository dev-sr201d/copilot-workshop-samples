# Feature specification: inventory name search

**Feature ID:** 001-item-search
**Checkpoint:** m5-speckit
**Status:** Prepared implementation available
**Date:** 2026-11-04

## User stories

### US1 (P1): find items by part of their name

As a stockroom worker, I want case-insensitive substring name search so that
I can find an item without knowing its exact spelling or capitalization.

Given "Blue Pen", "Pencil" and "Notebook", when name=pen is supplied, return
"Blue Pen" and "Pencil" in their original insertion order.

### US2 (P2): keep the unfiltered list unchanged

As an existing API client, I want GET /items to behave exactly as before when I
do not search, so that adding search does not break current integrations.

Given "Blue Pen" and "Pencil", when name is omitted, empty or only whitespace,
return both items in insertion order with the unchanged Item shape.

## Functional requirements

* FR-001: Add optional `name` query parameter to GET /items.
* FR-002: Trim the query's leading/trailing whitespace. Omitted, empty or
  whitespace-only query means no name filter.
* FR-003: Match a substring using Unicode casefold on both query and stored
  name, not a regular expression. A query "STRASSE" matches a stored German
  sharp-s spelling of that word. Do not mutate stored names.
* FR-004: Preserve insertion order for filtered and unfiltered results.
* FR-005: Return HTTP 200 and [] for unmatched searches or an empty store.
* FR-006: Keep the Item response shape and all unrelated routes unchanged.
* FR-007: Document name as an optional query string in OpenAPI.

## Clarifications

* Search is literal substring, not prefix-only, fuzzy search or regular expression.
* No sorting, pagination, locale-specific transliteration or new validation cap.
* Empty query intentionally behaves like omitted query.
* Stored names are not trimmed or rewritten as part of this feature.
* Name is the only filter. Other list filters are out of scope for this feature.

## Success criteria

All FR requirements have passing HTTP tests, including Unicode, empty results,
non-mutation and query documentation. Existing tests and ruff checks pass.
No dependency, service, persistence or unrelated contract changes.
