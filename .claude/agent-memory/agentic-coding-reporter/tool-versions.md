---
name: tool-versions
description: Version numbers, model names, and product identity/rebrand tracking for major agentic coding tools — check for drift each cycle.
metadata:
  type: reference
---

Snapshot as of 2026-09-07. Verify current state before quoting in future reports — names and versions have been shifting fast.

## 2026-09-07 update (short 2-day cycle)
- **GPT-6 Astra**: ARC-AGI-3 score is harness-dependent — 99.9% (OpenAI's "Provider Adapter" harness) vs. 62.7% (shared "Standard" harness). Cite the harness when quoting either number.
- **Cognition**: ~$47B round still NOT closed as of Sept 1 (correction to prior cycle). Devin ARR ~$900M+ (was $492M in May).
- **Google Antigravity**: added enterprise SSO (Workforce Identity Federation/Advanced SSO), Gemini 3.8 Flash access for AGY Enterprise tenants.
- **OpenAI**: disclosed internal research-org coding-agent usage at 3.1 agent-workdays/human-workday; "automated research intern" framing.

## 2026-09-05 update
- **OpenAI**: **GPT-6 Astra** launched 2026-09-03 — $10/$50 per M tokens (2.5x GPT-5.6 Sol), Fast mode 2x speed/2x price, 90%-off cached input, batch/flex half-price. First OpenAI model rated **Critical** for cybersecurity under Preparedness Framework. GA in GitHub Copilot 2026-09-04.
- **Anthropic**: **Claude Fable 5.1 and Mythos 5.1** launched 2026-09-01 — same $10/$50 per M rate as GPT-6 Astra, 75% cheaper cache reads, ~25% cheaper typical workloads vs. Fable 5. New SWE-bench Pro #1 (81.2%).
- **Cognition**: rebuffed reported SpaceX acquisition approach (Aug 19 denial); now closing own round near **$47B valuation** (Sept 3), up from $26B (May 2026).
- **GitHub Copilot**: code review can approve PRs (Sept 1, preview, off by default); GPT-6 Astra GA (Sept 4); unified Copilot Chat relaunch planned ≥Sept 28.
- **Claude Code**: weekly limits — 50% promo ends Sept 13, permanent 25% increase (net lower) starts Sept 14. No weekly digest published past Week 34 (Aug 17-21) as of this snapshot.
- **Amp**: `ultra` mode now on Fable 5.1 (Sept 1).
- **Security**: GitSpawn vuln class (Manifold Security, Sept 1-2) hit Claude Code, Codex, Cursor, Goose, Qwen Code, Grok Build, Hermes Agent — 4 of 7 still exploitable on Sept 1 retest.

## 2026-08-24 update
- **Cursor**: shipped **Origin** (beta, Aug 18) — GitHub-competing code host (repo hosting, PRs, two-way GitHub sync, agent push), rolled to all paid plans. First major post-SpaceX-acquisition product.
- **OpenAI Codex**: 20M active users (Aug 21, up from 8M July 19/20). New model: **GPT-5-Codex-Mini**.
- **GitHub Copilot**: Agent Plugins 1.0 now GA (was "shipped" 2026-08-06, now GA across VS Code/CLI/SDK/app as of this cycle). Kimi K3 and Grok 4.6 both rolling out.
- **Google Antigravity**: now bundled into Gemini Enterprise Standard/Plus licenses; new VS Code extension.
- **Claude Code**: Week 34 digest resumed (v2.1.234-ish) after a gap — `/design` research preview, Concise output style, remote-control device cards, `ANTHROPIC_DEFAULT_MODEL` env var.
- **MCP**: new roadmap published (Aug 22); Den Delimarsky promoted Lead Maintainer, Clare Liguori joins Core Maintainer group.
- **SWE-bench Verified**: Opus 5 96.0% (Aug 22 reading; note this is a slight dip from the 97.00% figure recorded Aug 14 — likely re-scoring noise, watch for stabilization).
- **Cognition**: $40B round for Devin still in talks, not closed, as of this cycle.

## 2026-08-17 update
- **SpaceX/Cursor acquisition CLOSED 2026-08-14** (was "pending, expected Q3 2026" as of all prior cycles) — Cursor is now a wholly-owned SpaceXAI unit. Update product-identity tracking: no longer "Cursor (Anysphere)" as an independent company.
- **Cognition** in talks to raise at $40B valuation (up from $26B in May) — not yet closed, revisit next cycle.
- **Agent Plugins 1.0** (2026-08-06) — new open standard, NOT an MCP replacement; packages skills+MCP servers for distribution. Maintainers: Vercel (initiator), AWS, Anysphere, GitHub, Microsoft, OpenAI, Google.
- **Meta Muse Code** (beta, 2026-08-05) — new product, model "Muse Spark 1.2," $1.25/$4.25 per M tokens.
- **Claude Code**: auto mode now default (not opt-in) for Pro/Max/Team as of 2026-08-14. Latest versions seen: v2.1.229-233 (Aug 12-14).
- **Codex CLI**: MCP SDK bumped to 3.0.0 (matches 2026-07-28 MCP spec); Linux desktop app preview imports from Claude Code/Cursor.
- **SWE-bench Verified**: Claude Opus 5 now leads at 97.00% (Aug 14 snapshot) — update from any older Opus 4.8-era reading.

## 2026-08-03 update
- **MCP spec 2026-07-28 shipped stable** (confirmed, ending 3-cycle "still RC" tracking). Stateless core final; Tasks is a versioned extension.
- **MCP Python SDK v2.0.0 shipped stable 2026-07-28** — new `Dispatcher` pipeline replaces `ServerSession`; breaking for unpinned dependents.
- **GPT-5.6 pricing cut 2026-07-30**: Luna $1/$6→$0.20/$1.20 per M (-80%), Terra $2.50/$15→$2/$12 (-20%), Sol unchanged $5/$30. GPT-5.4/5.4-mini retire from ChatGPT-auth Codex 2026-08-31.
- **GitHub Copilot**: Grok 4.5 added 7/28; code-review agent-skills + MCP GA for all tiers 7/29; Gemini 2.5 Pro & Gemini 3 Flash deprecated across all Copilot surfaces 7/31 (this was previously flagged as scheduled for 7/31 — now confirmed shipped).
- **Cognition/Devin acquired Poke** (Interaction Co. of California) 2026-07-23 — messaging-agent personality layer, low-nine-figures deal.

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
- Fable 5.1 / Mythos 5.1 (2026-09-01): $10/$50 per M tokens, ~25% cheaper than Fable 5 for typical workloads, 75% cheaper cache reads.
- GPT-5.6: Sol $5/$30, Terra $2.50/$15, Luna $1/$6 per M tokens (in/out).
- GPT-6 Astra (2026-09-03): $10/$50 per M standard; >272K-input requests bill whole request at $20/$75; cached input 90% off ($1 in); Fast mode 2x price; batch/flex half-price ($5/$25).
- Grok 4.5 (SpaceXAI/Cursor): $2/$6 per M tokens.
- Claude Code weekly limits: 50% temporary increase ends 2026-09-13; permanent 25% increase (net lower than promo) starts 2026-09-14 for Pro/Max/Team/seat-based Enterprise.
