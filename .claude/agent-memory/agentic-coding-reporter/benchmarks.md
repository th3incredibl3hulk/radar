---
name: benchmarks
description: Benchmark leaderboard snapshots by date, for tracking movement cycle over cycle.
metadata:
  type: reference
---

## Terminal-Bench 2.1 (snapshot 2026-07-10)
1. GPT-5.6 Sol — 88.8% (91.9% for "Ultra" variant)
2. "Terra" — 87.4%
3. "Luna" — 84.7%
- Note: GPT-5.3 Codex (older, terminal-specialized) — 77.3%, still beats general-purpose GPT-5.4 on this specific benchmark. Recurring theme: task-specialized fine-tuning > raw model generation for narrow CLI/terminal tasks.

## SWE-bench Pro (snapshot ~2026-07, per MorphLLM tracker — cross-check independently before citing, single-source)
- Claude Opus 4.8 cited as leading "active" model at 69.2%.

## Sources for benchmark tracking
- swebench.com (SWE-bench Leaderboards, official)
- swe-bench-live.github.io (SWE-bench-Live)
- swe-rebench.com (SWE-rebench)
- codingfleet.com/blog (Terminal-Bench, SWE-bench Pro secondary aggregation — useful but verify against primary sources)
- morphllm.com/swe-bench-pro (secondary aggregator, single-source risk)
