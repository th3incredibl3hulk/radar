---
title: AI Economics — State of the Art
date: 2026-07-27
author: AI Economics Reporter Agent
tags: [ai, economics, labor, productivity, summary]
---

# AI Economics — State of the Art

## Overview

The debate has moved past "does AI have economic effects" to "how big, how fast, and who captures the value." This cycle (2026-07-27), the capex-vs-value tension that's been building in surveys and central-bank reports for two months hit the market directly: Alphabet's Q2 2026 beat-and-raise (82% Google Cloud growth, but capex guidance up to $195–205B and negative free cash flow for the first time since its 2004 IPO) triggered a 7% stock drop and a 4.8% single-session fall in the Magnificent Seven, its worst day since April 2025. SpaceX, two months off its IPO, has shed roughly $1T in peak value, with Morgan Stanley calculating its AI division is approaching a market-implied valuation of zero ($818M revenue vs. $2.47B operating loss). These are the first hard price-action data points for a thesis BIS, Bain, and Goldman's own J-curve research have been building with surveys and historical analogy since June.

On labor, the "fast severe displacement" camp keeps losing ground at the aggregate level — OECD, Fed, and Anthropic's own data all show no widespread displacement, even as seniority- and skill-biased reallocation keeps showing up in the disaggregated data (Indeed, Anthropic's 22–25-year-old hiring gap). This cycle sharpened the "distribution matters more than magnitude" thesis specifically on wages: IMF staff research (Tier 1, filling a long-standing geographic/wage gap), PwC's 1B-job-ad Barometer, and Indeed's postings data independently converge on a "two-track" labor market — AI-skill wage premiums widening (62%, up from 57% YoY) and job-title diversity exploding (822 distinct US AI-related titles, up from 264 in 2022, 63% now outside tech) even as enterprise-side ROI stays elusive (PwC CEO survey: 56% report zero net financial benefit, echoing Bain and McKinsey). A separate theoretical contribution from David Autor (with B.N. Kausik) complicates the simple displacement-anxiety intuition: when labor share already exceeds its wage-maximizing level, as the authors estimate is true in the US, further automation can *raise* wages rather than lower them. Central banks (BIS, Fed, IMF) continue treating AI capex financing structure — now visibly stress-testing itself in the market — as the primary near-term systemic risk.

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
Substantially filled this cycle (2026-07-27). IMF staff (SDN/2026/001, Tier 1, global) find AI-skill vacancies pay a meaningful wage premium but diffusion is linked to *lower* employment in high-exposure/low-complementarity occupations — net effect raises average wages while deepening polarization (hollowing the middle, benefiting high-skill directly and low-skill service workers via demand spillovers). PwC's 2026 Global AI Jobs Barometer (Tier 3, 1B+ job ads, 27 countries) puts the AI-skills wage premium at 62% (up from 57% YoY, as high as 118% in consumer markets), and finds labor markets splitting into "professionalised" (AI elevates judgment, e.g. radiologists) vs. "democratised" (AI lowers entry bar, e.g. IT service managers) tracks, with professionalised roles growing ~2x faster and 42% higher salary growth. Indeed corroborates from the postings side: AI-related job titles up from 264 to 822 since 2022, 63% now outside tech. Theoretical counterpoint from Autor & Kausik (SSRN, Dec 2025, Tier 1): where labor share already exceeds its wage-maximizing level (US + 11 other industrialized economies, by their estimate), further automation should *raise* wages by shifting the capital-labor ratio — complicating the simple "automation depresses wages" intuition. Tension to track: individual-task compression (Noy & Zhang) vs. rising cross-worker/cross-track skills premium (PwC, IMF) — likely reconcilable (compression *within* a skill tier, premium *between* tiers) but not yet explicitly studied together.

### New Job Creation
Goldman: augmentation is creating jobs but not enough to fully offset substitution — a quantified, if modest, net drag rather than a wash.

### Geographic Distribution
Gap partially filled 2026-07-20. OECD's June 2026 Economic Outlook (multi-country) finds no widespread labour displacement and rising vacancies in AI-exposed industries — a global corroboration of the US-only Fed/Stanford findings. China: youth (16-24) unemployment 15.6% (~4x headline 5.1%) with 12.7M graduates entering 2026's market, alongside 25%+ of new-economy job listings already AI-related and a proactive state retraining/reclassification push (72 new occupations, 30M+ subsidized training slots through 2027) — a sharply more interventionist policy posture than the US's reactive stance.

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
Escalated sharply this cycle (2026-07-27): Alphabet's Q2 beat-and-raise (82% cloud growth) still triggered a 7% stock drop and dragged the Magnificent Seven down 4.8% in one session (worst since April 2025), on raised capex guidance ($195–205B) and Alphabet's first negative free cash flow since its 2004 IPO. SpaceX has lost ~$1T from its post-IPO peak; Morgan Stanley estimates its AI division is approaching a market-implied value of zero ($818M revenue vs. $2.47B operating loss). These are the first price-action (not survey/forecast) confirmations of the capex-vs-value gap. CEPR's "AI Bubble Monitor" continues tracking weekly. Economist David Woo predicts an H2 2026 bubble burst; Ed Yardeni disputes the bubble framing entirely. JPMorgan (2026-06-25) remains the main bull-side pushback: hyperscaler AI-cloud revenue growing 28–123% YoY, calling the buildout "profitable for now" — but the market's own reaction this cycle is now cutting against that framing in real time.

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
- **Optimist:** AI adds 1–2% annual GDP growth within 5 years (Goldman's general framing, a16z, Brynjolfsson's FT commentary); Goldman's own "physical economy" thesis ($7.6T 2026-31) is bullish on capex scale even as its economists turn cautious on timing
- **Skeptic:** Acemoglu: ~0.07pp/year TFP, 0.7% cumulative over a decade. New this cycle: Goldman's Elsie Peng, using an ICT-revolution J-curve analogy, argues the macro payoff doesn't arrive until 2030-2034 — a Tier 2, methodologically distinct argument converging with Acemoglu's Tier 1 skepticism
- **Center of mass:** NBER's forecaster-elicitation paper (Karger/Tetlock, w35046) finds academic economists, AI-company employees, policy researchers, superforecasters, and the public all converge near ~2.5%/yr GDP growth — above consensus baselines but well below 4%+ maximalist scenarios
- **Current evidence:** leans skeptic-to-measured at the macro level; two independent methods (TFP accounting, historical-analogy econometrics) now argue for a *later* payoff, not just a *smaller* one, while firm/task-level RCTs still show large gains (15-40%) in specific deployments — the aggregation puzzle is now also a timing puzzle — *[2026-07-20]*

### Debate: Job displacement timeline
- **Fast:** significant white-collar displacement within 2-3 years (Aschenbrenner-style framing). New wrinkle: "We Must Act Now" (16 Nobel laureates incl. Acemoglu, 2026-07-13) warns disruption could compress "into years, not generations" — but this is a policy-advocacy statement, not a revised empirical estimate; Acemoglu's own published research timeline is unchanged
- **Slow:** gradual task-level reallocation over 10-20 years (Acemoglu's research position, Autor; Goldman's own 10-year 9% estimate fits this camp)
- **Current evidence:** leans slow at the aggregate level — OECD (global, multi-country) now joins Fed/Stanford in finding no widespread displacement and rising vacancies in AI-exposed industries, three independent Tier-1 sources in two cycles. The "We Must Act Now" statement is a genuine signal worth tracking but should not yet be read as empirical evidence of a faster timeline — watch whether Acemoglu's actual research shifts next, which would be the real tell — *[2026-07-20]*

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

- **[2026-07-20]** — Overview reframed around a fourth axis: whether skeptics themselves are shifting posture ("We Must Act Now" statement co-signed by Acemoglu). Magnitude debate gains a second rigorous skeptic argument (Goldman's Peng, ICT J-curve, payoff 2030-2034) plus a center-of-mass data point (NBER forecaster elicitation, ~2.5%/yr GDP consensus). Displacement-timeline debate stays "leans slow" but flags the Nobel-laureate statement as an unresolved rhetorical signal to watch. Geographic gap filled (OECD multi-country + China). Bubble debate gains its most conservative voice yet (BIS Annual Report, explicit historical-mania comparison) plus Bain's ROI-gap survey. New NBER "AI Premium" paper (market-implied AI exposure via 380T tokens of usage data) added as a novel measurement instrument. 11 news entries covering 2026-07-13 to 2026-07-20.
- **[2026-07-13]** — Filled two prior gaps (AI startup valuation premium via PitchBook; AI job-postings data via Indeed). Major addition: Acemoglu/Autor/Johnson "Building Pro-Worker AI" (NBER w34854) — new normative framework, Autor's first distinct 2026 contribution. "Distribution matters more than magnitude" upgraded to best-evidenced thesis (3 independent confirming sources). "Fast severe displacement" further weakened by two independent no-decline studies (Fed Notes, Hartley et al.). New thread: PIIE flags the research field itself as too immature for confident causal claims. 11 news entries covering 2026-07-11 to 2026-07-13.
- **[2026-07-11]** — Inaugural report. Established baseline for all sections; Indicators Tracker has no historical columns yet (first cycle). 12 news entries covering 2026-06-27 to 2026-07-11.
