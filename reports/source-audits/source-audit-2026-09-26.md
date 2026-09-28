---
title: Radar Source Audit — 2026-09-26
date: 2026-09-26
author: Skeptic
tags: [audit, sources, meta]
---

# Radar Source Audit — 2026-09-26

**Scope:** All five domains. Reports reviewed: frontier-watch 09-17 + 09-21; agentic-coding 09-14 + 09-21; production-ai-eng 09-14 + 09-21; ai-economics 09-14 + 09-21; research-pulse 09-05 + 09-14. Also checked citation domains across *all* reports per domain, and the uncommitted edits to `agents/agentic-coding-reporter.md`.
**Bottom line:** 3 recommendations, all hygiene: fixing dead entries and holding back a list expansion. The bigger finding isn't a sourcing problem. Every confirmed blind spot this cycle came from a source that is **already on the list** and wasn't read. Adding sources won't fix that.

## Headline Finding (outside the 3-rec cap — a process issue, not a source issue)

The newsletter tiers are decorative. In the last two reports per domain, the listed newsletters almost never appear: Import AI, The Batch, Ahead of AI, Last Week in AI, Stratechery, Pragmatic Engineer, Hamel, Eugene Yan, Chip Huyen, Noahpinion, Marginal Revolution and Clancy each got **0** citations. smol.ai got 1 and Interconnects got 1. Frontier-watch 09-17 cites kucoin.com (x2), cryptopolitan.com, nokiapoweruser.com, fool.com and progressiverobot.com. It cites **none** of its newsletter tier and one lab blog. Reporters are running open web searches and taking whatever SEO aggregator ranks highest.

Confirmed misses, each from a source already on the list:
- **OpenAI's Navier-Stokes Millennium Prize claim (2026-09-08).** Multi-agent system, 166-page proof + Lean formalization, plus the Buckmaster credit dispute. It was on openai.com, the smol.ai 09-08 headline, Quanta, Fortune and Axios. **Missed by frontier-watch 09-17 and research-pulse 09-14**, even though both windows included it. Research-pulse covered Anthropic's FLT formalization in the same window and still missed it. Probably the biggest research story of the quarter.
- **DeepMind's 100-agent math swarm cheating/whistleblower paper (09-03; MIT Tech Review 09-14).** Import AI #472 featured it. Missed by research-pulse and production-ai-eng.
- **Harvey acquires Guardrails AI (09-09).** Guardrails AI is a listed PAE primary source. Missed by PAE 09-14.
- **Factory raises $200M at $5B (factory.com, 09-15).** Factory is a listed agentic-coding primary source. Missed by agentic-coding 09-21.

The fix belongs in the reporter workflow, not the source list: explicitly fetch the latest issues of the top 2–3 newsletters and the primary-tier news pages each cycle, and down-rank citations from crypto/SEO aggregators. This is your call; the skeptic doesn't edit reporters.

## Per-Domain Verdict

### Frontier Watch — Adjust (hygiene only)
Relies on TechCrunch, Axios, Bloomberg and benchlm/marktechpost. Newsletter tier: 0 citations across the last two reports. Missed Navier-Stokes. The list itself is sound. The problem is execution, see above. Papers with Code is dead (302 redirect to huggingface.co/papers/trending) and is covered in Rec 1.

### Agentic Coding — Adjust
The healthiest execution: github.blog (26 citations across all reports), simonwillison.net (16), code.claude.com, blog.modelcontextprotocol.io. But across **all 12 reports**, the individual-voices tier beyond Willison has 0 citations: Yegge, Ball, Hashimoto, Huntley, swyx and Karpathy. So do Pragmatic Engineer, Interconnects, The Batch and Lobste.rs. The uncommitted edit adds four more voices, which goes against the evidence. See Rec 3. Missed Factory's $5B raise.

### Production AI Eng — Keep as-is
Citations are primary and reasonable (openai.com, aws.amazon.com, docs.langchain.com, Willison). Missed the Guardrails AI acquisition. **Watch:** after the Harvey acqui-hire the Guardrails hub reportedly sunset on 08-25 (one secondary source, beri.net, not independently confirmed). If that holds, Guardrails AI stops being a primary source next cycle.

### AI Economics — Keep as-is
The best source discipline in Radar: NBER (20 citations across all reports), BLS (12), Census BTOS, the Fed, PitchBook, Stanford Digital Economy Lab. Tier-3 commentators never appear, but Tier-1 is doing the work, so no change.

### Research Pulse — Adjust
Only 2 reports, so thin evidence. The list has problems anyway: several entries are dead or wrong (Rec 1), and 10 of the 14 "researcher tier" entries are reachable only via X, which the system can't read. Missed Navier-Stokes and the DeepMind swarm paper. There's no research-journalism layer to catch landmark results (Rec 2).

## Recommendations (3)

**[SWAP] — Fix dead/broken entries**  (research-pulse; also frontier-watch)
- **Why:** checked each one today.
  - `paperswithcode.com` 302-redirects to HF trending. Drop it from research-pulse and frontier-watch; HF Daily Papers is already listed in both.
  - `distill.pub` last published 2021-09-02, hiatus notice 2021-07-02. Olah's work now lives at `transformer-circuits.pub` (live, latest post Aug 2026).
  - `bengio.abrilab.net` doesn't resolve (DNS ENOTFOUND). The real site is `yoshuabengio.org`, active, latest post 2026-09-23 (UN Security Council speech).
  - Drop "Google Scholar alerts". An agent without an account can't use it.
- **Quality basis:** these are straight corrections to the canonical homes of the same sources.
- **Displaces:** nets out at -2 entries.

**[ADD] — Quanta Magazine** (quantamagazine.org)  (research-pulse)
- **Why:** closes the Navier-Stokes blind spot directly. Quanta ran it on 09-08, the day of the announcement. Its whole beat is landmark math, CS and physics results, which is exactly research-pulse's "shifts what's possible" mandate. Research-pulse currently has no curated editorial layer, only raw arXiv plus X handles it can't read.
- **Quality basis:** the standard for research journalism in math and theoretical CS, editorially independent (Simons Foundation), and trusted by researchers for accuracy.
- **Displaces:** Semantic Scholar. It's a paper-recommendation engine, has 0 citations, and duplicates arXiv/HF Papers.
- **Caveat:** Quanta only helps if the reporter actually reads it. Without the process fix above, this is a partial fix.

**[HOLD] — Don't commit the expanded agentic-coding voices tier as written**  (agentic-coding)
- **Why:** 12 reports of evidence. The 6 existing non-Willison voices produced 0 citations. The new entries are mostly X-handle-only (@paulgauthier, @antonosika, @hwchase17), which the system can't read. The Osika entry is stale: gpt-engineer turned into Lovable in 2024, so "GPT-engineer, AI scaffolding" describes a project that no longer exists. Simon Willison is now listed twice (newsletter tier and voices tier). The LangChain blog belongs in production-ai-eng, where LangChain/LangSmith is already a primary source.
- **Quality basis:** bounded lists win. Entries the agent can't fetch only suggest coverage that isn't happening.
- **Displaces:** keep only voices with fetchable blogs: Willison (once), Karpathy, Yegge, Ball, swyx. Drop X-only entries and the LangChain duplicate. If you want Aider signal, `aider.chat/HISTORY.html` is fetchable; @paulgauthier is not.

## Watch List (not recommendations)
- **smol.ai / AINews:** the last issue listed is 2026-09-10, a 16-day gap for a daily newsletter, with no announcement found. Many recent issues were "not much happened today." If it's still dark next audit, it's a drop candidate in 4 domains.
- **Guardrails AI** (PAE): see above.
