---
title: Research Pulse News Report — 2026-09-14
date: 2026-09-14
author: Research Pulse Reporter Agent
tags: [research, papers, frontier, safety, architecture, agents, news]
---

# Research Pulse News Report — 2026-09-14

## Executive Summary

The headline this cycle is Anthropic's autonomous formalization of Fermat's Last Theorem: a fleet of Claude agents produced a complete, machine-checked Lean 4 proof — 13 million lines of code, over 30,000 intermediate theorems, five times the size of Mathlib — in 11 days with minimal human direction, versus an estimated decade of human effort. It's the most concrete evidence yet that frontier models can sustain autonomous, multi-week formal-reasoning projects far beyond single-shot problem solving, even if the proof itself is a simplified restatement of Wiles's known approach rather than new mathematics.

The second thread is "AI researching AI" hardening from anecdote into infrastructure. OpenAI published hard internal metrics on research-task automation (3.1 agent-workdays logged per human workday, median researcher spending $600+/day on coding-agent inference), Meta FAIR shipped a preference model that ranks unrun ML experiment candidates to cut wasted GPU-hours, and Anthropic's Fermat effort is itself a data point in the same trend. Combined with the automated-alignment-researcher work covered last cycle, three separate labs are now independently converging on research-acceleration-via-agents as a core 2026 initiative — worth tracking as a leading indicator for internal tooling investment.

On architecture, a new latent-space language model (NCP-ArchPreview) reached OLMo-3-7B's pretraining loss using half the training tokens by predicting multi-token "concepts" alongside next-token prediction — a genuinely new pretraining objective, not a scaling tweak, at meaningful scale (8.9B params, 5.7T tokens). And Anthropic's Frontier Red Team published capability evaluations showing current models can now perform tactical intelligence-targeting and weapons-engineering tasks previously restricted to specialist humans — an understanding-shift result platform leaders should treat as a preview of forthcoming regulatory and enterprise-policy pressure on model access controls, not just a safety-team curiosity.

## Anthropic formalizes Fermat's Last Theorem — 13 million lines of autonomous, machine-checked Lean proof in 11 days

`project` `paper` `reasoning` `anthropic-research` · **Source:** [Formalizing Fermat's Last Theorem — Anthropic Research](https://www.anthropic.com/research/formalizing-fermats-last-theorem) · *Found: 2026-09-14*

Dozens of Claude agents, coordinating through an internal platform ("Prove2Me") with only occasional high-level task prioritization from a human, produced the first complete formal (Lean 4) proof of Fermat's Last Theorem: 13 million lines of code and roughly 30,300 proved theorems (29,500 in the final proof) — over 5x the size of Mathlib, Lean's entire community math library — consuming on the order of 6 billion output tokens over 11 days. Wiles's original 1995 proof took months to verify by hand; a fully formalized version was expected to take a human team roughly a decade. Anthropic is careful to flag limits: the proof follows a simplified version of Wiles's known strategy rather than discovering new mathematics, and the result is far more verbose than a human mathematician would produce. Still, sustaining a coherent multi-week formal-verification project with minimal steering is a different capability than benchmark-style single-shot proving, and it's the clearest agentic-autonomy data point to date outside of coding.

**More:** [Nature coverage](https://www.nature.com/articles/d41586-026-02822-9) · [Math Scholar](https://mathscholar.org/2026/09/ai-software-complete-a-formal-proof-of-fermats-last-theorem/)

## A new pretraining objective: predicting multi-token "concepts" cuts training tokens nearly in half

`paper` `architecture` `training` `open-source` · **Source:** [NCP-ArchPreview Technical Report — arXiv](https://arxiv.org/abs/2609.10715) · *Found: 2026-09-14*

Most 2026 architecture papers are scaling tweaks; this one changes the training objective itself. NCP-ArchPreview builds a discrete "concept" vocabulary (via product-quantized hidden states) that spans multiple tokens, then trains a dedicated Concept Module to predict future concepts jointly with standard next-token prediction, feeding predicted concepts back down to guide token-level generation. At 8.9B parameters trained on 5.73T tokens — the largest latent-space LM demonstration to date — it matches OLMo-3-7B's final pretraining loss using only 51.3% of the training tokens, while beating it by 2.45 points on downstream benchmarks (including a 5.99-point jump on GSM8K). If multi-token concept prediction generalizes past this scale, it's a direct lever on the single largest cost in frontier training: token count to reach a target loss.

**More:** [Hugging Face paper page](https://huggingface.co/papers/2609.10715)

## Three labs converge on AI-accelerated AI research as core infrastructure, not a side project

`blog-post` `agents` `training` `openai-research` `meta-fair` · **Source:** [Research acceleration: the view inside OpenAI](https://simonwillison.net/2026/Sep/6/research-acceleration-the-view-inside-openai/) · *Found: 2026-09-14*

OpenAI published internal metrics on how far agentic tooling has penetrated its own research workflow: the org logged 3.1 agent-workdays of effort for every human workday by August, with the median researcher spending over $600/day on coding-agent inference at API prices, and every category of research activity — coding, running evals, monitoring live experiments — grew from January to August. Their next explicit target is a fully automated AI researcher by March 2028. The same week, Meta FAIR published AI Research Preference Models (RPMs) — a model that ranks *unexecuted* ML experiment candidates before any GPU time is spent, lifting AIRS-Bench from 0.684 to 0.729 with no additional training, directly attacking the bottleneck that idea generation is now cheap but verification (actually running the candidate) is not. Read together with Anthropic's automated-alignment-researcher work and the Fermat effort (both covered separately), three labs are now independently treating "agents doing research on how to do research" as core 2026 infrastructure rather than a demo. For platform teams, this is the leading indicator to watch before it shows up as a product feature: internal research-agent tooling investment is running well ahead of what's externally visible.

**More:** [Meta FAIR RPMs coverage — MarkTechPost](https://www.marktechpost.com/2026/09/06/meta-fair-introduces-ai-research-preference-models-rpms-ranking-ml-experiments-before-spending-gpu-hours/amp/)

## Frontier models can now perform tactical targeting and weapons-engineering tasks once restricted to trained specialists

`paper` `evaluation` `safety` `anthropic-research` · **Source:** [Measuring AI capabilities in intelligence targeting and conventional weapons — Anthropic](https://www.anthropic.com/research/intelligence-targeting-conventional-weapons-capabilities) · *Found: 2026-09-14*

Anthropic's Frontier Red Team built new evaluations for two specific capability classes — locating people from fragmentary intelligence fragments, and engineering weapons (e.g., drones) to strike moving targets — and found current frontier Claude models, plus at least one tested open-weight PRC model, can now perform tasks in both categories that historically required scarce, highly trained human experts. This is a genuine capability-understanding shift, not an incremental benchmark move: it's the first public evidence that dual-use military-adjacent capability has crossed a threshold specific labs are treating as requiring new on-platform safety classifiers, and Anthropic says the findings are being shared with government and industry partners to shape broader standards. Expect this to accelerate export-control and enterprise-access-policy conversations well before it shows up as a headline product restriction.

**More:** [Blockchain.News coverage](https://blockchain.news/news/anthropic-ai-surveillance-weapons-evaluation)

## Research Themes This Cycle

- **AI-accelerated AI research is now a cross-lab pattern, not one lab's story.** OpenAI's internal metrics, Meta FAIR's experiment-ranking model, and Anthropic's autonomous Fermat proof all landed within the same nine-day window — independently corroborating last cycle's Anthropic "automated researchers" finding. This is compounding faster than public model releases suggest.
- **Formal, long-horizon reasoning is a live frontier, not just chat-turn reasoning.** The Fermat formalization and NCP-ArchPreview's concept-level prediction are both evidence that 2026's interesting reasoning work is happening at the level of sustained multi-step structure (proofs, concepts) rather than longer chains of next-token generation.
- **Capability-threshold safety findings are arriving faster than governance frameworks can absorb them.** Anthropic's tactical-targeting/weapons eval is a genuine "understanding shift" result that will likely drive policy conversations (export control, enterprise access tiers) well before any lab ships a corresponding product change.
- **Quiet on the researcher-tier this cycle.** No new in-window output from Karpathy (last public activity was an April Sequoia talk), LeCun/AMI Labs (LeWorldModel predates window), or Ilya Sutskever/SSI (still no technical publication, only partnership news) — worth checking again next cycle rather than treating as a trend.
