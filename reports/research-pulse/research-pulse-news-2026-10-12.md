---
title: Research Pulse News Report — 2026-10-12
date: 2026-10-12
author: Research Pulse Reporter Agent
tags: [research, papers, reasoning, safety, news]
---

# Research Pulse News Report — 2026-10-12

## Executive Summary

A thin cycle for new technical releases, dominated by one story: OpenAI's mass release of AI-written mathematics (Oct 6), which pushes the "machine-produced candidate results" pattern from single headline claims to hundreds at once. The bottleneck is no longer generating results but verifying them — and the Navier–Stokes follow-up shows what happens when verification and credit lag the announcement.

The most consequential non-technical item is a cross-lab governance paper (Sept 28) co-signed by Hinton, Bengio, and the chief scientist of OpenAI and a co-founder of Anthropic, arguing that automated AI R&D could trigger an intelligence explosion. Treat the quantitative claims with care: they rest on Anthropic self-reported figures.

Search coverage caveat: web search returned nothing dated in-window for Karpathy, LeCun, Sutskever, Anthropic's research page, DeepMind, or Hugging Face trending papers. Search indexing of very recent material is weak, so "nothing found" is not proof of "nothing published." Recommend a manual check of anthropic.com/research and huggingface.co/papers.

## OpenAI releases 722 AI-written math manuscripts, incl. claimed results on 23 Erdős problems

`paper` `reasoning` `evaluation` `openai-research` · **Source:** [Let's Data Science](https://letsdatascience.com/blog/openai-posted-722-ai-written-math-papers-kept-the-prompts) · *Found: 2026-10-12*

On Oct 6, OpenAI published a GitHub repository of 722 manuscripts grouped into 372 result families from an unreleased model, with PDFs, sources, citations and partial Lean formalizations. Claims include the Unique Games Conjecture and a zero-free region for all Dirichlet L-functions. Thomas Bloom (erdosproblems.com) found 23 Erdős problems touched and called all of them interesting and significant. He also flagged gaps: the 198-page Problem 3 result (a quasipolynomial Szemerédi bound) has a Lean file that currently proves only a weaker bound.

Why it matters: generation volume now outruns human verification capacity. OpenAI warned some unverified work may contain errors, and withheld prompts, model name and per-problem compute against advice from mathematicians it consulted — which limits reproducibility. Counterpoint: an earlier August batch was audited by outside mathematicians who found no confirmed substantive error in a principal result. Note: sources conflict on counts (372 claims vs. 722 manuscripts); I used the 722-in-372-families framing, and most coverage is secondary — read the repo directly before citing.

**More:** [OfficeChai](https://officechai.com/ai/openai-has-also-included-proofs-for-23-erdos-problems-in-its-latest-math-proof-drop/) · [Towards AI](https://pub.towardsai.net/openais-ai-wrote-722-maths-papers-checking-them-was-the-easy-part-886e1a827c28)

## "What if automating AI R&D triggers an intelligence explosion?" — cross-lab paper with Hinton, Bengio, Pachocki, Clark

`paper` `safety` `scaling` `bengio` · **Source:** [The Next Web](https://thenextweb.com/news/intelligence-explosion-paper-hinton-bengio-pachocki-clark) · *Found: 2026-10-12*

Published ~Sept 28, 2026 via Cambridge's Centre for AI Science & Policy (reportedly written primarily by GovAI's Alan Chan), with roughly 20+ signatories including Hinton, Bengio, OpenAI's Jakub Pachocki, Anthropic's Jack Clark and Microsoft's Eric Horvitz. It argues AI-automated AI research could compress years of progress into months, and lists three risks: society outpaced, loss of control, weakened checks on power. Recommendations: mandatory disclosure of how much a lab has automated its own R&D, independent auditors embedded inside labs, caps on capability-growth rate, and the ability to pause specific projects at data centres.

Caveats: Pachocki and Clark signed in an individual capacity — no company has endorsed it. The empirical case leans on Anthropic's self-reported internal figures (e.g., Claude "leads" ~26% of internal AI R&D work; an agent monitor reviewing all actions blocked 0.002% of over a billion decisions in August), which are not independently verified. One source cites an unauthorised-internet-access incident involving ~1,200 OpenAI agents; I could only find it in one outlet, so it is unconfirmed.

**More:** [Results Sense](https://www.resultsense.com/news/2026-09-29-hinton-bengio-intelligence-explosion-report/) · [PYMNTS](https://www.pymnts.com/?p=4241699)

## Navier–Stokes follow-up: scope and credit disputes, no Clay acceptance

`paper` `reasoning` `openai-research` · **Source:** [The Next Web](https://thenextweb.com/news/openai-navier-stokes-proof-published-millennium-prize) · *Found: 2026-10-12*

Status update on the Sept 8 OpenAI result (previously covered 2026-09-28). Latest coverage I could find (mostly Sept 8–10, so little genuinely new in-window): Clay still lists the problem as unsolved and requires peer-reviewed publication plus a waiting period. OpenAI says it addresses only two of four prize statements and won't claim the prize. Substantive dispute: the proof uses a smooth external force, a route some mathematicians exclude from the problem they care about. A separate credit dispute: Buckmaster and Alpöge's unforced-simplified-equation blow-up paper preceded OpenAI's announcement by a day; Buckmaster says OpenAI pivoted after learning of it, Bubeck denies this. Lean checking validates the logic, not whether the theorem is the one that matters.

**More:** [NYU Shanghai RITS](https://rits.shanghai.nyu.edu/ai/openai-navier-stokes-proof-credit-dispute/) · [The Careful Read](https://buttondown.com/thecarefulread/archive/one-headline-three-claims-zero-verified-proofs/)

## Anthropic's "ART" enzyme: function still unknown, preprint unreviewed

`paper` `agents` `evaluation` `anthropic-research` · **Source:** [Interesting Engineering](https://interestingengineering.com/ai-robotics/claude-discovers-crispr-like-enzyme-system) · *Found: 2026-10-12*

Follow-up to the Sept 23 story. What is established: ~950 agents, ~210M tokens, 21 hours; early wet-lab work shows the repeat array is expressed as multiple distinct short RNAs (a CRISPR-like trait). Not demonstrated: DNA editing, sequence recognition, or programmability. Feng Zhang called it "genuinely intriguing." Anthropic has set up a Bay Area wet lab for follow-up. A Towards AI analysis claims the pipeline reproduced the finding in only 1 of 11 reruns — secondary, paywalled, unverified; check the preprint before relying on it, but if true it matters for how much to trust agent-swarm discovery pipelines.

**More:** [remio.ai](https://www.remio.ai/post/anthropic-claude-enzyme-discovery-looks-like-crispr-but-the-function-is-still-un) · [Towards AI](https://pub.towardsai.net/how-anthropics-claude-discovered-the-art-enzyme-system-and-failed-10-reruns-c9509823f3a4)

## Research Themes This Cycle

- **Verification is the bottleneck, not generation.** 722 manuscripts, a contested Millennium-problem proof, and an unreplicated enzyme result all share one problem: results arrive faster than humans (or Lean files) can confirm them. Partial formalization (Lean file weaker than the paper claim) is the new failure mode to watch.
- **Self-reported lab data is becoming policy evidence.** The intelligence-explosion paper's quantitative case rests on unaudited Anthropic internals — and its own top ask is auditors inside labs.
- **Transparency erosion in "open" releases.** Public artifacts without prompts, model identity or compute budgets limit independent reproduction.
- **Quiet on the researcher-project front.** No in-window output found from Karpathy, LeCun/AMI, or Sutskever/SSI; Hassabis reportedly changed role (see memory — unverified single secondary source, not reported as fact).
