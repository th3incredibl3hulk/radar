---
title: AI Economics — State of the Art
date: 2026-07-13
author: AI Economics Reporter Agent
tags: [ai, economics, labor, productivity, summary]
---

# AI Economics — State of the Art

## Overview

The debate has moved past "does AI have economic effects" to "how big, how fast, and who captures the value." Two data streams are diverging sharply. The financial/capex stream is unambiguous and enormous: $725B in 2026 hyperscaler capex guidance, 86% of US venture dollars going to AI, two labs (OpenAI, Anthropic) capturing 43% of all global startup funding. The macro-productivity stream is stubbornly unimpressive by comparison: BLS total factor productivity decelerated in 2025, McKinsey's own survey shows only 39% of enterprises can point to EBIT impact despite near-universal adoption, and the most rigorous academic estimate (Acemoglu) puts the 10-year cumulative TFP gain at well under 1%. The open question isn't whether AI matters economically — it clearly does, at minimum as a capital-allocation phenomenon — but whether the productivity payoff catches up to the spend before markets lose patience, and who ends up holding the value: the labs, the hyperscalers, or the enterprises paying for tokens.

On labor, the "fast severe displacement" camp keeps losing ground: a Fed Notes study (Census BTOS + Lightcast) and a Stanford/SSRN paper (Hartley et al.) both independently find no aggregate job-posting or employment decline in AI-adopting firms/occupations despite generative AI usage rocketing to 35.9% of US workers by Dec 2025. But the more durable, increasingly well-evidenced question is *distributional*: Indeed Hiring Lab now shows AI-exposed occupations flipping from the steepest job-posting declines (2022–2025) to leading the recovery — with 71% of that recovery in senior roles. Acemoglu has now teamed with David Autor on a normative framework ("Building Pro-Worker AI") arguing this distributional skew is a design choice, not an inevitability. Central banks have started treating AI concentration and debt-funded capex as a financial-stability risk in its own right, independent of the labor-market debate.

## Productivity & Growth

### Measured Productivity Impact (empirical)
- BLS: nonfarm business labor productivity +0.3% q/q in Q1 2026 (+2.9% y/y, a deceleration). Total factor productivity decelerated from 1.5% (2024) to 0.8% (2025) even as AI-linked software investment grew 11.1%/year 2019–2024 — the fastest of any capital asset category. [BLS Q1 2026](https://www.bls.gov/news.release/pdf/prod2.pdf)
- Firm-level RCT evidence remains the strongest positive signal: Brynjolfsson/Li/Raymond's "Generative AI at Work" (customer support, Fortune 500 deployment) found a 15% average productivity increase (issues resolved/hour), 34% for the bottom-skill quintile — a genuine causal, task-level result, not a survey.
- Noy & Zhang (2023, Science) remains the canonical RCT for knowledge work generally: ChatGPT cut task time 40%, raised output quality 18%, and compressed the productivity distribution (bigger gains for lower-ability workers) — the original evidentiary basis for the "AI narrows inequality within firms" claim.

### Productivity Paradox Status
Actively strengthening as a live concern. TFP deceleration in the face of record AI-linked capex is the first hard macro data point supporting "Productivity Paradox 2.0" rather than just theoretical Solow-paradox analogizing.

### Firm-Level vs. Economy-Wide Evidence
The gap is now the central empirical fact of the debate. Firm/task-level RCTs show real, large, causally-identified gains (15–40% in specific deployments). Economy-wide aggregates show near-zero movement. Goldman's own March 2026 research explicitly found "no meaningful relationship between AI and productivity at the economy-wide level" alongside a 30% boost in two specific use cases — the optimist and skeptic camps are, in a sense, both right, just measuring different things.

### Adoption Curves & Diffusion
McKinsey: 88% of orgs regularly use AI in at least one function (72% gen AI regularly, up from 33% in 2024); 72% have an AI workload in production, up from 20% in 2020. Stanford HAI 2026 AI Index corroborates: generative AI hit 70% business-function penetration in three years — faster than PCs or the internet — but agent deployment remains single-digit across most functions. NBER firm-level data: 69% of firms actively use AI, skewed toward younger, more-productive firms — adoption is compounding pre-existing firm advantage, not equalizing it. Atlanta Fed CFO Survey: ~60% of firms invested in AI in 2025 (80% of large firms, ~50% of small firms), with resulting productivity gains revenue-driven (innovation/demand channel) rather than capital-deepening — a more optimistic mechanism than pure capex-into-capital-stock. Stanford HAI's task-level productivity range: customer support +14–15%, software dev +26%, marketing +50%, shrinking for reasoning-heavy work.

## Labor Markets

### Displacement vs. Augmentation
Goldman (June 2026): raised 10-year displacement estimate to >9% of US workforce (~15M workers), up from 6–7%; AI now shaving 10–15K jobs/month off employment growth in most-exposed sectors (tech, consulting, graphic design). Net framing: augmentation-driven job creation partially offsets, producing a "small net drag," not an apocalypse. Two new independent studies (2026-07-13) reinforce the no-apocalypse read at the aggregate level: Fed Notes (Census BTOS + Lightcast) finds no job-posting decline in AI-adopting firms/industries; Hartley et al. (Stanford/SSRN) find small positive wage effects and no significant employment decline despite genAI usage hitting 35.9% of US workers. But Indeed Hiring Lab shows the *composition* shifting hard: AI-exposed occupations flipped from steepest declines (2022–25) to leading the recovery from May 2025, with 71% of the recovery in senior roles — aggregate stability masks real seniority-biased reallocation. Acemoglu/Autor/Johnson's new "Building Pro-Worker AI" (NBER w34854) reframes this as a design choice: AI's current deployment favors substitution over augmentation due to misaligned incentives, path dependence, and industry ideology — not technological necessity.

### Occupational Exposure
~30% of workers have near-zero AI task coverage (cooks, mechanics, bartenders, lifeguards — physical/in-person work). Exposure concentrates in white-collar, especially entry-level, roles.

### Wage Effects & Skills Premium
Gap partially filled 2026-07-13: Hartley/Jolevski/Melo/Moore (Stanford/SSRN) find small but statistically significant *positive* wage effects from generative AI adoption, concentrated among younger, college-educated, higher-earning workers, alongside no significant employment decline. PwC's 2026 Global AI Jobs Barometer (Tier 3, job-ad-based) finds the AI-skills wage premium at 62% (up from 57% YoY), with AI-skill job postings growing ~8x the overall market rate. Noy & Zhang's within-firm compression finding (AI narrows gaps between high- and low-skill workers on a given task) remains the most-cited RCT data point. Tension to track: individual-task compression (Noy & Zhang) vs. rising cross-worker skills premium (PwC) — likely reconcilable (compression *within* a skill tier, premium *between* tiers) but not yet explicitly studied together.

### New Job Creation
Goldman: augmentation is creating jobs but not enough to fully offset substitution — a quantified, if modest, net drag rather than a wash.

### Geographic Distribution
Not well covered this cycle — flagged as a gap; the domain sources lean US-centric (BLS, Fed, Goldman). Should actively search for EU/OECD and China-specific labor data in future cycles.

## Industry Transformation

### Software & Technology
Tech and financial services lead enterprise AI adoption at 88% and 79% respectively (McKinsey). Most-exposed to near-term displacement per Goldman (alongside consulting, graphic design).

### Financial Services / Healthcare / Manufacturing
Goldman flagged the "next AI boom" shifting toward the physical economy — factories, mines, utilities, oil rigs — as compute/data-center buildout matures. Limited hard data yet; watch next cycle.

### Professional Services (Legal, Consulting)
Management consulting named explicitly by Goldman as a high-exposure sector already seeing hiring-growth drag.

### Creative Industries / Education
Graphic design named by Goldman as high-exposure. No major education-specific data this cycle.

## Investment & Market Dynamics

### VC Funding Landscape
US venture: $412.7B deployed H1 2026 (+~30% vs. all of 2025); $355.9B (86%) to AI companies. OpenAI ($122B) + Anthropic ($95.6B) = 43% of *all* global startup funding. Anthropic alone raised $65B in Q2 2026 — ~1/3 of that quarter's global VC total. Fund-level concentration: 5 managers captured 73.1% of Q1 2026 US VC fundraising.

### Enterprise AI Spending
72% of enterprises have an AI workload in production; only 23% report scaling agentic AI anywhere in the org; no function exceeds 10% agent-scaling penetration; only 39% report enterprise-level EBIT impact (McKinsey).

### Public Market Valuations
Hyperscaler stocks sold off following Q1/Q2 2026 earnings calls despite (or because of) capex guidance increases — investor patience signal. CEPR has launched a dedicated "AI Bubble Monitor." Economist David Woo predicts an H2 2026 bubble burst; Ed Yardeni disputes the bubble framing entirely. JPMorgan (2026-06-25) adds real data to the bull side: hyperscaler AI-cloud revenue growing 28–123% YoY (AWS/Google Cloud/Azure), calling the buildout "profitable for now" — the first investment-bank pushback on bubble-skeptics backed by revenue figures rather than just sentiment, though Sequoia's ~$600B/yr revenue-gap estimate remains unresolved on the other side.

AI startup valuation-premium gap (flagged last cycle) is now filled: PitchBook's Q1 2026 data shows AI companies at a ~4x pre-money premium over non-AI peers at Series D+ ($4.7B vs $1.3B median), 84% at Series A — a structural, cross-stage premium, not just a mega-round artifact.

### Compute / Infrastructure Economics
Combined 2026 hyperscaler capex guidance: $725B (+77% YoY) — Amazon $200B, Google $175–185B, Microsoft $110–120B (Meta not separately itemized this cycle). Estimated $600B/year gap between AI infrastructure spend and AI ecosystem revenue, and widening.

### Business Model Disruption (SaaS, etc.)
Palantir's Karp publicly attacked frontier labs' token-based pricing as "oversold" with no enterprise ROI, timed with Palantir's Nvidia open-weight/on-prem partnership — a direct commercial challenge to the OpenAI/Anthropic API-consumption business model. Treat as a competitor's marketing claim, but the underlying capex-vs-value tension it's exploiting is real (see Fed/McKinsey data above).

## Policy & Governance

### Regulatory Landscape (US, EU, China)
Fed's Spring 2026 Financial Stability Report: 50% of market contacts cite AI as a possible systemic shock (up from 30% Fall 2025, 9% a year prior) — the fastest-rising risk category tracked. Concern centers on debt-funded AI capex and banks' rising AI-adjacent credit exposure (9%→13% of C&I commitments 2015→late 2025, ~25% of Tier 1 capital at large banks). IMF's April 2026 GFSR independently flagged AI valuation concentration as a "material downside risk."

### Industrial Policy & International Competition
Atlanta Fed proposes a tax on automation-derived profits paired with subsidies for firms preserving entry-level task exposure, explicitly to protect the "learning by doing" pipeline (reviving Arrow 1962). Not yet enacted policy — a research proposal, flagged for tracking.

## The Great Debate

### Debate: Magnitude of productivity impact
- **Optimist:** AI adds 1–2% annual GDP growth within 5 years (Goldman's general framing, a16z, Brynjolfsson's FT commentary that "the AI productivity take-off is now visible in US economic data")
- **Skeptic:** Acemoglu: ~0.07pp/year TFP, 0.7% cumulative over a decade — roughly 5% of tasks profitably automatable near-term
- **Current evidence:** leans skeptic at the macro level (BLS TFP deceleration, Goldman's own "no meaningful economy-wide relationship" finding) while firm/task-level RCTs continue to show large, real, causally-identified gains (15–40%) in specific deployments. The unresolved question is aggregation: why isn't a 15% productivity gain in customer support showing up in nonfarm TFP? — *[2026-07-11]*

### Debate: Job displacement timeline
- **Fast:** significant white-collar displacement within 2–3 years (Aschenbrenner-style framing; implicit in the more alarmist capex-driven narratives)
- **Slow:** gradual task-level reallocation over 10–20 years (Acemoglu, Autor; Goldman's own 10-year 9% estimate fits this camp despite the higher headline number)
- **Current evidence:** leans slow. Even the institution that raised its displacement estimate (Goldman) explicitly frames the outcome as gradual reallocation with net drag, not fast apocalypse — *[2026-07-11]*

### Debate: Distribution of gains
- **Concentrating:** NBER firm data shows adoption skewed to already-productive, younger firms; VC funding concentrated in 2 labs (43% of global funding) and 5 fund managers (73% of Q1 fundraising); McKinsey shows scaled value capture concentrated in a handful of functions; PwC finds top-quintile AI-exposed firms at 163% productivity growth vs. 24% for least-exposed; PitchBook's 4x valuation premium concentrates at Series D+; Indeed's labor-market recovery is 71% senior roles
- **Distributing:** Noy & Zhang's original RCT found AI compresses within-firm productivity gaps (bigger gains for lower-skill workers on a given task)
- **Current evidence:** concentrating at the capital/firm level AND now at the individual-worker level (seniority, skills premium), distributing only at the narrow within-task RCT level. This is now the single best-evidenced thesis in the debate — three independent sources this cycle (Indeed, PwC, PitchBook) all point the same direction — *[2026-07-13]*

### Debate: Design of AI matters, not just its capability (new thread, 2026-07-13)
- **Acemoglu/Autor/Johnson's argument:** current AI deployment favors pure automation over augmentation not because of technological necessity but because of misaligned developer/firm incentives, path dependence, and pro-automation industry ideology — implying displacement/distribution outcomes are a policy and design choice, not fixed by the technology itself.
- **Watch for:** whether this framework generates testable predictions or stays normative/agenda-setting; whether other economists (Korinek, Rock) engage with or contest it next cycle.

## Economic Indicators Tracker

| Indicator                   | 3mo ago | 2mo ago | 1mo ago | Now | Direction | Source |
|-----------------------------|---------|---------|---------|-----|-----------|--------|
| Global AI VC funding (Q)     | —       | —       | —       | ~$205B (US, Q2 2026); $355.9B AI share of $412.7B US venture H1 2026 | ⇑ | PitchBook/NVCA |
| Hyperscaler AI capex (annual guidance) | —  | —       | —       | $725B combined 2026 (+77% YoY) | ⇑ | Company guidance / Goldman |
| Enterprise AI adoption %     | —       | —       | —       | 72% have AI workload in production; 88% use AI in ≥1 function | ↑ | McKinsey State of AI |
| AI job postings              | —       | —       | —       | n/a — not found this cycle | — | — |
| AI layoff/hiring-drag mentions | —     | —       | —       | ~10–15K jobs/month shaved off growth in most-exposed sectors | ↑ | Goldman Sachs Research |
| BLS productivity (nonfarm)   | —       | —       | —       | +0.3% q/q, +2.9% y/y (Q1 2026); TFP decelerated 1.5%→0.8% in 2025 | ↓ | BLS |
| AI startup valuations (median) | —     | —       | —       | Series D+ pre-money $4.7B (4x non-AI); Series A 84% premium | ⇑ | PitchBook Q1 2026 |
| Fed AI systemic-risk sentiment | —     | —       | —       | 50% of market contacts cite AI as risk (up from 30%) | ⇑ | Fed Financial Stability Report |
| Software-dev postings (senior share of gains) | — | — | — | 71% of net US software-dev posting increase is senior roles (May 2025–May 2026) | ↗ | Indeed Hiring Lab |

Directions: ↑ rising, → flat, ↓ declining, ⇑ surging, ↗ emerging

*Note: this is the first cycle of this tracker — historical columns are blank by construction. Populate retroactively where possible next cycle, and prioritize finding AI job-postings data (Indeed Hiring Lab tracks this) and median AI startup valuation data (PitchBook) which were not located this cycle.*

## Predictions & Bets

- **[2026-06-25]** (medium confidence, ongoing, Tier 2) — JPMorgan: AI capex buildout is "profitable for now" through 2030 ($5.5T global), conditional on hyperscaler cloud AI revenue sustaining 28–123% YoY growth rates.
- **[2026-07-04]** (low confidence, H2 2026, unresolved, Tier 3) — David Woo predicts the AI bubble bursts in H2 2026, citing AI-boom-sustained elevated real yields.
- **[2026-06-25]** (medium confidence, 10-year horizon, unresolved, Tier 2) — Goldman Sachs: >9% of US workforce (~15M workers) displaced by AI over 10 years, net "small drag" not apocalypse.
- **[2026-05-11]** (medium-high confidence given track record, 10-year horizon, unresolved, Tier 1) — Acemoglu: ~0.7% cumulative TFP gain from AI over 10 years; ~5% of tasks profitably automated near-term.

## What This Means for Platform Leaders

- The capex-to-value gap is now visible in official data (BLS TFP deceleration) and survey data (McKinsey's 39% EBIT-impact figure) simultaneously — don't assume vendor ROI claims will hold up to scrutiny; ask what "scaled" actually means operationally, not just what's in production.
- Central banks are treating AI concentration as a financial-stability risk independent of whether the productivity case pans out. If your platform strategy depends on continued hyperscaler capex growth, model a scenario where that capex decelerates for balance-sheet reasons unrelated to AI's actual usefulness.
- The credible displacement forecasts (Goldman, Acemoglu) both converge on "gradual reallocation, not sudden collapse" — this argues for a multi-year workforce-transition plan over crash reskilling, but the entry-level/junior-pipeline risk (Atlanta Fed's "learning by doing" concern) is a genuine second-order risk worth planning for now, before it shows up in your own senior-talent pipeline.
- Watch the adoption-vs-scaling gap in your own org against McKinsey's benchmarks (88% adoption / 23% agentic scaling / 39% EBIT impact) — if you're below those figures you're behind peers; if you're claiming to be far above them without hard EBIT evidence, be skeptical of your own reporting.

## Changelog

- **[2026-07-13]** — Filled two prior gaps (AI startup valuation premium via PitchBook; AI job-postings data via Indeed). Major addition: Acemoglu/Autor/Johnson "Building Pro-Worker AI" (NBER w34854) — new normative framework, Autor's first distinct 2026 contribution. "Distribution matters more than magnitude" upgraded to best-evidenced thesis (3 independent confirming sources). "Fast severe displacement" further weakened by two independent no-decline studies (Fed Notes, Hartley et al.). New thread: PIIE flags the research field itself as too immature for confident causal claims. 11 news entries covering 2026-07-11 to 2026-07-13.
- **[2026-07-11]** — Inaugural report. Established baseline for all sections; Indicators Tracker has no historical columns yet (first cycle). 12 news entries covering 2026-06-27 to 2026-07-11.
