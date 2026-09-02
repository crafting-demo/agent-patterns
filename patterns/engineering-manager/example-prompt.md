Implement a small, self-contained change using a sandbox from this org. Do not open a pull request. Leave the sandbox running when done.

Pick a template:

- If I named a template, use that.
- Otherwise list templates in this org and pick a simple one that has at least one workspace. Prefer a template whose name or description looks like an app or workspace, not an empty stub.

Task:

1. In that sandbox, add a file `AGENT_PATTERNS_NOTE.md` at the workspace home directory (`~/AGENT_PATTERNS_NOTE.md`) with:
   - the template name
   - the sandbox name
   - one short paragraph on how someone would start services here (`cs up` / `cs ps` if the template defines daemons; otherwise say that no daemons are defined)
2. Have local QA confirm the file exists and that the paragraph is accurate given `cs ps` (or the lack of daemons).
3. If the template has a Kubernetes intercept plan, have integration start it and report status. If it does not, skip integration and say why.

Work is done when local QA has passed, and integration has either passed or been skipped because there is no intercept plan.
