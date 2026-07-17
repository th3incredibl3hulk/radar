---
name: report-history
description: Last report date, per-cycle coverage log, and dedup guidance for production-ai-eng reporter
metadata:
  type: project
---

## Last report
- **2026-07-13** — `reports/production-ai-eng/production-ai-eng-news-2026-07-13.md`. Short 2-day cycle (window: 2026-07-11 to 2026-07-13). Only 3 entries qualified; padding avoided per instructions. Living doc `production-ai-eng-state-of-the-art.md` updated same date.

## Coverage log (avoid re-covering these)

### 2026-07-13 cycle (window 07-11 to 07-13)
- Hamel Husain / Parlance Labs, "Do Automated Evals Work?" (2026-07-11) — empirical comparison of Braintrust Loop, Arize Alyx, LangSmith, and coding-agent judges vs. human-labeled ground truth on a production apartment-leasing dataset. Found all judges share a "criteria drift" blind spot (context-dependent failures invisible in trace). https://parlance-labs.com/blog/posts/auto-evals/index.html
- OpenAI GPT-5.6 "Sol" launch capacity/reliability firefight (2026-07-09 through 07-13) — traffic doubled in 48h, rate limits reset twice, 5-hour cap suspended temporarily, Codex lead (Tibo Sottiaux) publicly denied quiet capacity-driven quality cuts on 07-13. Framed as SRE-for-LLM-APIs case study.
- DTEX Claude Cowork insider-threat simulations (primary research 2026-07-09) amplified via Forbes Technology Council op-ed by Mohan Koo (2026-07-13) — agents with legitimate access completed Salesforce-to-Outlook exfil-draft chain in 24 min, file-archive transfer in 10 min. Argument: identity-based zero trust insufficient, need behavioral/action-chain tracing.
- Noted but placed in "on the radar" (outside strict window, not counted as dated entries): First Recon AI Security Runtime GA (2026-07-08); Braintrust GLM-5.2 built-in model + rolling small UI updates (no single dated headline).
- Checked and found NO new movement this cycle on carryover watch items: Google DeepMind multi-agent safety fund (proposals due 2026-08-08, winners autumn 2026 — nothing yet); EU Digital Omnibus VII (Council approved 2026-06-29, still not seen published in Official Journal); Fullstack Code Arena adoption signal (too early); LangSmith changelog (no entries dated between 2026-07-04 and 2026-07-13 — most recent entries were 2026-06-29 to 07-03, already covered last cycle).
- Verified and REJECTED a stale/confused web-search claim: "Anthropic acquires Humanloop ~2 weeks before 2026-07-13" — this is wrong, the actual Anthropic/Humanloop acqui-hire was 2025-08-13 (already old news, was folded into the 07-11 baseline report's Key Players section). Don't re-verify this every cycle, but don't trust AI-search-summary claims about acquisition timing without checking a primary source — search summarization drifted the date by ~11 months.

### 2026-07-11 cycle (baseline/inaugural, window ~2026-06-04 to 07-11, widened deliberately)
- EU AI Act high-risk deadline delayed 16 months (Council final approval 2026-06-29, Digital Omnibus VII)
- AWS Well-Architected Agentic AI Lens (published 2026-06-10)
- Microsoft year-one red-teaming taxonomy v2.0 — HITL bypass named top exploited failure mode (2026-06-04)
- NIST/Apostol Vassilev Gödel-incompleteness proof re: guardrails (announced 2026-06-09)
- Cursor reward-hacking research on SWE-bench Pro (~2026-06-26/27)
- LangSmith full-stack cost observability + composite evaluators (shipped 2026-06-29 to 07-03)
- OpenAI GPT-Live system card / full-duplex voice safety stack (2026-07-08)
- SemiAnalysis enterprise token-budgeting survey (2026-07-01)
- lmarena Fullstack Code Arena launch (2026-07-02)
- Google DeepMind $10M multi-agent safety research fund announced (2026-06-11, proposals due 2026-08-08)

## Watch list for next cycle
- Google DeepMind multi-agent safety fund winners (expected autumn 2026 — check again in Sept/Oct cycles, nothing to check before then)
- EU Digital Omnibus VII formal Official Journal publication (check each cycle until confirmed published)
- Fullstack Code Arena adoption/usage data (check occasionally, no fixed cadence expected)
- LangSmith changelog cadence — went quiet 07-04 to 07-13 (9 days with no entries after multiple-per-week pace in June); confirm whether this is a real slowdown or a documentation lag next cycle
- Braintrust product changelog — rolling small updates (GLM-5.2 built-in model, tag-filter/span-error UI changes) without a single dated flagship post; consider checking their changelog page directly (not search) next cycle for a consolidated item
