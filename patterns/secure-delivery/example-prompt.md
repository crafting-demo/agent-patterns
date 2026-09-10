Deliver a small, self-contained change using a sandbox from this org. Do not open a pull request. Leave the sandbox running when done.

Pick a template:

- If I named a template, use that.
- Otherwise list templates in this org and pick a simple app or workspace template, not an empty stub.

Task:

1. In that sandbox, add `~/AGENT_PATTERNS_NOTE.md` with the template name, sandbox name, and one short paragraph on how someone would start services (`cs up` / `cs ps`, or say no daemons).
2. Have `qa-engineer` confirm the file exists and that the paragraph matches `cs ps`.
3. If the sandbox (or template) exposes an HTTP endpoint, have `security-scanner` scan that URL and report findings. If there is no URL, skip the scan and say why. Do not write exploits. If the scanner reports issues in **this** change, send them back to `software-engineer` to fix (the note file is not an HTTP app — do not invent vulnerabilities in it).

Work is done when local QA has passed, and the scan has either completed or been skipped.
