---
name: source-quality
description: Which sources/search tactics proved most and least valuable for frontier-watch cycles
metadata:
  type: project
---

Most valuable this cycle (2026-09-21, WebSearch-only, no article-summarizer dispatch — budget was too tight to justify the extra Agent calls for a 4-day thin-news cycle):
- Direct per-lab WebSearch queries ("<lab> news September <date> 2026") reliably surfaced Bloomberg/Reuters/CNBC/TechCrunch/Axios coverage with usable synthesized snippets — often sufficient without a full-page fetch.
- Bloomberg and Reuters (via CNBC/Yahoo Finance mirrors) are the strongest sources for Anthropic financial/IPO and Meta market-reaction stories.
- aiweekly.co/ai-news-today/<lab>-news pages are a good single-stop lab-specific news aggregator — worth querying directly by URL pattern next time.
- Individual "quiet lab" sweeps (one query per lab even when nothing is expected) keep catching real signal — e.g., Meta's JPMorgan upgrade and Mistral's Samsung round both surfaced only because of a direct per-lab query, not a generic "AI news" query.

Weak/misleading this cycle:
- Generic "AI model news [date range] 2026" queries return mostly SEO-farm aggregator sites (llmgateway.io, llm-stats.com, geotoolbox.ai, cellcog.ai) with shallow or stale info — useful for a first pass/date-anchoring only, not as a citable primary source.
- Third-party benchmark scrapers (e.g., benchlm.ai) can show stale/conflicting Intelligence Index numbers vs. the actual Artificial Analysis site — always prefer artificialanalysis.ai's own articles/changelog over scraper mirrors when precision matters.
- arXiv/landmark-paper searches have returned "nothing landmark found" for several consecutive cycles now — consider this a real signal (no big papers, not a search gap) rather than re-running the same broad query every cycle; a lighter-touch check (one query) is enough.

Process note: this cycle ran under an explicit tight budget ($2 total for the session). Given that, WebSearch-only synthesis (no Agent/article-summarizer dispatch, no Bash) was the right tradeoff — cut research breadth (skipped hyperscaler-capex and OpenAI DevDay deep dives, skipped full re-verification of AA Index scraper discrepancy) rather than cutting report quality on the stories that were found. Next cycle, if budget allows, spend more on: (1) verifying the AA Index scraper discrepancy directly against artificialanalysis.ai, (2) DevDay 2026 once it happens, (3) a fuller state-of-the-art refresh (capability frontiers, lab strategy watch, trend tracker, predictions sections were only partially touched this cycle).
