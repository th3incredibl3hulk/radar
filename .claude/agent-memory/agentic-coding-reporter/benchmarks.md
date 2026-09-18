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

## 2026-08-24 cycle — SWE-bench Verified snapshot (as of 2026-08-22, via BenchLM)
1. Claude Opus 5 — 96.0%
2. Claude Mythos 5 — 95.5%
3. Claude Fable 5 — 95.0%
- Top three now within 1 point. Note: Opus 5's reading dipped from 97.00% (2026-08-14 snapshot) to 96.0% — most likely leaderboard re-scoring/methodology noise, not a real regression; flag rather than silently treat as a trend. Benchmark is now a pass/fail bar at the frontier, low differentiation value.
- SWE-bench Pro: still no cleaned re-run from OpenAI. No new leaderboard movement checked this cycle beyond what's in the 2026-08-17 entry below.

## 2026-08-17 cycle — SWE-bench Verified snapshot (as of 2026-08-14, via BenchLM)
1. Claude Opus 5 — 97.00%
2. DeepSeek V4 Pro 0813 — 96.40%
3-5. (three more models also >95%, not individually named in source)
6. Kimi K3 — 93.40%
- Claude Opus 4.8 — 88.60%; Grok 4.5 — 86.60%.
- Reading: 5-of-83 evaluated models now clear 95% — this benchmark (introduced to replace the saturated original SWE-bench Verified) is itself now showing saturation at the top. Treat top-of-leaderboard SWE-bench Verified scores as compressed/low-differentiation going forward.
- SWE-bench Pro still uncleaned post-OpenAI-retraction; Claude Mythos 5/Fable 5 still cited leading at 80.3% by third-party trackers, Qwen3.8 Max newly reported at 67.7% (strongest new non-Anthropic Pro entry since Opus 5, but same credibility caveat applies).

## 2026-08-03 cycle
No new benchmark leaderboard movement found this cycle (budget-constrained run, did not deep-check). SWE-Bench Pro credibility warning stands unchanged — no cleaned re-run published yet by OpenAI as of 2026-08-03. Terminal-Bench 2.1 standings from 2026-07-17 unchanged. Check swebench.com/swe-bench-live.github.io directly next cycle.

## 2026-09-05 cycle
- **SWE-bench Pro**: Claude Fable 5.1 new #1 at 81.2% (per CodingFleet, 2026-09-01), also 52.6% on Terminal-Bench-Science. First movement since OpenAI's credibility audit — still no cleaned re-run from OpenAI itself, treat cross-vendor comparisons cautiously.
- **SWE-bench Verified**: unchanged from 2026-08-22 (Opus 5 96.0%, Mythos 5 95.5%, Fable 5 95.0%).
- **New benchmark: FrontierHarness Eval** (frontierharness.org) — first standardized cross-harness comparison, holding model constant and varying only the harness (Claude Code, Codex, DeepSeek Harness, Exo Harness, Hermes, Kimi Code, Oh My Pi, OpenCode, Pi). 30 tasks (21 Terminal-Bench + 9 DeepSWE), 360 runs, ~2B tokens. Pass rates 50-67%, cost-per-pass $1.05-$18.34 — harness choice alone swung cost up to 26x for the same fix (Pi $2.50/90 turns vs Claude Code $64.36/381 turns, cited example). Worth tracking each cycle as it matures — first real empirical data on "harness engineering" (Lilian Weng's July thesis).

## Sources for benchmark tracking
- swebench.com (SWE-bench Leaderboards, official)
- swe-bench-live.github.io (SWE-bench-Live)
- swe-rebench.com (SWE-rebench)
- codingfleet.com/blog (Terminal-Bench, SWE-bench Pro secondary aggregation — useful but verify against primary sources)
- morphllm.com/swe-bench-pro (secondary aggregator, single-source risk)
- openai.com/index (primary source for the SWE-Bench Pro credibility audit — check OpenAI's own blog for benchmark-methodology posts going forward, they've now done this twice in 2026)
