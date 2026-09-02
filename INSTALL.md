# Install (read this first)

You are installing a Crafting Agent UI pattern onto the **current org**. Follow this file, then the pattern-specific INSTALL.md.

You have no extra context beyond this repository and tools available in this session (`cs` CLI after you are in a workspace, template/sandbox listing, model listing).

## 1. Get this repository into a workspace

If the files of `https://github.com/crafting-demo/agent-patterns` are **already** in the current workspace, use them. Do not clone again.

Otherwise:

1. Create a sandbox from this git repository (the URL the user pasted).
2. Target a workspace in that sandbox **immediately**. Do not stop to ask whether to open it.
3. Hand off to the workspace agent so you can run `cs`.

This is an install, not an exploration. After the sandbox exists, keep going until the pattern resources are created and you have printed the example prompt.

Work from the repository root (the directory that contains this `INSTALL.md`).

## 2. Choose shared vs personal agents

Prefer org-shared agents:

```sh
cs llm agent create NAME --shared FILE.yaml
```

If create fails because you are not an org admin, omit `--shared` (personal agents) and use the same omit on `update`.

If an agent already exists, update it instead of failing:

```sh
cs llm agent update NAME --shared FILE.yaml
```

Agent names are at most 20 characters: lowercase letters, digits, and dashes.

## 3. Which pattern?

Read the user message.

- If they asked for the **engineering manager** pattern, continue at `patterns/engineering-manager/INSTALL.md`.
- If they asked for the **agent eval** pattern, continue at `patterns/agent-eval/INSTALL.md`.
- If they asked for both, do engineering manager first, then agent eval.

## 4. When you are done

Print, verbatim, the example prompt from that pattern’s `example-prompt.md`, and tell the user:

- which agent to select for the next session
- not to set a session model override for agent eval
- that install is finished
