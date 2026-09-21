---
name: landscape-snapshot
description: Who's-ahead and model-landscape snapshot as of the last report (2026-09-21)
metadata:
  type: project
---

Snapshot as of 2026-09-21 (unchanged from 2026-09-17 except where noted — see coverage-log.md for what moved this cycle):

- General reasoning: Claude Fable 5.1 / GPT-6 Astra tied #1 on AA Intelligence Index v4.3 (53, rescaled). Claude Opus 5 close behind (51). Meta Muse Spark 1.3 at 48.
- Agentic/long-horizon: Claude leads on demonstrated long-horizon autonomy (11-day Lean FLT proof, prior cycle) AND now has the sharpest internal-automation data point (26% of Anthropic's own R&D led by Claude, up from <1% in Feb — NEW this cycle). DeepSeek V4.1 Flash is the low-cost agentic challenger (Automation-Bench 54.8, beats Opus 5).
- Coding: Claude Fable 5.1 (SWE-bench Pro 81.2%) / Opus 5 (SWE-bench Verified 96%) lead named flagships; DeepSeek V4.1 Flash (DeepSWE 74.2%) narrows the gap from open-weight side at ~20-50x lower cost.
- Multimodal: xAI Grok Voice Think Fast 2.0 leads voice; DeepSeek V4.1 Flash is the notable open-weight multimodal (image) entrant. xAI also shipped Grok Voice Transcribe 2.0 (transcription-specific, minor).
- Long context: Meta Muse Spark 1.3 / Kimi K3 (both 1M, Muse at 98.5% retrieval) lead; Gemini's rumored 2M remains unshipped.
- Cost-efficiency: DeepSeek V4.1 Flash ($0.15-0.30/M input, MIT license) sets the floor; caveat is verbosity (higher output-token counts).
- Open-weight: DeepSeek V4.1 Flash / Moonshot Kimi K3 (2.8T) lead; Tencent Hy4 Preview, Z.AI GLM-5.3, Qwen 3.8-Max are challengers.

Model landscape quick-reference (closed frontier): Anthropic (Fable 5.1/Mythos 5.1, Sept 1), OpenAI (GPT-6 Astra, Sept 3), Google (Gemini 3.5 Pro still unshipped — 4+ months overdue since May 19 tease; Gemini 3.8 Flash is the stopgap), xAI (Grok 4.6 shipped; 4.7/4.8/4.9 all unreleased, Grok 5 queued behind them), Meta (Muse Spark 1.3 / consumer "Muse" agent, closed API, now market-validated by JPMorgan Sept 19 upgrade).

Open-weight: DeepSeek (V4.1 Flash, Sept 10), Moonshot (Kimi K3, Jul 17 — reputationally dented by Anthropic's Sept 10 traffic-routing fraud accusation), Tencent (Hy4 Preview, Aug 28), Z.AI (GLM-5.3, Aug 14), Qwen/Alibaba (Qwen3.8 27B/Qwen 3.8-Max; Qwen 4.0 still rumor-only), Mistral (no new flagship for 6 consecutive cycles, but raised €3B from Samsung Sept 8 at €21B valuation — sovereign-AI infra play, not a model release), Thinking Machines (Inkling).

IMPORTANT CAVEAT: this snapshot reflects a budget-constrained cycle (2026-09-21) where the state-of-the-art doc's capability-frontiers, lab-strategy-watch, trend-tracker, and predictions sections were carried forward WITHOUT a full refresh (only overview + model landscape + changelog were updated). Verify against the live doc before treating those specific sections as current.
