---
name: source-quality
description: Which sources produced real signal vs. generic SEO/content-marketing noise during production-ai-eng research, to speed up future search passes
metadata:
  type: reference
---

## High-signal sources (went straight to primary/dated news)
- **Official vendor/gov press releases** — nist.gov, consilium.europa.eu (EU Council), deepmind.google/blog, docs.aws.amazon.com/wellarchitected, openai.com/index, microsoft.com/security/blog. Always try to find the primary source page directly rather than aggregator coverage — dates and specifics are far more reliable.
- **Cursor's engineering blog** (cursor.com/blog) — publishes real research with hard numbers (e.g. reward-hacking %s), not marketing copy. Worth checking every cycle.
- **SemiAnalysis newsletter** (newsletter.semianalysis.com) — consistently has hard enterprise cost data (token counts, budget ranges, margins). Best cost-engineering source found.
- **LangSmith/LangChain changelog** (docs.langchain.com/langsmith/changelog) — dated, specific, ships fast (multiple entries per week). Good weekly-ish check.
- **Cloud Security Alliance research notes** (labs.cloudsecurityalliance.org) — good secondary analysis layer on top of NIST/primary security research.

## Low-signal / mostly noise
- Generic WebSearch queries like "LLM evals framework release 2026" or "AI guardrails 2026" return overwhelmingly SEO/content-marketing "2026 guide" pages (getmaxim.ai, various dev.to/medium posts, "Best X in 2026" comparison sites) with no real dates or news — these are evergreen content, not news. Don't waste search budget re-running broad "X 2026" queries; go straight to named-source + date-bounded queries instead (e.g. "site:cursor.com/blog" style, or "[company] blog July 2026").
- Hamel Husain / Chip Huyen / Eugene Yan personal blogs are excellent for applied practice *content* but publish infrequently — don't expect a hit every 2-week cycle. Eugene Yan's "Patterns for Building Cybersecurity Evals" (2026-06-21) was the one relevant hit this cycle, just outside window.
- ThoughtWorks Technology Radar publishes only ~2x/year (last relevant: Vol 34, April 2026) — check its publish cadence before searching for it every cycle; it will rarely have fresh material in a 2-week window.

## Search strategy notes for next cycle
- Named-entity + month/year queries (e.g. "Anthropic blog July 2026 agent safety") outperform generic topic queries for finding dated news.
- arXiv paper IDs encode YYMM (e.g. 2606.xxxxx = June 2026) — useful for quickly filtering in-window research without opening every paper.
- AInews/smol.ai (news.smol.ai) daily issues are a good one-stop aggregator for what broke through in a given week — worth checking issue-by-issue rather than searching generically.

## Update [2026-07-13 cycle, 2-day window]
- **Hamel Husain's actual blog lives at parlance-labs.com/blog/posts/**, not hamel.dev directly (hamel.dev links out to it). WebFetch on the bare hamel.dev/blog/posts/<slug>/ path 404s — fetch the parlance-labs.com/blog/ index first to get the exact post URL, then fetch that.
- **WebSearch's AI-generated summary answers can drift dates by months** — one query returned "Anthropic acquires Humanloop ~2 weeks before 2026-07-13" when the real event was 2025-08-13 (11 months off). Always verify any date-sensitive claim from a WebSearch summary against a primary source or a second independent search before citing it in a report. This is a bigger risk than the known SEO-padding trap — it's a false negative risk (missing this check could have caused a fabricated-looking entry to ship).
- **Forbes Council posts (forbes.com/councils/forbestechcouncil/)** are contributor op-eds, not Forbes staff reporting — treat as opinion/analysis, tag `opinion`, but they're a decent way to surface a vendor's own research (e.g. DTEX's) that hasn't otherwise broken through. Check who the author is and what company they're from; the "source" is really the company research they're citing.
- **docs.langchain.com/langsmith/changelog fetch results can be inconsistent between a direct WebFetch and a WebSearch AI-summary of the same page** — WebFetch of the actual page said no entries existed in a given date range while a WebSearch summary for the same query listed several. Trust the direct WebFetch of the primary page over a WebSearch AI-summary when they conflict.
- **Good in-window hits this cycle, worth rechecking early next time:** parlance-labs.com/blog (Hamel), openai.com/index (launch/incident posts), forbes.com/councils/forbestechcouncil (op-ed surfacing vendor research), dtex.ai/resources (i³ threat advisories — a security vendor worth adding to the guardrails/HITL beat alongside CSA).
- **Confirmed low-signal again:** generic "AI agent guardrails/observability July 2026" WebSearch queries still return almost entirely SEO "20XX guide" content (atlan.com, montecarlo.ai, braintrust.dev/articles/* comparison pages, aimultiple.com) — continue to skip and go straight to named-source queries.
