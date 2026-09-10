# Sources

The agents these patterns install are defined in [crafting-demo/agent-hub](https://github.com/crafting-demo/agent-hub). Attribution for each agent lives there: the hub's [SOURCES.md](https://github.com/crafting-demo/agent-hub/blob/main/SOURCES.md) has the table, each agent's `manifest.yaml` lists its `sources`, and each agent's `README.md` explains what was taken from where. The hub's bar is an official vendor publication, a GitHub repository with at least 10,000 stars, or a published standard.

What this repository adds is the Crafting-side wiring (sandbox join, `cs`, org-shared agents, sub-agent fan-out) and the example tasks. We do not vendor other vendors' plugin files.

## Shared ideas (all patterns)

| Idea | Where it is published |
| --- | --- |
| Specialists in **isolated context**, parent only sees the summary | [Anthropic: Create custom subagents](https://code.claude.com/docs/en/sub-agents) |
| Do not mix implement and review in one session; review the diff in a **fresh** subagent | [Anthropic: Best practices for Claude Code](https://code.claude.com/docs/en/best-practices) |
| Sequential pipeline: write, then review (we do **not** auto-refactor in the reviewer) | [Google ADK SequentialAgent](https://github.com/google/adk-docs/blob/main/docs/agents/workflow-agents/sequential-agents.md) |
| Durable project norms live in-repo (`AGENTS.md`, `CLAUDE.md`, `CONTRIBUTING.md`) | [OpenAI Codex AGENTS.md](https://developers.openai.com/codex/guides/agents-md), Anthropic `CLAUDE.md` |

## Per pattern

Pointers into the hub for the agents each pattern uses. Star counts are the hub's snapshots.

- **PDE team**: `pde-lead` and `product-manager` follow Get Shit Done ([gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done), 64.5k, archived; live successor [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core)) for gray-area questions and locked `D-nn` decisions, plus Anthropic's [product-management plugin](https://github.com/anthropics/knowledge-work-plugins/tree/main/product-management) for spec shape. `design-lead` follows Anthropic's [frontend-design](https://github.com/anthropics/claude-code/tree/main/plugins/frontend-design) plugin and OpenAI's [frontend-skill](https://developers.openai.com/blog/designing-delightful-frontends-with-gpt-5-4). `engineering-manager` in definition mode follows the GSD planner and roadmapper and Anthropic's plan-before-code guidance.
- **Engineering manager** and **secure delivery**: `engineering-manager` follows Google ADK's writer-then-reviewer sequence and Anthropic's fresh-session verification. `qa-engineer` uses [Playwright](https://github.com/microsoft/playwright) for UI flows and Crafting's [Kubernetes intercept plan](https://docs.sandboxes.cloud/guides/developers/kubernetes-intercept-plan.html) for the cluster pass. `security-scanner` is Crafting's webscan CLI-in-template pattern with [lonkero](https://github.com/bountyyfi/lonkero).
- **Incident commander**: same read-only contract as Anthropic's reviewer agents (reproduce and report, do not patch), in a fresh session so diagnosis is not graded by the session that would want to fix it.
- **Code review**: the three lenses map onto Anthropic's [pr-review-toolkit](https://github.com/anthropics/claude-code/tree/main/plugins/pr-review-toolkit) specialist split and the read-only `code-reviewer` / `security-reviewer` contract in the [subagents docs](https://code.claude.com/docs/en/sub-agents). Output shape is GitHub Copilot's [review-code](https://docs.github.com/en/copilot/tutorials/customization-library/prompt-files/review-code) prompt. Security taxonomy is OWASP Top 10 and CWE.
- **Vendor contract review**: Anthropic's [knowledge-work-plugins legal](https://github.com/anthropics/knowledge-work-plugins/tree/main/legal) and [claude-for-legal](https://github.com/anthropics/claude-for-legal); [pandoc](https://github.com/jgm/pandoc) for `.docx`. Draft for attorney review. The sample MSA is an original fixture.
- **Backlog to reviewed change**: the product-management plugin for the PM, the engineering split above for delivery, the Copilot review shape for the gate.

## Agent eval

The one pattern that is not hub-backed. Isolated trial sessions follow Anthropic subagent isolation (each cell is a new context); independent repeats so one lucky run does not decide the ranking. Eval hygiene, not a vendor plugin. It stays here because it needs install-time model placeholders the hub does not compile yet.
