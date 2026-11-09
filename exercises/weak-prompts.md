# Rewrite these prompts

Use Goal, Context, Constraints, Done when. Write your version before opening
the answer card. Run each comparison from a clean `m2-prompting` checkpoint
with a fresh chat and the same model.

## 1. Input validation

> Add input validation to the create-item endpoint.

Consider: Which values are valid? What should happen to whitespace? What is
the expected error shape? Which files and endpoints may change?

## 2. Add an endpoint

> Add a version endpoint.

Consider: Which method and path? Where does the version come from? What JSON
shape and status? How is the router registered? What must not change?

Record changed files, added tests, test results, assumptions and out-of-scope
changes for each run. Discuss predictability, not only which response looks
more polished.
