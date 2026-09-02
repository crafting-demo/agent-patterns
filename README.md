# Agent patterns

Reusable Crafting Agent UI patterns. Each pattern is a set of custom agents (and, for eval, a sandbox template) you install on your own org.

These examples are not tied to a particular product, template, or site. After install, you point the engineering manager at *your* templates and issues, and the eval matrix at *your* org’s LLM catalog.

## One-prompt install

In Crafting Agent UI, start a **new session** with the default agent (do not pick a custom agent). Paste **one** of these lines as the entire message:

```
Set up the engineering manager pattern from https://github.com/crafting-demo/agent-patterns
```

```
Set up the agent eval pattern from https://github.com/crafting-demo/agent-patterns
```

That is enough. The default agent checks out this repository, follows [INSTALL.md](INSTALL.md), and prints what to run next.

You need permission to create org-shared agents (`cs llm agent create --shared`). If you are not an org admin, install still works as personal agents.

GitHub access: this repository is private. Checkout uses your org’s GitHub integration, the same as any other private repo.

## Patterns

| Pattern | When to use it | After install, start a session with |
| --- | --- | --- |
| [Engineering manager](patterns/engineering-manager/README.md) | One coordinator delegates implementation, local QA, and optional cluster verification to specialists. Each specialist run is its own session, so the manager keeps a small context. | `em-manager` |
| [Agent eval](patterns/agent-eval/README.md) | Compare **prompt × model** variants on the same task, with repeated trials, then rank them. | `eval-manager` |

## Remove

```sh
cs llm agent remove NAME --shared
```

Eval also creates template `eval-kata`:

```sh
cs template remove eval-kata
```
