Run this pattern as **three separate sessions**. Do not set a session model override.

---

## Session 1 — select `product-manager`

Turn this into a v1 spec (and a sprint slice if a ticket board is bound). Do not write application code.

Problem: internal users need a **weekly team digest** page that lists shipped PRs, open incidents, and who is on support, so they stop scraping five tools by hand.

If a ticket board is configured, search related tickets and link them. If it is not, work from this text and say so.

Write `~/REQUIREMENTS.md` in a sandbox from a template in this org (or the one I named). Include problem, audience, v1 scope, non-goals, success metrics, and open questions.

When that file exists, stop and tell me to start engineering-manager on the same sandbox.

---

## Session 2 — select `engineering-manager`

Implement the spec in the sandbox the product manager named (or create from the template I name). Do not open a pull request. Leave the sandbox running.

Have `software-engineer` implement, then `qa-engineer` verify. Loop on failures.

Work is done when local QA has passed. Tell me the sandbox and workspace so code-reviewer can join it.

---

## Session 3 — select `code-reviewer`

Review the current change in that sandbox (read-only). Prefer `git diff` against the default branch, else `git diff HEAD`, else a tree review.

Publish one Critical / Suggestions / Good practices review. Do not patch.
