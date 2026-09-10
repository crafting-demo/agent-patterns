# Hub install (shared)

Hub definitions live in the private repo [crafting-demo/agent-hub](https://github.com/crafting-demo/agent-hub). This file is how a pattern INSTALL.md compiles those packages into `cs llm agent create` YAML.

Work from a workspace where `cs` and `python3` (PyYAML) run.

## 1. Get agent-hub

Prefer an existing checkout:

- If `agent-hub/` already exists next to this `agent-patterns` checkout (sibling directory) or inside the current workspace as `agent-hub/`, use it. `git pull` on the default branch.
- Otherwise clone `https://github.com/crafting-demo/agent-hub` (SSH `git@github.com:crafting-demo/agent-hub.git` if HTTPS is denied). The repo is **private**; the session must already be able to clone it.

Do not copy hub files into agent-patterns.

## 2. Compile and create

From the agent-hub root, for each `AGENT` in the order the pattern INSTALL.md lists (specialists before coordinators):

```sh
python3 scripts/build.py AGENT
# optional: python3 scripts/build.py product-manager --provider ticket_board=jira

if [ -f "dist/AGENT/template.yaml" ]; then
  cs template create "hub-AGENT" "dist/AGENT/template.yaml" \
    || cs template update "hub-AGENT" "dist/AGENT/template.yaml"
fi

cs llm agent create AGENT --shared "dist/AGENT/agent.yaml" \
  || cs llm agent update AGENT --shared "dist/AGENT/agent.yaml"
```

Omit `--shared` if you are not an org admin (same omit on `update`).

`cs template validate dist/AGENT/template.yaml` is optional but useful when logged in.

## 3. Verify

```sh
cs llm agent list
cs llm agent show COORDINATOR --shared
```

Then print the pattern's `example-prompt.md` and tell the user which agent to select in a **new** session.
