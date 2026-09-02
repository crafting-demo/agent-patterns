Diagnose this incident. Do not patch, do not open a pull request, and do not spawn an implementer. Leave the sandbox running when done.

Symptom:

Checkout `POST /api/cart/total` has been returning HTTP 500 on staging since 14:00 UTC. Product thinks it is the frontend. I need to know whether this reproduces in an isolated sandbox copy of the app, and whether the cluster path (intercept) matches.

Pick a template:

- If I named a template, use that.
- Otherwise list templates in this org and pick a simple one that has at least one workspace. Prefer a template whose name or description looks like an app or shop, not an empty stub.

Task:

1. Reproduce locally in a sandbox from that template. Start services with `cs up` / `cs ps`. Hit `POST /api/cart/total` with a small cart body if the app has that path. If it does not, say so and hit the closest health or API endpoint you can find — that is still evidence.
2. If the template has a Kubernetes intercept plan, repeat the same request through intercept and compare. If it does not, skip cluster and say why.
3. Write a diagnosis: what reproduced, where (local, intercept, both, neither), what you ruled out, sandbox name, and a recommended next step. If a product fix is indicated, say that a delivery coordinator such as `em-manager` could take this sandbox and the diagnosis. Do not implement the fix.

Work is done when that diagnosis is written. The sandbox stays up.
