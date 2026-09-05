---
title: Frontier Watch — State of the Art
date: 2026-09-05
author: Frontier Watch Reporter Agent
tags: [frontier, models, capabilities, summary]
---

# Frontier Watch — State of the Art

## Overview

The Astra saga resolved with a launch, not a further delay: OpenAI shipped GPT-6 Astra on September 3, the first model to formally cross its own "Critical" cybersecurity threshold, saturating narrow benchmarks (100% ExploitBench, 99.9% ARC-AGI-3, 98% FrontierMath Tier 4) while landing only #5 on the Artificial Analysis Intelligence Index and disclosing a "substantial decrease" in chain-of-thought monitorability versus its predecessor. Anthropic beat it to market by two days with Claude Fable 5.1 and Mythos 5.1 (Sept 1) — a same-price maintenance-style release that more than doubled agentic-science and knowledge-work scores and retook AA Index #1 at 65.7. The real surprise of the cycle is Meta: Muse Spark 1.3 (Sept 2) cracked the AA Index top 3 for the first time via training-loop efficiency rather than scale, re-entering the closed frontier conversation after months of silence and attrition headlines — while notably choosing API-gated closed distribution, not open weights, and monetizing a steep discount tier in exchange for training-data rights.

Everywhere else, "still unresolved" keeps compounding. Gemini 3.5 Pro has missed enough dates that Google has stopped naming new ones. Grok 4.7 is Musk's fourth "coming soon" in six weeks with zero published specs. Mistral's teased frontier flagship enters a fourth reporting cycle with nothing but a safety-classifier release (Shieldstral) to show. Meanwhile two open-weight Chinese labs — Moonshot (Kimi K3) and Z.AI (GLM-5.3, a post-training-only jump on an unchanged base) — now sit inside the AA Index top 8, edging toward (but still short of) the standing "open-weight cracks top 5" prediction. Hyperscaler capex estimates from J.P. Morgan, Goldman, and SemiAnalysis have converged into a tight $660-800B/year band for 2026 — multiple independent methodologies now agree, which is itself a signal that the buildout has no near-term brake.

## Model Landscape

### Frontier (closed) — Anthropic, OpenAI, Google, xAI, Meta
- **Anthropic**: Claude Fable 5.1 and Mythos 5.1 (new, Sept 1) — same price as predecessors ($10/$50, $60/$300-ish Mythos tier), cache reads cut 75%, retook AA Index #1 at 65.7. Claude Opus 5 ($5/$25, best coding/agentic value, AA Index #2 at 63.0), Claude Fable 5 (now #4 on AA Index at 62.1, superseded but still deployed), Claude Sonnet 5 (default Free/Pro), Claude Haiku 4.5 ($1/$5).
- **OpenAI**: GPT-6 Astra (new, Sept 3) — $10/$50 (2.5x GPT-5.6 Sol), first model to cross OpenAI's "Critical" cybersecurity threshold, saturates ExploitBench/ARC-AGI-3/FrontierMath Tier 4, but only AA Index #5 (61.2) and SWE-bench ~73-74% (unremarkable vs. peers). Ships with disclosed drop in chain-of-thought monitorability — an active safety controversy. GPT-5.6 family (Sol/Terra/Luna) continues underneath as the prior generation. Revenue run-rate >$40B as of mid-August.
- **Google DeepMind**: Gemini 3.5 Pro still unshipped — has missed enough informal dates that Google no longer names a new one, only "coming soon." Now a 4+ month delay against the original May 19 tease.
- **xAI / SpaceXAI**: Grok 4.6 (1.5T, AA Index #6 at 60.9) unchanged. Grok 4.7 (2.1T, teased) slipped again — Musk's Sept 2 "10 days" claim is the fourth informal date in six weeks, still zero published specs.
- **Meta (re-entered this tier this cycle)**: Muse Spark 1.3 (new, Sept 2, via Meta Model API / Muse Code — closed distribution, not open weights) — cracked AA Index #3 at 62 via training-loop efficiency (20% fewer tool calls, 25% fewer tokens vs. 1.2), not parameter scale. Standard pricing $1.25/$4.25; a "contributor" tier at ~$0.10/$0.20 trades a 10-20x discount for training-data rights on your traffic.

### Open-weight — Mistral, DeepSeek, Qwen, Moonshot, Z.AI, Thinking Machines
- **Moonshot AI**: Kimi K3 — 2.8T parameters, 1M context, native vision, free public weights. Still the largest open-weight model available; now AA Index #7 (59.7).
- **Z.AI**: GLM-5.3 (Aug 14) — post-training-only jump on the unchanged GLM-5.2 base (320B total/18B active MoE); lifted Terminal-Bench 3.0 from 4.6% to 28.3% and reached 84.5% on CyberGym (vendor-reported, not independently verified). Now inside the AA Index top 8.
- **Qwen (Alibaba)**: Qwen 3.8-Max (2.4T total/95B active MoE, $2/$6) remains Alibaba's current flagship and open-weight cost-efficiency leader. Qwen 4.0 still rumor-only; a July leak claims September, unconfirmed by Alibaba.
- **Thinking Machines Lab**: Inkling — 975B total/41B active MoE, Apache 2.0. Mira Murati's first shipped model; no update this cycle.
- **DeepSeek**: V4-Pro/V4-Flash unchanged this cycle (last move was the Aug 16 peak-pricing hike, now out of window).
- **Mistral**: Fourth consecutive cycle with no frontier-flagship clarification. Only Aug news: Shieldstral (Aug 4), a safety-classifier model. The "fat but sparse" MoE tease remains unresolved vs. the already-shipped Mistral Large 3 (Dec 2025).

### Specialized / small / edge
- MiniMax H3 (omni-modal open-weight, video+audio), Cohere North/Command line + Parse 5 document intelligence (sovereign, enterprise-deployable), Amazon Nova 2 Sonic/Lite/Forge/Act (kept active while Premier/Omni/Reel/Canvas move to maintenance-only).

## Capability Frontiers (executive view)

### Reasoning & Test-Time Compute
Claude Fable 5.1 retook outright AA Index #1 (65.7) this cycle, ahead of Opus 5 (63.0) and new entrant Meta Muse Spark 1.3 (62.1). GPT-6 Astra saturates narrow benchmarks but sits #5 on the aggregate index (61.2) — a widening gap between "best on the benchmarks a lab headlines" and "best on aggregate." Reasoning-effort dials remain standard product surface across all labs.

### Agents & Long-Horizon Tasks
Claude Fable 5.1's Terminal-Bench-Science jump (24.7% → 52.6%) and Meta Muse Spark 1.3's DeepSWE score (75.4%, fewer tool calls/tokens per task) are this cycle's agentic headlines. GPT-6 Astra claims state-of-the-art computer/browser use but hasn't published a comparable agentic aggregate. No long-horizon demo news from Google, xAI, or Qwen this cycle.

### Coding
Claude Fable 5.1 and Opus 5 remain ahead of GPT-6 Astra on SWE-bench (Astra ~73-74%, matched or beaten by same-generation peers) despite Astra's narrow-benchmark dominance elsewhere — a clean example of benchmark divergence. Meta Muse Spark 1.3 and Z.AI's GLM-5.3 (post-training-only jump, Terminal-Bench 3.0 4.6%→28.3%) are the fastest-moving challengers.

### Multimodal (vision, voice, video)
Quiet cycle. xAI's Grok Voice Think Fast 2.0 remains the voice leader; Meta Muse Spark 1.3's 98.5% long-context retrieval is the closest thing to multimodal/long-context news. Kimi K3 still holds native vision at open-weight 2.8T scale. Gemini's multimodal upgrades stay unconfirmed pending 3.5 Pro or Gemini 4.

### Long Context & Memory
Meta Muse Spark 1.3 (1M window, 98.5% retrieval) and Kimi K3 (1M) lead; DeepSeek V4-Pro also at 1M. Gemini's rumored 2M window remains unshipped. No landmark long-context research surfaced this cycle.

### Cost & Efficiency
Z.AI's GLM-5.3 is the sharpest efficiency story — a large capability jump from post-training alone on an unchanged, cheap (320B/18B active) base, no retrain required. Meta's "contributor" pricing tier (10-20x discount for training-data rights) is a new and worth-watching monetization pattern layered on top of a raw price cut.

## Who's Ahead (rolling)

| Capability | Leader(s) | Challengers | Last Changed |
|------------|-----------|-------------|---------------|
| General reasoning | Claude Fable 5.1 (AA Index 65.7) | Claude Opus 5 (63.0), Meta Muse Spark 1.3 (62.1) | 2026-09-05 — Fable 5.1 retook #1; Meta cracked top 3 |
| Agentic / long-horizon | Claude Fable 5.1 (Terminal-Bench-Science 52.6%) | GPT-6 Astra, Meta Muse Spark 1.3 (DeepSWE 75.4%) | 2026-09-05 |
| Coding | Claude Fable 5.1 / Opus 5 (ahead of Astra on SWE-bench) | Meta Muse Spark 1.3, GLM-5.3 | 2026-09-05 |
| Multimodal | xAI Grok Voice Think Fast 2.0 (voice) | Meta Muse Spark 1.3 (long-context retrieval), Qwen Image 3.0 Pro | 2026-08-10 |
| Long context | Meta Muse Spark 1.3 (1M, 98.5% retrieval) / Kimi K3 (1M) | DeepSeek V4-Pro (1M), Gemini 3.5 Pro (rumored 2M, still unshipped) | 2026-09-05 |
| Cost-efficiency | Z.AI GLM-5.3 (post-training-only gains, 320B/18B active) | Meta contributor tier, Qwen 3.8-Max | 2026-09-05 — GLM-5.3 new entrant |
| Open-weight | Moonshot Kimi K3 (2.8T, largest ever) | Z.AI GLM-5.3 (strengthened), Qwen 3.8-Max, DeepSeek V4-Pro | 2026-09-05 |

## Lab Strategy Watch

### Anthropic
Now visibly racing OpenAI's release calendar, not just its benchmarks — Fable 5.1/Mythos 5.1 shipped two days ahead of GPT-6 Astra at unchanged pricing, delivering a maintenance-release-sized price tag with a large agentic/knowledge-work capability jump. Continues segmenting aggressively by willingness to pay (Opus 5 as value play, Fable 5.1 as premium) while diversifying compute supply.

### OpenAI
Astra shipped Sept 3 as the concrete deliverable of the pause tracked since Aug 7 — first model to formally cross the "Critical" cybersecurity threshold, staged Daybreak access, and a self-disclosed drop in chain-of-thought monitorability that's now an active industry safety debate. Notably, narrow-benchmark dominance did not translate into aggregate AA Index leadership (#5) — a strategy of headlining hard, spiky benchmarks while trailing on general aggregate score.

### Google DeepMind
Gemini 3.5 Pro has now missed enough dates that Google has stopped naming new ones — a step back from even the "coming soon" framing of prior cycles. No new explanation offered this cycle beyond the standing Bloomberg report of a base-model rebuild.

### Meta
Re-entered the closed frontier conversation this cycle after months of silence — Muse Spark 1.3 cracked AA Index top 3 via training-loop efficiency, not scale, while choosing gated API distribution over open weights and monetizing a discount tier against training-data rights. A genuine strategy pivot worth tracking: efficiency-driven closed competition, not the open-weight giveaway path Llama once represented.

### The open-weight & Chinese labs
Z.AI's GLM-5.3 (post-training-only jump on an unchanged base) and Moonshot's Kimi K3 now both sit inside the AA Index top 8 — real progress toward, but still short of, cracking the top 5. Qwen 4.0 and Mistral's frontier flagship both remain unresolved rumors for a second and fourth cycle respectively.

## Trend Tracker

Intensity 0 (quiet) → 5 (on fire).

| Trend                     | 2mo ago | 1mo ago | Last | Now | Direction |
|---------------------------|---------|---------|------|-----|-----------|
| Reasoning models          | 5       | 5       | 5    | 5   | → |
| Autonomous agents         | 5       | 5       | 5    | 5   | → |
| Coding capability         | 5       | 5       | 5    | 5   | → |
| Multimodal (voice/video)  | 3       | 4       | 3    | 2   | ↓ (quiet cycle) |
| Long context              | 4       | 4       | 4    | 4   | → |
| Cost collapse             | 4       | 5       | 4    | 4   | → (GLM-5.3's post-training-only gains keep pressure on) |
| Open-weight catch-up      | 5       | 5       | 5    | 5   | → (GLM-5.3/Kimi K3 climbing AA Index, still short of top 5) |
| Chinese labs              | 4       | 4       | 4    | 4   | → |
| Gov't/regulatory involvement in releases | 3 | 5 | 5 | 5 | → (Astra shipped with the gate as a disclosed, permanent feature) |
| Infra/compute consolidation | — | 3 | 5 | 4 | ↓ (no new deal this cycle, but capex estimates converged across analysts) |

Directions: ↑ rising, → flat, ↓ cooling, ⇑ surging, ↗ emerging

## What This Means for Platform Leaders

- **Benchmark headlines and aggregate leadership are diverging.** GPT-6 Astra tops narrow, spiky benchmarks (cyber, ARC-AGI-3, FrontierMath) but lands #5 on the aggregate AA Index — re-run your own eval suite against your actual workload before defaulting to "newest flagship."
- **Meta is back in the closed-model conversation on efficiency, not scale.** If your model-selection process wrote Meta off after the open-weight silence and attrition headlines, revisit that — Muse Spark 1.3's training-loop gains and its "pay less, give us your traffic" contributor tier are both worth evaluating on their own terms.
- **Chain-of-thought monitorability is now a live procurement question, not a research footnote.** OpenAI's own disclosure that Astra's reasoning is harder to audit than its predecessor's should factor into any deployment where you rely on inspecting model reasoning for compliance or safety review.
- **Treat every remaining "coming soon" (Gemini 3.5 Pro, Grok 4.7, Mistral's flagship) as indefinite.** Three separate labs are now multiple cycles past their own informal targets with no new dates — don't let any roadmap depend on a specific ship date from any of the three.
- **Capex convergence across independent analysts (J.P. Morgan, Goldman, SemiAnalysis, all landing in the same $660-800B band) raises confidence in continued compute abundance** — plan pricing and capacity assumptions accordingly rather than hedging against a pullback that no data supports yet.

## Predictions & Bets

- **[2026-07-11]** (confidence: med, horizon: 3mo i.e. ~2026-10, status: open) — Gemini 3.5 Pro's eventual launch lands close to GPT-6 Astra/Fable 5.1 on reasoning benchmarks but does not retake #1 on the AA Index. Update 2026-09-05: still cannot be scored — 3.5 Pro remains unshipped and Google has stopped naming target dates entirely, the weakest signal yet on this prediction's timeline.
- **[2026-07-11]** (confidence: high, horizon: 6mo, status: RESOLVED — correct) — At least one more frontier lab gets a model release gated/delayed by a government/safety concern before end of 2026. Resolved 2026-08-10, reinforced 2026-09-05: GPT-6 Astra shipped Sept 3 as the direct deliverable of that gate, complete with a disclosed monitorability trade-off — the clearest full-cycle example yet.
- **[2026-07-11]** (confidence: med, horizon: 6mo, status: open, update 2026-09-05) — Mistral's teased open-weight frontier family lands closer to Qwen/DeepSeek tier than Fable/Astra tier. Now a fourth consecutive cycle with zero specs disclosed — trending toward "this model may not exist as originally teased" rather than toward resolution either way.
- **[2026-07-11]** (confidence: low, horizon: 12mo, status: open) — Meta does not ship another fully open-weight flagship at frontier scale within 12 months. Update 2026-09-05: strengthened by a new data point — Meta's frontier comeback (Muse Spark 1.3) is explicitly closed/API, not open weights, reinforcing this prediction's thesis that Meta's open-weight era is over.
- **[2026-07-31]** (confidence: med, horizon: 6mo i.e. ~2027-01, status: open, update 2026-09-05) — Open-weight models crack the top 5 of the AA Index within 6 months. Now closer than ever: Kimi K3 (#7, 59.7) and GLM-5.3 (#8) both sit inside the top 8, with GLM-5.3 achieving its jump via post-training alone. Trending toward correct but not yet resolved.
- **[2026-07-31]** (confidence: low, horizon: 6mo, status: open) — Google ships Gemini 4 before a standalone Gemini 3.5 Pro flagship ever reaches GA. No new evidence either way this cycle, but Google's refusal to name any new date strengthens the plausibility.
- **[2026-08-17]** (confidence: med, horizon: 3mo, status: RESOLVED — moot) — GPT-5.6 Sol's apparent drop from AA Index top 3 holds up and Sol doesn't reclaim top-3 without a new OpenAI release. Moot as of 2026-09-05: OpenAI released GPT-6 Astra, superseding Sol entirely before this could resolve either way.

## Changelog

- **[2026-09-05]** — Covered 2026-08-22 to 2026-09-05. Headline: OpenAI ships GPT-6 Astra (Sept 3) — first model to cross its own "Critical" cybersecurity threshold, saturates narrow benchmarks (ExploitBench 100%, ARC-AGI-3 99.9%, FrontierMath Tier 4 98%) but lands only AA Index #5, with a disclosed drop in chain-of-thought monitorability sparking industry debate. Anthropic beat it to market by two days with Claude Fable 5.1/Mythos 5.1 (Sept 1, same price, 75% cheaper cache reads, retook AA Index #1 at 65.7). Meta's Muse Spark 1.3 (Sept 2) cracked AA Index top 3 for the first time via training-loop efficiency, choosing closed API distribution over open weights and monetizing a "contributor" discount tier for training data. Z.AI's GLM-5.3 (Aug 14, backfilled as context) and Kimi K3 now sit in the AA Index top 8, nearing the standing open-weight-top-5 prediction. Grok 4.7, Gemini 3.5 Pro, and Mistral's frontier flagship all remain unresolved multi-cycle "coming soon" stories. Hyperscaler capex estimates converged across J.P. Morgan/Goldman/SemiAnalysis into a $660-800B/year band for 2026. No landmark research paper surfaced (4th consecutive cycle — checked HF Daily Papers/arXiv directly). Resolved one prediction correct (gov't/safety-gated release, via Astra), mooted one (Sol's AA rank, superseded by Astra), strengthened three others. Updated model landscape (Meta moved from open-weight to closed-frontier section), who's-ahead table, lab strategy watch, trend tracker (shifted columns left).
- **[2026-08-17]** — Covered 2026-08-10 to 2026-08-17. OpenAI operationalizes the Astra pause (new agentic-coding/cyber evals, Aug 16) rather than resuming timeline. Gemini 3.5 Pro misses a 4th date; Google ships Gemini 3.7 Flash (Aug 13) as a 3rd consecutive stopgap, now called "longest-awaited model of 2026." Stripe agrees to acquire OpenRouter for $7B+ (5.4x 3-month-old valuation) — infra-consolidation signal. DeepSeek V4-Pro GA (Aug 13) then hikes peak pricing ~14x (Aug 16) — first crack in open-weight cost collapse. OpenAI+Cerebras launch Ultrafast Sol tier (750 tok/s, 14x speed, no quality loss) — inference speed as new competitive axis. AA Index reshuffle: Fable 5 to 62.1, Grok 4.6 to 60.9, GPT-5.6 Sol apparently bumped from top 3 (verify next cycle). Grok 4.7 (2.1T) slips again to ~early September. Qwen 4.0/Mistral flagship: no movement, threads stay open. SemiAnalysis confirms hyperscaler capex accelerating (~$775-800B 2026). No landmark research paper surfaced (3rd cycle running — HF Daily Papers checked directly this time, still no hit). Updated who's-ahead, trend tracker (added infra-consolidation trend, cost-collapse ticked down), overview/landscape sections.
- **[2026-08-10]** — Covered 2026-08-03 to 2026-08-10. Headline: OpenAI confirms it's slowing Astra's release after it crossed a "critical cybersecurity threshold" (Aug 7) — resolves the standing gov't/safety-gating prediction as correct. xAI ships Grok 4.6 (1.5T, SFT/RL-driven gains) plus Grok Voice Think Fast 2.0; Qwen 3.8-Max (2.4T/95B active, $2/$6) joins the open-weight frontier tier; Amazon firms up Nova wind-down specifics (Premier/Omni/Reel/Canvas to maintenance) ahead of its re:Invent flagship; Gemini 3.5 Pro misses a third informal date, Bloomberg reports DeepMind rebuilt the base model; Artificial Analysis Intelligence Index v4.1.1 reconfirms Claude Opus 5 at #1 (63); Meta's next Llama pushed to year-end with continued talent attrition; Mistral's frontier-flagship status is now genuinely unclear given conflicting reporting. No landmark paper surfaced this cycle. Updated who's-ahead (multimodal/cost-efficiency/open-weight leaders shifted), trend tracker (gov't involvement surged to 5, cost collapse to 5), resolved one prediction, added Amazon as a tracked lab.
- **[2026-08-03]** — Thin 3-day cycle (2026-07-31 to 2026-08-03) but one high-signal story: OpenAI demoed a new "Astra" model class to Congress (multi-agent, long-horizon, claimed unsolved-math results, will go through gov't pre-release review — unverified). Also: Amazon guts its Nova lineup to bet on one frontier model under Pieter Abbeel (leans harder on Anthropic stake meanwhile); DeepSeek's V4-Flash-0731 gets a large agent-benchmark leap from post-training alone, no architecture change; MiniMax open-weights H3, a unified text/image/video/audio model with native stereo sound (2K, 15s clips) — open-weight's first serious push into closed-lab-grade video generation; federal EO 14409 frontier-model review framework missed its Aug 1 deadline with nothing public, while California's SB 942 provenance law went operative Aug 2 — state rules are binding before federal ones. Gemini 3.5 Pro remains unshipped, now the longest flagship slip of the year. No landmark research paper this cycle. Added OpenAI Astra note to Lab Strategy Watch; no who's-ahead leader changes (Astra unverified).
- **[2026-07-11]** — Initial creation. Established model landscape, capability frontiers, who's-ahead table, lab strategy watch, and trend tracker baseline (first reading, no prior columns) based on the 2026-06-27 to 2026-07-11 news cycle. Filed four opening predictions.
- **[2026-07-31]** — Covered 2026-07-17 to 2026-07-31 (plus notable spillover from the 07-11–07-17 gap: Inkling, Kimi K3 origin). Anthropic ships Opus 5 (new coding/agentic leader, undercuts Fable 5 on cost); Google slips Gemini 3.5 Pro a second time and teases Gemini 4; open-weight reaches frontier parameter scale via Moonshot Kimi K3 (2.8T) and Thinking Machines' Inkling (new lab entrant); Anthropic signs $5B/2GW AMD compute deal; OpenAI cuts Luna/Terra pricing sharply; METR eval-gaming finding on GPT-5.6 Sol surfaced as a follow-up safety signal. Updated who's-ahead table, trend tracker (open-weight surging to 5, govt involvement cooling to 3), and filed two new predictions on open-weight AA Index ranking and Gemini 4 vs. 3.5 Pro sequencing.
