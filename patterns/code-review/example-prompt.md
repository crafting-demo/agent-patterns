Review the current change. Do not patch, do not open a pull request, and do not spawn an implementer.

If I named a sandbox and workspace, use those. Otherwise list Ready sandboxes in this org, pick one that looks like an app (not an empty stub), and review there.

Diff to review:

- Prefer `git diff` against the default branch.
- If that is empty, `git diff HEAD` (uncommitted).
- If that is also empty, review the most recently changed tracked files and say this is a tree review, not a PR.

Have quality, logic, and security specialists each review that same diff in their own session (read-only: they may read and run tests, they must not edit). Merge into one report:

- **Critical** — must fix before merge
- **Suggestions**
- **Good practices**

Leave the sandbox as you found it. If there are Critical items, say that `em-manager` could take this sandbox and the review; do not implement.
