---
name: tool-versions
description: Version numbers, model names, and product identity/rebrand tracking for major agentic coding tools — check for drift each cycle.
metadata:
  type: reference
---

Snapshot as of 2026-07-11. Verify current state before quoting in future reports — names and versions have been shifting fast.

## Models (frontier — cross-reference with frontier-watch-reporter, don't duplicate deep analysis)
- Claude: Sonnet 5 (launched 2026-06-30, new tokenizer, pricing ramps 2026-08-31), Opus 4.8 (cited as leading SWE-bench Pro active model), "Fable 5" (moving from plan-included to usage-credit billing after 2026-07-12 — note: "Fable" is Anthropic's own naming here, distinct from any unrelated internal Claude Agent SDK model aliases).
- OpenAI: GPT-5.6 (incl. "Sol" and "Sol Ultra" variants), GPT-5.5, GPT-5.4, GPT-5.3 Codex (older terminal-specialized checkpoint, still competitive on Terminal-Bench).
- Google: Gemini 2.5 Pro (Jules), Gemini 3.5 Flash (GA in Code Assist), Gemini 3 Flash (being deprecated from Copilot 2026-07-31 alongside Gemini 2.5 Pro).

## Products / rebrands to track
- **Windsurf → Devin Desktop** (Cognition). Cascade → Devin Local (Rust rewrite). Rebrand shipped 2026-06-02; Cascade retired 2026-07-01. Don't refer to "Windsurf/Cascade" as current product names going forward — use Devin Desktop/Devin Local.
- **Amp**: was a Sourcegraph product, now independent "Amp, Inc." (spinout announced this cycle). Sourcegraph retains code-search/enterprise business under CEO Dan Adler.
- **Cursor / Anysphere**: pending acquisition by SpaceX ($60B all-stock, expected close Q3 2026). Watch for the close and any renaming.
- **Google Gemini Code Assist / Gemini CLI (consumer tiers)**: being sunset in favor of unified "Antigravity" platform + Antigravity CLI. Jules is a separate, unaffected product (async, GitHub-integrated, cloud VM).
- **GitHub Copilot**: "Agentic Workflows" feature (public preview since Feb 2026) is the model-agnostic markdown-instruction automation layer (works with Copilot/Claude/Gemini/Codex) — distinct from the core Copilot Agent chat/CLI product. Was the subject of the GitLost disclosure.

## Specific version/patch numbers worth citing
- Claude Code GitHub Action v1.0.94 — patched the `[bot]`-actor-trust supply-chain flaw.

## Pricing notes
- Claude Sonnet 5: $2/$10 per M tokens (in/out) intro through 2026-08-31 → $3/$15 standard. New tokenizer inflates effective token counts up to 1.35x vs. old tokenizer — factor this in before comparing "flat" pricing across model generations.
- Fable 5: 50% of weekly plan usage free through 2026-07-12, then $10/$50 per M tokens (in/out) via usage credits, same as API pricing. No enterprise grace period.
