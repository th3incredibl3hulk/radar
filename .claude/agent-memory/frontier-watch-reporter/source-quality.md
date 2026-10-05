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

Update 2026-10-05 cycle (~$0.7 of $2 used): 6 parallel WebSearches then 2 WebFetch/4 WebSearch follow-ups sufficed. WebFetch of InfoQ worked well for DevDay; microcenter returned 403. Searching "<lab> news <date>" missed Sonnet 5.5 last cycle — a named-model query ("Claude Sonnet 5.5 launch") surfaced it; do a 'sibling model' query per lab (Sonnet/Haiku/Flash tiers). Beware third-party-hosted re-uploads (e.g. "luminal/DeepSeek-V4.1-Flash") masquerading as releases. Light-touch state-of-the-art refresh this cycle; do full section rewrite next cycle (landscape, capability frontiers, lab strategy).

Update 2026-09-28 cycle (also WebSearch-only, ~$1.7 of $2 budget used, did a fuller state-of-the-art refresh as planned above):
- Batching 6 WebSearch calls per message (one per lab) continues to be the most efficient pattern — each returns a synthesized multi-source answer plus a REMINDER-enforced Sources list, sufficient for report writing without a follow-up fetch in most cases.
- Direct searches for specific named events ("Dario Amodei Pace the Frontier essay", "OpenAI Anthropic UN Security Council briefing") surfaced far richer, more precise results than generic "<lab> news <date>" queries once a specific story name was known from an earlier broader search — worth doing a broad sweep first, then 1-2 follow-up targeted searches on anything that looks like it has more depth (a UN briefing, an essay, a named incident).
- AA Index tracking is now showing a real, unresolved naming ambiguity between "GPT-5.6 Sol" and "GPT-6 Sol" across third-party trackers vs. OpenAI's own announcements — flagged in this cycle's report/state-of-the-art rather than silently picking one; worth a direct artificialanalysis.ai check next cycle if budget allows.
- Still no landmark-paper hit via a single generic arXiv/"AI research breakthrough" search — this is now 3+ consecutive cycles of "nothing landmark," reinforcing last cycle's note that a lighter-touch single query is the right amount of effort here, not zero effort.
- Skipped this cycle: Cohere, Microsoft, NVIDIA direct sweeps (no time/budget); worth a periodic direct check even when they rarely produce news, per the general principle that per-lab sweeps catch things generic queries miss.
