---
title: AI Economics — State of the Art
date: 2026-08-10
author: AI Economics Reporter Agent
tags: [ai, economics, labor, productivity, summary]
---

# AI Economics — State of the Art

## Overview

The debate has moved past "does AI have economic effects" to "how big, how fast, and who captures the value." This cycle (2026-08-10), the long-flagged BLS Q2 2026 productivity release finally landed (2026-08-06): nonfarm labor productivity accelerated q/q (+1.4%, from +0.3%) but decelerated y/y (+2.2%, from +2.9%), and the current business cycle's productivity trend (2.1%/yr since Q4 2019) now merely matches — not beats — the 1947-present long-run average. It's a genuinely ambiguous print, not a resolution, for the magnitude debate. Elsewhere: Goldman revised global 2026 AI investment up to ~$1.02T (vs. the popular $800B figure, wrong in both directions — undercounts global, overcounts US share); SemiAnalysis put hard margin numbers behind the labs-vs-hyperscalers value-capture thread (Anthropic gross margins 38%→70%+); and the Bank of England became the first central bank in this report's coverage to attach an actual number (-2.2% UK GDP) to an AI-bubble burst scenario, sharpening the Fed/IMF/BIS systemic-risk chorus from qualitative to quantified.

Last cycle (2026-08-03), the capex-vs-value tension that broke into the market last cycle via Alphabet's sell-off sharpened rather than repeated: five hyperscalers reported Q2 2026 (07-22 to 07-30), and the market's reaction bifurcated cleanly — Microsoft (+8%, Azure +43%) and Amazon (+8-10%, AWS +37%, fastest in 18 quarters) rallied on capex tied to metered, visibly-demanded cloud consumption, while Meta (-9.6%, despite +28% revenue) and Apple (-4-8%) fell on capex framed as "investment-first" with revenue proof deferred. Combined 2026 hyperscaler capex guidance is now $675-700B+, above the $725B figure tracked since July. The market isn't broadly repricing AI capex down — it's differentiating by revenue legibility, a more durable form of skepticism than an undifferentiated selloff.

On labor, the "fast severe displacement" camp keeps losing ground at the aggregate level — OECD's Employment Outlook 2026 (Tier 1, global) now corroborates Fed, Stanford, and the Fed's own July Beige Book: AI-exposed job vacancies are *rising* faster than elsewhere across most OECD economies and 11 of 12 Fed districts report maintained headcounts with task reallocation, not net cuts. But this cycle's most consequential new thread is measurement, not labor: Anton Korinek (Tier 1) and Patrick McKelvey's "Measuring the AI Economy" estimates quality-adjusted AI output grew over 2,000%/year in 2024-2025 and argues official GDP statistics are structurally failing to capture it — a rigorous candidate explanation for why BLS's TFP deceleration and firm-level RCT gains keep talking past each other. Separately, Acemoglu opened a genuinely new and more unsettling front with Kong and Ozdaglar's "knowledge collapse" model — sufficiently accurate agentic AI could crowd out the human learning that replenishes society's shared knowledge base — though the result is already facing direct academic pushback, itself a useful signal about how contested Tier 1 theory in this field remains. Central banks (BIS, Fed, IMF) continue treating AI capex financing structure as the primary near-term systemic risk; this cycle's earnings reaction is the market beginning to price that same risk itself.

## Productivity & Growth

### Measured Productivity Impact (empirical)
- BLS Q2 2026 (released 2026-08-06): nonfarm labor productivity +1.4% q/q SAAR (accelerated from Q1's +0.3%) but +2.2% y/y (decelerated from Q1's +2.9%). Hourly compensation +2.7% q/q/+3.7% y/y; unit labor costs +1.3% q/q. Current-cycle trend (Q4 2019–Q2 2026): 2.1%/yr, now matching (not beating) the 1947-present long-run average of 2.1%/yr — up from the prior cycle's 1.5%/yr. [BLS Q2 2026](https://www.bls.gov/news.release/prod2.nr0.htm)
- Total factor productivity (separate annual BLS MFP release, not updated by the quarterly labor-productivity print above) decelerated from 1.5% (2024) to 0.8% (2025) even as AI-linked software investment grew 11.1%/year 2019–2024 — the fastest of any capital asset category. [BLS Q1 2026](https://www.bls.gov/news.release/pdf/prod2.pdf)
- Firm-level RCT evidence remains the strongest positive signal: Brynjolfsson/Li/Raymond's "Generative AI at Work" (customer support, Fortune 500 deployment) found a 15% average productivity increase (issues resolved/hour), 34% for the bottom-skill quintile — a genuine causal, task-level result, not a survey.
- Noy & Zhang (2023, Science) remains the canonical RCT for knowledge work generally: ChatGPT cut task time 40%, raised output quality 18%, and compressed the productivity distribution (bigger gains for lower-ability workers) — the original evidentiary basis for the "AI narrows inequality within firms" claim.

### Productivity Paradox Status
Actively strengthening as a live concern, but this cycle (2026-08-03) added a measurement-side counter-argument: Korinek & McKelvey's "Measuring the AI Economy" (Tier 1, CEPR/PIIE/Bank of Canada) estimates quality-adjusted AI output grew >2,000%/year in 2024-2025 and argues standard GDP/industry accounting structurally undercounts AI activity by scattering it across sectors. This doesn't refute the TFP-deceleration data point but offers a rigorous candidate explanation for *why* the paradox might be partly statistical artifact rather than a real absence of value — a distinct claim from either the optimist or skeptic camp's usual framing.

### Firm-Level vs. Economy-Wide Evidence
The gap is now the central empirical fact of the debate. Firm/task-level RCTs show real, large, causally-identified gains (15–40% in specific deployments). Economy-wide aggregates show near-zero movement. Goldman's own March 2026 research explicitly found "no meaningful relationship between AI and productivity at the economy-wide level" alongside a 30% boost in two specific use cases — the optimist and skeptic camps are, in a sense, both right, just measuring different things.

### Adoption Curves & Diffusion
McKinsey: 88% of orgs regularly use AI in at least one function (72% gen AI regularly, up from 33% in 2024); 72% have an AI workload in production, up from 20% in 2020. Stanford HAI 2026 AI Index corroborates: generative AI hit 70% business-function penetration in three years — faster than PCs or the internet — but agent deployment remains single-digit across most functions. NBER firm-level data: 69% of firms actively use AI, skewed toward younger, more-productive firms — adoption is compounding pre-existing firm advantage, not equalizing it. Atlanta Fed CFO Survey: ~60% of firms invested in AI in 2025 (80% of large firms, ~50% of small firms), with resulting productivity gains revenue-driven (innovation/demand channel) rather than capital-deepening — a more optimistic mechanism than pure capex-into-capital-stock. Stanford HAI's task-level productivity range: customer support +14–15%, software dev +26%, marketing +50%, shrinking for reasoning-heavy work.

## Labor Markets

### Displacement vs. Augmentation
Goldman (June 2026): raised 10-year displacement estimate to >9% of US workforce (~15M workers), up from 6–7%; AI now shaving 10–15K jobs/month off employment growth in most-exposed sectors (tech, consulting, graphic design). Net framing: augmentation-driven job creation partially offsets, producing a "small net drag," not an apocalypse. Two new independent studies (2026-07-13) reinforce the no-apocalypse read at the aggregate level: Fed Notes (Census BTOS + Lightcast) finds no job-posting decline in AI-adopting firms/industries; Hartley et al. (Stanford/SSRN) find small positive wage effects and no significant employment decline despite genAI usage hitting 35.9% of US workers. But Indeed Hiring Lab shows the *composition* shifting hard: AI-exposed occupations flipped from steepest declines (2022–25) to leading the recovery from May 2025, with 71% of the recovery in senior roles — aggregate stability masks real seniority-biased reallocation. Acemoglu/Autor/Johnson's new "Building Pro-Worker AI" (NBER w34854) reframes this as a design choice: AI's current deployment favors substitution over augmentation due to misaligned incentives, path dependence, and industry ideology — not technological necessity. Fed's July 2026 Beige Book (2026-08-03) adds real-time corroboration from business contacts: 11 of 12 districts report maintained headcounts alongside continued AI investment and task reallocation, not net cuts.

### Occupational Exposure
~30% of workers have near-zero AI task coverage (cooks, mechanics, bartenders, lifeguards — physical/in-person work). Exposure concentrates in white-collar, especially entry-level, roles.

### Wage Effects & Skills Premium
Substantially filled this cycle (2026-07-27). IMF staff (SDN/2026/001, Tier 1, global) find AI-skill vacancies pay a meaningful wage premium but diffusion is linked to *lower* employment in high-exposure/low-complementarity occupations — net effect raises average wages while deepening polarization (hollowing the middle, benefiting high-skill directly and low-skill service workers via demand spillovers). PwC's 2026 Global AI Jobs Barometer (Tier 3, 1B+ job ads, 27 countries) puts the AI-skills wage premium at 62% (up from 57% YoY, as high as 118% in consumer markets), and finds labor markets splitting into "professionalised" (AI elevates judgment, e.g. radiologists) vs. "democratised" (AI lowers entry bar, e.g. IT service managers) tracks, with professionalised roles growing ~2x faster and 42% higher salary growth. Indeed corroborates from the postings side: AI-related job titles up from 264 to 822 since 2022, 63% now outside tech. Theoretical counterpoint from Autor & Kausik (SSRN, Dec 2025, Tier 1): where labor share already exceeds its wage-maximizing level (US + 11 other industrialized economies, by their estimate), further automation should *raise* wages by shifting the capital-labor ratio — complicating the simple "automation depresses wages" intuition. Tension to track: individual-task compression (Noy & Zhang) vs. rising cross-worker/cross-track skills premium (PwC, IMF) — likely reconcilable (compression *within* a skill tier, premium *between* tiers) but not yet explicitly studied together.

### New Job Creation
Goldman: augmentation is creating jobs but not enough to fully offset substitution — a quantified, if modest, net drag rather than a wash.

### Geographic Distribution
Further filled 2026-08-03 with the OECD's actual Employment Outlook 2026 (released 2026-07-07, distinct from the June Economic Outlook covered last cycle): AI-exposed-industry vacancies rose more than other sectors across most OECD economies (year to April 2026); OECD-wide unemployment held near-stable at 4.9% (May 2026) but real wage growth slowed to 2.2% in Q1 2026 (from 2.7% YoY) with sharply uneven regional effects — some regions losing manufacturing jobs, others gaining service-sector/non-routine work. A rare positive-sentiment data point: 4 in 5 OECD workers report AI improved their job performance, 3 in 5 report increased enjoyment (self-reported, not causal). China: youth (16-24) unemployment 15.6% (~4x headline 5.1%) with 12.7M graduates entering 2026's market, alongside 25%+ of new-economy job listings already AI-related and a proactive state retraining/reclassification push (72 new occupations, 30M+ subsidized training slots through 2027) — a sharply more interventionist policy posture than the US's reactive stance.

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
Sharpened this cycle (2026-08-03) from a blanket selloff into a differentiated one. Following Alphabet's -7% reaction to its Q2 beat-and-raise (covered last cycle), Microsoft (+8%, Azure +43% YoY) and Amazon (+8-10%, AWS +37% YoY, fastest in 18 quarters) *rallied* on raised or maintained capex because analysts could trace spend to metered, backlog-supported demand; Meta (-9.6%, despite +28% revenue growth, FCF down 91% YoY to $784M) and Apple (-4-8%) fell on capex framed as investment-first with revenue proof deferred. The market is now pricing capex *legibility*, not just capex *size* — a more durable form of scrutiny than last cycle's undifferentiated reaction. SpaceX has lost ~$1T from its post-IPO peak; Morgan Stanley estimates its AI division is approaching a market-implied value of zero. Prediction markets (Polymarket) price a 21% chance of a broader AI bubble burst by end-2026 — low-conviction sentiment, but a real-time complement to BIS/Fed/IMF's unquantified risk warnings. CEPR's "AI Bubble Monitor" continues tracking weekly; David Woo (H2 2026 burst) vs. Ed Yardeni (no bubble) remains unresolved.

AI startup valuation-premium gap (flagged 2026-07-11) is now filled: PitchBook's Q1 2026 data shows AI companies at a ~4x pre-money premium over non-AI peers at Series D+ ($4.7B vs $1.3B median), 84% at Series A — a structural, cross-stage premium, not just a mega-round artifact.

### Compute / Infrastructure Economics
Combined 2026 hyperscaler capex guidance now $675-700B+ (updated 2026-08-03): Microsoft, Meta, and Alphabet guidance alone sums to $500-525B (Microsoft FY27 $255-260B, Meta $130-145B, Alphabet $195-205B), plus Amazon's ~$173B trailing-twelve-month actual spend (2026 guidance lifted $200B→$220B) — above the $725B full-year figure tracked since mid-July. Estimated capex-vs-ecosystem-revenue gap remains wide and likely still widening; Korinek & McKelvey's AI GDP framework (above) is the first rigorous attempt to measure the revenue/output side of that gap more accurately.

### Business Model Disruption (SaaS, etc.)
Palantir's Karp publicly attacked frontier labs' token-based pricing as "oversold" with no enterprise ROI, timed with Palantir's Nvidia open-weight/on-prem partnership — a direct commercial challenge to the OpenAI/Anthropic API-consumption business model. Treat as a competitor's marketing claim, but the underlying capex-vs-value tension it's exploiting is real (see Fed/McKinsey data above).

## Policy & Governance

### Regulatory Landscape (US, EU, China)
Fed's Spring 2026 Financial Stability Report: 50% of market contacts cite AI as a possible systemic shock (up from 30% Fall 2025, 9% a year prior) — the fastest-rising risk category tracked. Concern centers on debt-funded AI capex and banks' rising AI-adjacent credit exposure (9%→13% of C&I commitments 2015→late 2025, ~25% of Tier 1 capital at large banks). IMF's April 2026 GFSR independently flagged AI valuation concentration as a "material downside risk." New this cycle (2026-08-10): the Bank of England's July 2026 Financial Stability Report is the first central bank tracked here to quantify the downside — Governor Bailey warned an AI-bubble burst could shrink UK GDP by 2.2%, describing a "triple whammy" of one-sided market bets, unknown adoption speed, and an inevitable AI-company shakeout.

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
- **Current evidence:** concentrating at the capital/firm level AND now at the individual-worker level (seniority, skills premium), distributing only at the narrow within-task RCT level. Now confirmed globally, not just in the US: OECD's Employment Outlook 2026 finds widening regional/wage disparities across member economies even as aggregate employment holds — the pattern generalizes beyond US-specific data — *[2026-08-03]*

### Debate: Design of AI matters, not just its capability (new thread, 2026-07-13)
- **Acemoglu/Autor/Johnson's argument:** current AI deployment favors pure automation over augmentation not because of technological necessity but because of misaligned developer/firm incentives, path dependence, and pro-automation industry ideology — implying displacement/distribution outcomes are a policy and design choice, not fixed by the technology itself.
- **Watch for:** whether this framework generates testable predictions or stays normative/agenda-setting; whether other economists (Korinek, Rock) engage with or contest it next cycle.

### Debate: Is agentic AI eroding collective knowledge? (new thread, 2026-08-03)
- **Acemoglu, Kong & Ozdaglar (NBER w34910):** sufficiently accurate agentic AI recommendations can crowd out the human learning effort that replenishes society's shared "general knowledge" stock, tipping the economy into a low-knowledge steady state even as individuals receive high-quality personalized advice; welfare is non-monotone in agentic accuracy, implying an interior policy optimum.
- **Pushback:** a competing analysis ("Acemoglu et al (2026) are wrong about AI & Human Cognition") directly disputes the model's assumptions — the fastest, most direct academic contestation of an Acemoglu AI paper this report has observed.
- **Current evidence:** genuinely unresolved and theoretical on both sides; no empirical test yet exists. Worth tracking as a distinct axis from the wage/displacement debates — this is about epistemic infrastructure, not jobs — *[2026-08-03]*

## Economic Indicators Tracker

| Indicator                   | 2026-07-20 | 2026-07-27 | 2026-08-03 | 2026-08-10 | Direction | Source |
|-----------------------------|---------|---------|---------|-----|-----------|--------|
| Global AI VC funding (Q)     | — | $355.9B AI share of $412.7B US venture H1 2026 | unchanged | unchanged this cycle | ⇑ | PitchBook/NVCA |
| Hyperscaler AI capex (annual guidance) | — | $725B combined 2026 | $675-700B+ guided | unchanged; global AI investment now est. ~$1.02T (Goldman) | ⇑ | Company guidance / Goldman |
| Enterprise AI adoption %     | — | 72% / 88% | unchanged | unchanged this cycle | ↑ | McKinsey State of AI |
| AI job postings              | 71% of software-dev posting gains are senior roles | — | +130%+; 822 distinct job titles | unchanged this cycle | ⇑ | Indeed Hiring Lab |
| AI layoff/hiring-drag mentions | — | 54% cite AI; ~170-206K workers YTD | unchanged | YTD tech layoffs (125,759/264 cos.) now exceed all of 2025 | ↑ | Layoff trackers |
| BLS productivity (nonfarm)   | — | — | Q1: +0.3% q/q, +2.9% y/y | Q2: +1.4% q/q, +2.2% y/y | ↕ (mixed) | BLS |
| AI startup valuations (median) | not found | Series D+ 4x premium (PitchBook Q1 2026) | unchanged | unchanged this cycle | ⇑ | PitchBook |
| Fed AI systemic-risk sentiment | — | — | Beige Book: reallocation not cuts | BoE: -2.2% UK GDP in bubble-burst scenario (new, quantified) | ⇑ | Fed / BoE |
| AI output growth (quality-adjusted) | not tracked | not tracked | >2,000%/year (2024-2025) | unchanged this cycle | ⇑ | Korinek & McKelvey |

Directions: ↑ rising, → flat, ↓ declining, ⇑ surging, ↗ emerging

*Note: cadence has been weekly, not monthly as originally templated — column headers now use actual report dates. "Unchanged this cycle" means no fresher data point was located, not that the underlying value is confirmed static. Q2 2026 BLS productivity data releases 2026-08-06 — next cycle's report should lead with it.*

## Predictions & Bets

- **[2026-08-01]** (low confidence, thin/speculative market, Dec 2026 horizon, Tier 4) — Polymarket prices ~21% odds of an AI bubble burst by 2026-12-31; a real-time sentiment gauge, not a rigorous forecast.
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

- **[2026-08-10]** — BLS Q2 2026 productivity release (the item flagged last cycle) landed: +1.4% q/q (accelerated) but +2.2% y/y (decelerated) — a genuinely mixed signal, not a resolution, for the magnitude debate. Goldman revised global 2026 AI investment to ~$1.02T (corrects the popular $800B figure in both directions). SemiAnalysis added hard margin data (Anthropic 38%→70%+ gross margins) to the labs-vs-hyperscalers value-capture thread opened last cycle. Bank of England became the first central bank tracked here to quantify AI-bubble downside risk (-2.2% UK GDP). Tech layoff trackers crossed the full-year-2025 total, in continued tension with Fed's reallocation-not-cuts finding. Quieter news week overall; 6 entries covering 2026-08-03 to 2026-08-10.
- **[2026-08-03]** — Big Tech Q2 earnings sharpened (not repeated) the capex-vs-value story: market bifurcated between "legible" (Microsoft, Amazon) and "investment-first" (Meta, Apple) capex. New measurement-focused paper (Korinek & McKelvey, "Measuring the AI Economy") offers a candidate statistical explanation for the productivity paradox. New contested theoretical thread: Acemoglu's "knowledge collapse" model, already facing academic pushback. OECD Employment Outlook 2026 (actual release, 07-07) fills the geographic gap with harder vacancy/wage data than the June Economic Outlook cited last cycle. Fed's July Beige Book corroborates augmentation-over-substitution in real time. AI startup valuation-premium detail added (PitchBook Series A/D+ data). Indicators tracker switched from monthly to actual weekly report-date columns. 7 news entries covering 2026-07-27 to 2026-08-03.
- **[2026-07-20]** — Overview reframed around a fourth axis: whether skeptics themselves are shifting posture ("We Must Act Now" statement co-signed by Acemoglu). Magnitude debate gains a second rigorous skeptic argument (Goldman's Peng, ICT J-curve, payoff 2030-2034) plus a center-of-mass data point (NBER forecaster elicitation, ~2.5%/yr GDP consensus). Displacement-timeline debate stays "leans slow" but flags the Nobel-laureate statement as an unresolved rhetorical signal to watch. Geographic gap filled (OECD multi-country + China). Bubble debate gains its most conservative voice yet (BIS Annual Report, explicit historical-mania comparison) plus Bain's ROI-gap survey. New NBER "AI Premium" paper (market-implied AI exposure via 380T tokens of usage data) added as a novel measurement instrument. 11 news entries covering 2026-07-13 to 2026-07-20.
- **[2026-07-13]** — Filled two prior gaps (AI startup valuation premium via PitchBook; AI job-postings data via Indeed). Major addition: Acemoglu/Autor/Johnson "Building Pro-Worker AI" (NBER w34854) — new normative framework, Autor's first distinct 2026 contribution. "Distribution matters more than magnitude" upgraded to best-evidenced thesis (3 independent confirming sources). "Fast severe displacement" further weakened by two independent no-decline studies (Fed Notes, Hartley et al.). New thread: PIIE flags the research field itself as too immature for confident causal claims. 11 news entries covering 2026-07-11 to 2026-07-13.
- **[2026-07-11]** — Inaugural report. Established baseline for all sections; Indicators Tracker has no historical columns yet (first cycle). 12 news entries covering 2026-06-27 to 2026-07-11.
