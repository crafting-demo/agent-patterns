# Hub-sourced agents

Three patterns use agents from the Crafting Agent Hub: [vendor contract review](patterns/vendor-contract-review), [secure delivery](patterns/secure-delivery), and [backlog to reviewed change](patterns/backlog-to-change).

Their YAML is compiled and **committed to this repository**. Installing a pattern reads only this checkout; it never clones or builds the hub. Every vendored file opens with a comment naming its hub package, the exact commit it was compiled from, and the command that produced it.

Vendored from [crafting-demo/agent-hub](https://github.com/crafting-demo/agent-hub) at commit [`b9ba570`](https://github.com/crafting-demo/agent-hub/commit/b9ba5702addf7bc6277d1d0575e6cbafa73202e7) (2026-09-10).

| Pattern | Agents | Sandbox templates |
| --- | --- | --- |
| Vendor contract review | `contract-analyst`, `compliance-reviewer`, `legal-counsel` | `hub-contract-analyst`, `hub-compliance-reviewer` |
| Secure delivery | `software-engineer`, `qa-engineer`, `security-scanner`, `engineering-manager` | `hub-software-engineer`, `hub-qa-engineer`, `hub-security-scanner` |
| Backlog to reviewed change | `product-manager`, `software-engineer`, `qa-engineer`, `security-scanner`, `code-reviewer`, `engineering-manager` | `hub-product-manager`, `hub-software-engineer`, `hub-qa-engineer`, `hub-security-scanner`, `hub-code-reviewer` |

An agent that ships skills or a CLI carries a sandbox template, and its `exec.use_template.name` points at `hub-<id>`. Create the template before the agent. Coordinators (`legal-counsel`, `engineering-manager`) have no template and reference their specialists by name, so create specialists first — including `security-scanner`, which `engineering-manager` names even when a pattern's task does not need a scan.

At this pin the hub collapsed four overlapping roles into the agents that already owned the job. Every id and template name above is unchanged, so the install steps and example prompts are unaffected, but four personas grew a second mode: `product-manager` also writes requirements with locked `D-nn` decisions, `engineering-manager` also writes `ENGINEERING.md` (and so now takes `transfer_to_workspace`), `qa-engineer` also verifies through Kubernetes interception, and `code-reviewer` absorbed the standalone security review.

## Refreshing to a newer hub version

Personas are edited in the hub, not here. To pull a newer version:

```sh
git clone https://github.com/crafting-demo/agent-hub   # or git pull in an existing checkout
cd agent-hub
python3 scripts/build.py --all
```

Then copy `dist/<id>/agent.yaml` to `patterns/<pattern>/agents/<id>.yaml` and `dist/<id>/template.yaml` to `patterns/<pattern>/templates/hub-<id>.yaml`, keeping the header comment and updating its `Source` and `Commit` lines to the new hub commit. Update the commit above too.

`software-engineer`, `qa-engineer`, `security-scanner`, and `engineering-manager` appear in two patterns. Refresh every copy at the same commit so the patterns do not drift apart.

`product-manager` is vendored with **no ticket board bound**, which works from a pasted backlog. To attach your org's Jira or Linear MCP, rebuild that one package with a provider and re-vendor it:

```sh
python3 scripts/build.py product-manager --provider ticket_board=jira
```
