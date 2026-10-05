---
name: landscape-snapshot
description: Who's-ahead and model-landscape snapshot as of the last report (2026-09-28)
metadata:
  type: project
---

Delta 2026-10-05: Agentic leader = OpenAI on productization (dots, Agents API computer use, Bedrock Managed Agents), Anthropic on demonstrated autonomy. Coding: Sonnet 5.5 (vendor-reported Opus-class at $2/$10) + GPT-6.1 Sol (~1/5 Astra price). AA top: GPT Sol 58.9, Opus 5.5 57.6, Sonnet 5.5 56.0, Terra 55.0 (tracker figures). Open-weight/Google/Mistral/xAI: no confirmed ships.

Snapshot as of 2026-09-28 (see coverage-log.md for what moved this cycle):

- General reasoning: GPT-6/5.6 Sol now #1 on AA Intelligence Index v4.3.2 (58.9%), Claude Opus 5.5 close #2 (57.6%), GPT-6 Terra #3 (55.0%) — displaced the prior Fable 5.1/Astra tie (53). NOTE: model-naming discrepancy unresolved (some trackers say "GPT-5.6 Sol" for the leader vs. OpenAI's own "GPT-6 Sol" launch) — verify against artificialanalysis.ai directly if precision matters.
- Agentic/long-horizon: Anthropic still leads on demonstrated internal automation (Claude leads 26% of Anthropic's own R&D, from 09-21 cycle). OpenAI's DevDay 2026 (Sept 29, unshipped as of this report) teases a persistent "o" agent + "managed agents" — could be the biggest capability-jump entry next cycle if it ships as described. Meta's Muse added Mac computer-use (Connect 2026, Sept 23).
- Coding: Claude Opus 5.5 / Fable 5.1 remain named-flagship leaders; two new cost-tier entrants narrowed the field — GPT-6 Sol (economical, coding-tuned) and Grok 4.7 (xAI's first ship in 3 cycles, longer RL run on hard/many-hour tasks). DeepSeek V4.1 Flash still the open-weight cost-efficiency leader.
- Multimodal: Qwen3.8-Omni-Flash (Sept 18) is the new high-water mark — text/image/audio/video in one open-weight model, 1M context. Grok 4.7 adds image input; Meta's "Muse Realtime Avatar" turns voice into video.
- Long context: Qwen3.8-Omni-Flash (1M) ties Meta Muse Spark 1.3 (1M, 98.5% retrieval) and Kimi K3 (1M). Grok 4.7 only 500K. Gemini's rumored 2M still unshipped.
- Cost-efficiency: Cost pressure hit the closed frontier this cycle for the first time in months — OpenAI GPT-6 Luna ($0.10/$0.50 per M) and Anthropic Opus 5.5 (40% cheaper than Opus 5) both shipped Sept 22 as explicit margin-defense moves. DeepSeek V4.1 Flash ($0.15-0.30/M, MIT) remains the open-weight floor.
- Open-weight: Scale-ambition ceiling jumped an order of magnitude on paper — DeepSeek teased 20T (then 80T, up from V4's 14T); Qwen's lead said Qwen 4.5/5 will target 5-10T. Nothing shipped yet at that scale. Actual open-weight ships this cycle were multimodal breadth (Qwen Omni-Flash, Moonshot Kimi K2.8 Preview vision).

Model landscape quick-reference (closed frontier): Anthropic (flagship Fable 5.1/Mythos 5.1 Sept 1, cost-tier Opus 5.5 Sept 22), OpenAI (flagship GPT-6 Astra Sept 3, cost-tier Sol/Luna Sept 22, DevDay Sept 29 pending), Google (Gemini 3.5 Pro still unshipped, 4+ months overdue), xAI (Grok 4.7 shipped Sept 21 ending backlog; 4.8/4.9/5 still unshipped), Meta (Muse/Muse Spark, closed API, 3.4M+ downloads, Connect 2026 feature expansion).

Open-weight: DeepSeek (V4.1 Flash shipped Sept 10; 20T/80T teased), Qwen/Alibaba (Omni-Flash + Image-2.1 shipped; Qwen 4 "very soon," 4.5/5 teased 5-10T), Moonshot (Kimi K2.8 Preview shipped Sept 11, Kimi K3 on Bedrock Sept 18), Tencent (Hy4 Preview, no update), Z.AI (GLM-5.3, no update), Mistral (no new model for 7 consecutive cycles; riding Sept 8 Samsung round/Microsoft tie-up), Thinking Machines (Inkling, no update).

Strategic overlay (the actual headline this cycle): Anthropic IPO slipped Oct→Nov with real friction (price war, rates, cybersecurity exposure); Dario Amodei's "We Must Pace the Frontier" essay (Sept 12, backfilled) calls for a 1-2yr industry capability slowdown; UN Security Council briefing (Sept 23) had Amodei+Altman warning of AI risk alongside a UN panel report on an OpenAI-Hugging Face agent-cheating incident. OpenAI's own IPO separately reported at risk of slipping to 2027.
