---
name: tool-versions
description: Version numbers, model names, and product identity/rebrand tracking for major agentic coding tools — check for drift each cycle.
metadata:
  type: reference
---

Snapshot as of 2026-07-27. Verify current state before quoting in future reports — names and versions have been shifting fast.

## 2026-07-27 update
- **Claude Opus 5** launched 2026-07-24: same $5/$25 per-M pricing as Opus 4.8, "near Fable 5 intelligence at half the price," Fast mode (2.5x speed/2x price), beta mid-conversation tool changes + safety-classifier auto-fallback. Default on Max, top tier on Pro. Remains "substantially behind Mythos 5" on cybersecurity exploitation specifically. Added to GitHub Copilot same day.
- **MCP spec still NOT shipped** as of 2026-07-27 — RC status unchanged, final ship still scheduled 2026-07-28. Confirm actual status next cycle.
- Cognition/Devin: **FedRAMP Class D (High) In-Process confirmed** (independently verified via FedRAMP Marketplace, no longer just secondary-sourced).

## Models (frontier — cross-reference with frontier-watch-reporter, don't duplicate deep analysis)
- Claude: Sonnet 5 (launched 2026-06-30, new tokenizer, pricing ramps 2026-08-31), Opus 4.8, "Fable 5" (general-purpose Mythos-class model, announced 2026-06-09; free-plan promotion ended 2026-07-19, now permanently bundled for Max/Team-Premium/legacy-Enterprise-Premium seats, metered $10/$50 per M tokens for Pro/standard seats), "Claude Mythos 5" (confirmed, same June 9 announcement as Fable 5 — functionally identical but with cybersecurity/biomedical safety restrictions lifted; restricted to Project Glasswing partners + vetted biomedical researchers; NOT an unannounced preview, despite being flagged that way in the 2026-07-11/07-13 reports — correct this going forward).
- OpenAI: GPT-5.6 three-tier family — Sol (flagship, $5/$30 per M), Terra (mid, $2.50/$15), Luna (fast/cheap, $1/$6) — broadly launched 2026-07-09. GPT-5.5, GPT-5.4, GPT-5.3 Codex (older terminal-specialized checkpoint, still competitive on Terminal-Bench).
- Google: Gemini 2.5 Pro (Jules), Gemini 3.5 Flash (GA in Code Assist), Gemini 3 Flash (being deprecated from Copilot 2026-07-31 alongside Gemini 2.5 Pro).
- Open-weight: Moonshot AI's Kimi K3 (2.8T total params, 16-of-896 experts active/token, 1M context, native vision) released 2026-07-17 — largest open-weight model to date, strongest open-weight coding result yet (see benchmarks.md).

## Products / rebrands to track
- **Windsurf → Devin Desktop** (Cognition). Cascade → Devin Local (Rust rewrite). Rebrand shipped 2026-06-02; Cascade retired 2026-07-01. Don't refer to "Windsurf/Cascade" as current product names going forward — use Devin Desktop/Devin Local.
- **Amp**: was a Sourcegraph product, now independent "Amp, Inc." Sourcegraph retains code-search/enterprise business under CEO Dan Adler.
- **Cursor / Anysphere**: pending acquisition by SpaceX ($60B all-stock, expected close Q3 2026). SpaceXAI + Cursor already co-shipped a joint model, "Grok 4.5" (launched 2026-07-08/09, $2/$6 per M tokens, good cost/perf but weaker frontend/UI quality vs. Fable/Opus).
- **Google Gemini Code Assist / Gemini CLI (consumer tiers)**: being sunset in favor of unified "Antigravity" platform + Antigravity CLI. Jules is a separate, unaffected product (async, GitHub-integrated, cloud VM).
- **GitHub Copilot**: "Agentic Workflows" feature (public preview since Feb 2026) is the model-agnostic markdown-instruction automation layer — distinct from the core Copilot Agent chat/CLI product.

## Specific version/patch numbers worth citing
- Claude Code GitHub Action v1.0.94 — patched the `[bot]`-actor-trust supply-chain flaw.
- Claude Code v2.1.207–v2.1.212 (Week 29, July 13-17): Artifacts→MCP connector calls, screen reader mode, `/fork`.
- GitHub Copilot CLI v1.0.71 (2026-07-16): always-on multi-turn subagents, tool search for Claude Haiku 4.5+.
- MCP Python SDK: v2.0.0a1 (June 11) → beta (June 30) → stable v2.0 targeted 2026-07-27, one day ahead of the final spec (2026-07-28).

## Pricing notes
- Claude Sonnet 5: $2/$10 per M tokens (in/out) intro through 2026-08-31 → $3/$15 standard. New tokenizer inflates effective token counts up to 1.35x vs. old tokenizer.
- Fable 5: promotion (plan-included) ended 2026-07-19 11:59:59pm PT. As of 2026-07-20: permanently bundled for Max/Team-Premium/legacy-Enterprise-Premium seats; $10/$50 per M tokens (in/out) via usage credits for Pro/standard Team/Enterprise seats, no grace period.
- GPT-5.6: Sol $5/$30, Terra $2.50/$15, Luna $1/$6 per M tokens (in/out).
- Grok 4.5 (SpaceXAI/Cursor): $2/$6 per M tokens.
