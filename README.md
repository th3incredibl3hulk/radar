# Radar — Personal AI Intelligence Agents

A small fleet of Claude Code subagents that scan the web on a schedule, write signal-dense Markdown briefings, and maintain living "state-of-the-art" documents — so a busy platform leader stays ahead of AI without reading X all day.

Built on the [ai-news-discovery](https://github.com/collibra/ai-news-discovery) pattern, trimmed and retargeted for a VP of Platform: technical-heavy, business-aware, Markdown output.

## The core idea

**The agent is your reader.** You don't need an X account or a mental list of blogs — you hand each agent a curated, tiered source list and it does the reading. Sources are tiered on purpose:

- **Newsletter tier** — curated digests that already scrape X / Discord / Reddit for you (AInews/smol.ai, Import AI, Interconnects, SemiAnalysis, Stratechery…). This is how you get the leading edge without an X account.
- **Primary tier** — company and lab blogs, official release notes. The source of record.
- **Filter tier** — Hacker News, Reddit, Lobsters. Used to confirm what *broke through* to the mainstream, **not** as the leading edge. They lag and skew to dev tooling.

Each run produces a dated **delta report** (what's new since last time) and refreshes a **state-of-the-art** doc (your standing briefing). Persistent per-agent memory prevents duplicate coverage.

## Agents

| Agent | File | Focus |
|-------|------|-------|
| **Frontier Watch** | `agents/frontier-watch-reporter.md` | Model releases, capability jumps, who's ahead, lab strategy — trends & company blogs, not papers |
| **Agentic Coding** | `agents/agentic-coding-reporter.md` | AI coding tools/agents + the MCP tool-use ecosystem |
| **Production AI Eng** | `agents/production-ai-eng-reporter.md` | Evals, guardrails, observability, reliability, cost — shipping AI safely |
| **AI Economics** | `agents/ai-economics-reporter.md` | Labor, productivity, investment, contrarian tracking (source-tiered) |

`agents/templates/news-reporter.md` defines the shared Markdown format, quality bar, and workflow. Each agent inherits it and adds its own sources, tags, and state-of-the-art structure.

### The skeptic (on-demand, not scheduled)

| Agent | File | Focus |
|-------|------|-------|
| **Skeptic** | `agents/skeptic.md` | Skeptically audits whether Radar is still reading the right sources — reviews the last report or two, pressure-tests each source list, and proposes *at most a few* high-bar changes. Recommends only; never edits the reporters. |

Fire it when you want to question the mix (`claude --agent skeptic -p "Audit my sources. Today is <date>."`). It's deliberately quiet — "no change needed" is a normal, good result — and it runs on Opus because the whole value is discernment. It writes to `reports/source-audits/` and is intentionally kept **out of the weekly cron**, since it's a judgment call you invoke, not a feed.

## Setup

Copy the agents into your project's `.claude/agents/` directory:

```bash
mkdir -p .claude/agents/templates
cp agents/*.md .claude/agents/
cp agents/templates/news-reporter.md .claude/agents/templates/
```

Reports are written under `reports/<domain>/`. Grant write permissions in `.claude/settings.local.json`.

## Running

### Interactively (inside Claude Code)

```
claude --agent frontier-watch-reporter -p "Generate today's report. Today is 2026-07-10."
```

Or invoke as a subagent from a session — each agent's description includes trigger phrases.

### Scheduled (weekly, via launchd)

`scripts/run-all.sh` runs all four reporters **sequentially** and regenerates `reports/weekly-digest.md` (a single index linking every report). The skeptic is intentionally excluded — it's on-demand.

Install the weekly LaunchAgent (Mondays 07:00 local):

```bash
./scripts/install-launchd.sh          # generates ~/Library/LaunchAgents/com.larryhau.radar.weekly.plist and loads it
launchctl kickstart -k gui/$(id -u)/com.larryhau.radar.weekly   # optional: run it once now to test
./scripts/uninstall-launchd.sh        # remove it
```

The installer resolves its own absolute path, so **after you move `radar/` into your own repo, just re-run `install-launchd.sh` from the new location** — it regenerates the plist and reloads.

Notes:
- It runs as your GUI user, so it inherits your Claude Code subscription login. On **API billing**, add `ANTHROPIC_API_KEY` to the `EnvironmentVariables` block in `install-launchd.sh`.
- launchd won't fire while the Mac is asleep, but a **missed weekly run executes on the next wake** — so a closed laptop delays, rather than skips, the digest.
- Logs go to `scripts/run.log`.

Typical cost: ~$0.30–0.80 per agent per run (Sonnet).

## Reading it

Start at `reports/weekly-digest.md` on Monday. Drill into a domain's dated report for detail, or read its `*-state-of-the-art.md` before a meeting where you need the standing picture.

## Extending

Adding a domain is one agent file + one `reports/<domain>/` dir + a line in `run-all.sh`. Two obvious future adds for a Collibra platform leader, deliberately deferred:

- **AI Governance & Regulation** — EU AI Act, NIST AI RMF, model governance, data provenance/lineage.
- **Data Intelligence Competitive Landscape** — Databricks, Snowflake, Purview, Alation, Atlan, Informatica, dbt.

## Customize before relying on it

1. **Paths** — agents write to `reports/<domain>/` and remember in `.claude/agent-memory/<agent>/`. Adjust to your layout.
2. **Sources** — prune or add to each agent's tiered list as your interests sharpen.
3. **Cadence** — weekly by default; 2-week rolling window. Change in the agents and cron.
4. **Model** — Sonnet is the cost/quality sweet spot; bump to Opus for deeper synthesis.
