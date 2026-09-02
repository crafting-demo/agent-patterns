# Eval matrix

Two prompts × two model slots. Agent names are stable; INSTALL writes the real `provider:name` into each YAML `model:` field.

| | Slot A (`REPLACE_SLOT_A` until install) | Slot B (`REPLACE_SLOT_B` until install) |
| --- | --- | --- |
| Prompt `minimal` | `ev-min-a` | `ev-min-b` |
| Prompt `thorough` | `ev-thr-a` | `ev-thr-b` |

- **minimal** — smallest change that passes public tests. Source: `prompts/minimal.md`.
- **thorough** — production-quality; follow the full spec. Source: `prompts/thorough.md`.

Models must already exist in the org LLM catalog as `provider:name`. You do not need to assign CODING or FAST. Both slots must actually complete the kata; a provider error is not a score for that model.

OpenRouter (or any OpenAI-compatible router) is a provider with `--backend=openai` and a custom `base_url`, then `cs llm model create`.
