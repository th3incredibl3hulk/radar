---
name: landscape-snapshot
description: Model landscape and who's-ahead readings as of the 2026-09-17 report — update in place each cycle, don't append duplicates
metadata:
  type: project
---

## As of 2026-09-17 (delta from 2026-09-07, 10-day cycle)
- **No frontier lab shipped a new flagship this cycle.** Biggest capability story came from DeepSeek instead.
- **DeepSeek**: V4.1 Flash (Sept 10) — new asymmetric Causal Encoder-Decoder architecture family, 552B total/8B input-active/16B output-active, native multimodal input, MIT-licensed, beats Opus 5/GPT-5.6 Sol on several agentic benchmarks (DeepSWE 74.2%, Automation-Bench 54.8, CyberGym 88.1) at $0.15-0.30/M tokens (20-50x cheaper than a flagship call). Flagged as unusually verbose. AA Index open-weight #6 (40).
- **xAI**: Grok 4.7 shelved outright Sept 13 after a 5th missed date; Grok 4.8 (2.5T, new C++ stack) announced instead with no ship date/spec/price for either. Production remains Grok 4.6.
- **Anthropic**: No new model. IPO story firmed from investor rumor to company-sourced substance — Nasdaq confirmed, "second profitable quarter" claim on $65B ARR (July), immediate pushback on adjusted-profitability framing. Also accused Moonshot AI (Sept 10) of secretly routing ~300K Kimi requests to Claude and reselling answers as Kimi's own — a fraud allegation, not just distillation.
- **OpenAI**: No new model. Astra system card updated Sept 9, narrowing (not resolving) the CoT-monitorability disclosure. Began testing ChatGPT advertising ("sponsored agents," Sept 16) — new monetization lever. Sora API shuts down Sept 24.
- **Google**: Gemini 3.5 Pro still unshipped (4+ months past May 19 tease), but caught being silently A/B tested inside Antigravity under a fake "Gemini 3.1 Pro" label.
- **AA Intelligence Index**: bumped to v4.3 on Sept 7 (3 days after v4.2) — Terminal-Bench→4.0, AutomationBench-AA replaces τ³-Banking. Claude Fable 5.1 and GPT-6 Astra now TIED #1 at 53 (rescaled — not comparable to pre-v4.2 numbers). Opus 5 at 51. GLM-5.3 top open-weight at 45 (80/161 ranked models are open-weight).
- **Tencent** (newly tracked, backfilled): Hy4 Preview (Aug 28) — 770B/49B-active MoE, Apache 2.0, notable for self-optimizing its own training/inference (31.8% throughput gain).
- **Confirmed quiet via direct sweep**: Meta (Muse Spark 1.3 unchanged since Sept 2), Mistral (5th cycle, no frontier flagship, only OCR 4.1/Agentic Search product news), Qwen (Qwen 4.0 still rumor-only, Qwen 3.8-Max Aug 3 remains flagship).
- **Macro**: UBS now projects $4.1T combined hyperscaler AI infrastructure spend 2026-2028 (~3x the prior six years). S&P Global's $1.3T-in-2027 / 5-of-6-hyperscalers-FCF-negative figure unchanged.

## As of 2026-09-07 (delta from 2026-09-05)
- **Anthropic**: Claude autonomously formalized Fermat's Last Theorem in Lean (11 days, ~13M lines, via Prove2Me). Investors reportedly targeting $2T October IPO — unconfirmed by execs at the time (now substantiated, see above).
- **Google**: CORRECTION — shipped Gemini 3.8 Flash + 3.8 Flash Cyber on Sept 2 (missed in the 2026-09-05 report). Third consecutive Flash-tier stopgap.
- **OpenAI**: Astra's CoT-monitorability disclosure escalated in press scrutiny (4 days post-launch).
- **xAI**: Grok 4.7 hit a 5th informal date (~Sept 11-12).
- **Macro**: Hyperscaler capex outrunning free cash flow — 5 of 6 majors projected negative FCF through 2027, $1.3T combined capex.
- **New signal**: Aurora ransomware group used Cursor's coding agent (on Claude Sonnet) for hands-on exploitation of 10 targets.

## AA Intelligence Index — current top of leaderboard (v4.3, as of 2026-09-07, confirmed 2026-09-17)
1. Claude Fable 5.1 — 53 (tied)
1. GPT-6 Astra — 53 (tied)
3. Claude Opus 5 — 51
Top open-weight: GLM-5.3 — 45
(Note: v4.3 rescaled the index — these numbers are NOT comparable to pre-v4.2 scores like the old "65.7" for Fable 5.1. Always cite the index version alongside any score.)

## Who's-ahead table (updated 2026-09-17)
| Capability | Leader(s) | Challengers |
|---|---|---|
| General reasoning | Claude Fable 5.1 / GPT-6 Astra (tied, AA v4.3: 53) | Claude Opus 5 (51) |
| Agentic/long-horizon | Claude (Prove2Me/Lean 11-day autonomous run, prior cycle — no new demo this cycle) | GPT-6 Astra, Meta Muse Spark 1.3, DeepSeek V4.1 Flash (Automation-Bench 54.8) |
| Coding | Claude Fable 5.1 (SWE-bench Pro 81.2%) / Opus 5 (SWE-bench Verified 96%) | DeepSeek V4.1 Flash (DeepSWE 74.2%, beats Opus 5), Meta Muse Spark 1.3, GLM-5.3 |
| Multimodal | xAI Grok Voice Think Fast 2.0 | DeepSeek V4.1 Flash (new native multimodal input), Google Gemini 3.8 Flash |
| Long context | Meta Muse Spark 1.3 (1M, 98.5% retrieval) / Kimi K3 (1M) | DeepSeek V4.1 Flash (1M), Gemini 3.5 Pro (rumored 2M, unshipped) |
| Cost-efficiency | DeepSeek V4.1 Flash ($0.15-0.30/M, MIT license) | Google Gemini 3.8 Flash, Z.AI GLM-5.3 |
| Open-weight | DeepSeek V4.1 Flash / Moonshot Kimi K3 (2.8T) | Tencent Hy4 Preview (770B, Apache 2.0), Z.AI GLM-5.3, Qwen 3.8-Max |

## Trend tracker last reading (2026-09-17)
Reasoning 4 (↓ no new flagship shipped), Agents 4 (↓ no new long-horizon demo to match last cycle's FLT proof), Coding 5 (flat), Multimodal 3 (flat), Long context 4 (flat), Cost collapse 5 (⇑ DeepSeek V4.1 Flash resets the floor), Open-weight catch-up 5 (flat — new entrants but still short of AA top 5), Chinese labs 5 (↑ DeepSeek architecture shift + Tencent self-optimizing model + Moonshot dispute all China-adjacent), Gov't/regulatory involvement 4 (↓ Astra monitorability narrowed rather than escalated), Infra/compute consolidation 4 (flat — UBS $4.1T/2026-28 reconfirms trajectory, no new mega-deal).

## Prior snapshots (superseded, kept for delta reference — see full history in git log of this file if needed)
As of 2026-08-17: OpenAI Astra pause operationalized; Gemini 3.5 Pro missed 4th date; Grok 4.6 AA #3 (60.9); Fable 5 AA #2 (62.1); DeepSeek V4-Pro GA then 14x peak-hour hike; Stripe-OpenRouter $7B+ acquisition; hyperscaler capex ~$775-800B/2026.
