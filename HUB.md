# Hub-sourced agents

Every pattern except [agent eval](patterns/agent-eval) installs agents from the Crafting Agent Hub. The hub is the source of truth for what an agent is; a pattern here is a team of hub agents plus an example task.

Their YAML is compiled and **committed to this repository**. Installing a pattern reads only this checkout; it never clones or builds the hub. Every vendored file opens with a comment naming its hub package, the exact commit it was compiled from, and the command that produced it.

Vendored from [crafting-demo/agent-hub](https://github.com/crafting-demo/agent-hub) at commit [`407e009`](https://github.com/crafting-demo/agent-hub/commit/407e00960213fb9ccc5c9013c82c4e067198e7e7) (2026-09-15).

| Pattern | Agents | Sandbox templates |
| --- | --- | --- |
| PDE team | `product-manager`, `design-lead`, `engineering-manager`, `software-engineer`, `qa-engineer`, `security-scanner`, `pde-lead` | `hub-security-scanner` |
| Engineering manager | `software-engineer`, `qa-engineer`, `security-scanner`, `engineering-manager` | `hub-security-scanner` |
| Incident commander | `incident-commander` | none |
| Code review | `code-reviewer` | none |
| Vendor contract review | `contract-analyst`, `compliance-reviewer`, `legal-counsel` | `hub-contract-analyst`, `hub-compliance-reviewer` |
| Secure delivery | `software-engineer`, `qa-engineer`, `security-scanner`, `engineering-manager` | `hub-security-scanner` |
| Backlog to reviewed change | `product-manager`, `software-engineer`, `qa-engineer`, `security-scanner`, `code-reviewer`, `engineering-manager` | `hub-security-scanner` |

Most agents no longer carry a template. As of the hub commit above, skills are compiled into the agent's `instructions`, so only an agent that needs a **CLI on disk** — or extra workloads beside it — gets one: `security-scanner`, `contract-analyst`, `compliance-reviewer`. Those three set `exec.use_template.name` to `hub-<id>`, and their template must exist before the agent. Everything else is a single `cs llm agent create`.

`hub-security-scanner` now has two workspaces: `scan` for the agent and its CLI, and `target` running OWASP Juice Shop, which the scanner hits at `http://target:3000` when a request names no URL. Every pattern that installs `security-scanner` gets that target, including the delivery patterns where the manager always names a real URL to scan.

Coordinators (`pde-lead`, `engineering-manager`, `legal-counsel`) reference their specialists by name, so create specialists first. `engineering-manager` names `security-scanner` even when a pattern's task never scans, and `pde-lead` names `engineering-manager`, so a PDE team install pulls the whole engineering team.

Agent names are org-wide. Two patterns that both install `qa-engineer` install the same file; the copies are kept byte-identical, and `cs llm agent update` on the second install is a no-op.

## Refreshing to a newer hub version

Personas are edited in the hub, not here. To pull a newer version:

```sh
git clone https://github.com/crafting-demo/agent-hub   # or git pull in an existing checkout
cd agent-hub
python3 scripts/build.py --all
```

Then copy `dist/<id>/agent.yaml` to `patterns/<pattern>/agents/<id>.yaml` and `dist/<id>/template.yaml` to `patterns/<pattern>/templates/hub-<id>.yaml`, keeping the header comment and updating its `Source` and `Commit` lines to the new hub commit. Update the commit above too.

If a build stops producing `dist/<id>/template.yaml`, delete the vendored `templates/hub-<id>.yaml` and drop its `cs template create` line from the pattern's `INSTALL.md`; leaving it behind creates a template no agent references.

Refresh every copy of an agent at the same commit so the patterns do not drift apart.

`product-manager` is vendored with **no ticket board bound**, which works from a pasted backlog and is all the definition phase needs. To attach your org's Jira or Linear MCP, rebuild that one package with a provider and re-vendor it:

```sh
python3 scripts/build.py product-manager --provider ticket_board=jira
```
