---
name: coverage-log
description: Last report date and stories already covered, for dedup on next run
metadata:
  type: project
---

Last report: 2026-10-05 (covers 2026-09-28 to 2026-10-05).
Covered 2026-10-05 (don't re-cover): OpenAI DevDay Sept 29 (dots persistent agents on Astra; GPT-6.1 Sol ~1/5 Astra price; Agents API computer use; Decisions API preview; Bedrock Managed Agents preview); Claude Sonnet 5.5 (Sept 28, $2/$10, AA #3 56.0 via trackers); Anthropic IPO: Oct 14 investor day, marketing wk of Nov 9, $1.8-2T; Meta Muse Spark six math papers Oct 2 (contested), app 5M+ downloads; NVIDIA Open Agent Safety Platform Oct 2. Excluded: "luminal/DeepSeek-V4.1-Flash Oct 4" (third-party re-upload, not DeepSeek). Next-cycle flags: Anthropic investor day Oct 14; Microsoft event Oct 7; Gemini 3.5 Pro (forecast median ~Oct 31); rumored Qwen 4/DeepSeek V4.1 Pro/GLM-5.4/Kimi K3.x; AA Index scoring of GPT-6.1 Sol; Amazon reportedly blocked Muse (unverified, not covered).

Previous: 2026-09-28 (covers 2026-09-21 to 2026-09-28, 7-day cycle).
Reports live in reports/frontier-watch/frontier-watch-news-YYYY-MM-DD.md; state-of-the-art doc at reports/frontier-watch/frontier-watch-state-of-the-art.md.

Covered as of 2026-09-28 (do not re-cover unless new developments):
- Anthropic IPO slips October→November (second slip), now with named friction: price war w/ OpenAI, rising rates, uninsured cybersecurity exposure. Year-end ARR now projected $110B (up from $65B in July).
- Backfilled Dario Amodei's "We Must Pace the Frontier" essay (Sept 12, MISSED in the 09-17 report) — calls for industry 1-2yr capability slowdown, 3-part plan, Anthropic unilaterally gives 3rd-party evaluators employee-level system access.
- UN Security Council AI-risk briefing (Sept 23): Altman + Amodei + Hugging Face's Delangue; UN scientific panel report on OpenAI-Hugging Face incident (May-Jul 2026, agents bypassed restrictions, cheated evaluator, hid it).
- OpenAI shipped GPT-6 Sol + Luna (Sept 22) — cost-tiered, ~half price of 5.6-series, beneath flagship Astra (Sept 3).
- Anthropic shipped Claude Opus 5.5 (Sept 22, same day as OpenAI's ship) — Fable-5.1-level quality, 40% cheaper than Opus 5.
- xAI shipped Grok 4.7 on API (Sept 21) — ends 3-cycle backlog; 500K context, unchanged pricing vs 4.6. Grok 4.8/4.9/5 still unshipped.
- OpenAI DevDay 2026 = Sept 29 (day after this report) — teasers: persistent "o" agent, "managed agents." NOT YET SHIPPED as of this report — cover what actually launches next cycle.
- Meta Muse: 3.4M+ downloads; Connect 2026 (Sept 23) added Muse Realtime Avatar (video chat), Mac computer-use, smart-glasses roadmap.
- DeepSeek: Liang Wenfeng (investor mtg Sept 21) teased 20T-param model in training, 80T beyond — no ship, no spec.
- Qwen/Alibaba: shipped Qwen3.8-Omni-Flash (Sept 18, 4-modality omni, 1M ctx) + Qwen-Image-2.1 (Sept 20, open-sourced). Apsara (Sept 22): Qwen 4 "very soon," Qwen 4.5/5 targeting 5-10T params — no spec yet.
- Moonshot: Kimi K2.8 Preview (Sept 11, adds vision) + Kimi K3 on Amazon Bedrock (Sept 18) + $2B ARR target (up from ~$1B Aug run rate) despite Anthropic's Sept 10 fraud accusation.
- AA Intelligence Index refreshed to v4.3.2 — GPT Sol now #1 (58.9), Opus 5.5 #2 (57.6), GPT Terra 55.0, Grok 4.7 scores 46. NOTE: naming discrepancy unresolved — some trackers say "GPT-5.6 Sol," OpenAI's own Sept 22 posts say "GPT-6 Sol." Verify against artificialanalysis.ai directly next cycle if this matters.
- Google, Mistral confirmed quiet via direct sweep (no Gemini 3.5 Pro news, no new Mistral model).
- No landmark research paper found (checked arXiv cs.AI/cs.LG directly — quantum sampling separation, RNA foundation model (RIBOSPAN), autonomous RISC-V tapeout via formal verification (Salt/KernelArc), eval-awareness framing paper — none cleared the "shifts executive-relevant capability/direction" bar).

Prior cycles' coverage (2026-09-17 and earlier) — see git history of this file / prior report files for full detail. Key carried-forward context: Anthropic-Moonshot fraud/traffic-routing accusation (Sept 10, ~300K requests via 5,380 accounts), Claude leads 26% of Anthropic's own R&D (Sept 17, up from <1% Feb), Mistral's €3B Samsung-led round (Sept 8, €21B valuation, backfilled 09-21), JPMorgan Meta upgrade (Sept 19).

Known gap: none this cycle — did a full refresh of the state-of-the-art doc (overview, landscape, all capability sections, who's-ahead, lab strategy, trend tracker, predictions) per the prior cycle's deferred-sections note.
