# Tasks: inventory name search

Prepared dependency-ordered task list. Checkboxes represent the curated
implementation, not a live Spec Kit agent log.

## Phase 1: intent and contract

- [x] T001 Review constitution and write FR-001..FR-007 in spec.md.
- [x] T002 Resolve empty queries, Unicode casefold and AND behavior in research.md.
- [x] T003 [P] Document query/response contract in contracts/items.md.
- [x] T004 [P] Document unchanged storage model and derived search values in data-model.md.

T002 depends on T001; T003/T004 depend on T002 and can run independently.

## Phase 2: US1 (P1), basic search

- [x] T005 Write HTTP tests for omitted/empty/whitespace, case, substring,
  Unicode, no match and empty store in tests/unit/test_item_search.py.
- [x] T006 Add normalized, non-mutating optional name filtering to ItemStore.list.
- [x] T007 Wire optional name query into list_items and document in OpenAPI.

T005 depends on T002; T006 depends on T005; T007 depends on T006.

## Phase 3: US2 (P2), unchanged unfiltered list

- [x] T008 Test omitted, empty and whitespace queries return every item in
  insertion order, and that search does not mutate stored values or change
  the Item response shape.

T008 depends on T007.

## Phase 4: verification and handoff

- [x] T009 Run targeted tests, full pytest, lint and format checks from plan.md.
- [x] T010 Update requirements checklist and quickstart; inspect each FR against
  code/tests and report limitations without inventing slash-command results.

T009 depends on T008; T010 depends on T009.
