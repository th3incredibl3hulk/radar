---
name: benchmarks
description: Benchmark leaderboard snapshots by date, for tracking movement cycle over cycle.
metadata:
  type: reference
---

## Terminal-Bench 2.1 (snapshot 2026-07-17, per CodingFleet)
1. GPT-5.6 Sol — 88.8% (91.9% for "Ultra" variant)
2. Kimi K3 (Moonshot AI, open-weight) — 88.3% (new entrant, within 0.5pt of leader)
3. "Terra" — 87.4%
4. "Luna" — 84.7%
- Note: GPT-5.3 Codex (older, terminal-specialized) — 77.3%, still beats general-purpose GPT-5.4 on this specific benchmark. Recurring theme: task-specialized fine-tuning > raw model generation for narrow CLI/terminal tasks.
- Kimi K3 also leads SWE Marathon and Program Bench outright, and tops Arena.AI's Frontend Code Arena ahead of Fable 5 and GPT-5.6 Sol.

## SWE-bench Pro — CREDIBILITY WARNING (as of 2026-07-20)
OpenAI audited SWE-Bench Pro and found ~27.4-34.1% of its 731 public tasks broken (mostly overly-strict tests failing correct code); OpenAI retracted its recommendation to use it. **Do not cite SWE-Bench Pro leaderboard positions as reliable capability signal until a cleaned re-run is published.** Last pre-audit reading (2026-07-16, cross-checked llm-stats.com/benchlm.ai): Claude Mythos 5 — 80.3%, Claude Fable 5 — 80.0%, Sakana Fugu-Ultra — 73.7%. Note Mythos 5 is a confirmed restricted-access product (named June 9), not an unannounced preview.

## Sources for benchmark tracking
- swebench.com (SWE-bench Leaderboards, official)
- swe-bench-live.github.io (SWE-bench-Live)
- swe-rebench.com (SWE-rebench)
- codingfleet.com/blog (Terminal-Bench, SWE-bench Pro secondary aggregation — useful but verify against primary sources)
- morphllm.com/swe-bench-pro (secondary aggregator, single-source risk)
- openai.com/index (primary source for the SWE-Bench Pro credibility audit — check OpenAI's own blog for benchmark-methodology posts going forward, they've now done this twice in 2026)
