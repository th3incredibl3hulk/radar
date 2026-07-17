---
name: source-quality
description: Which sources/search tactics proved most and least valuable when researching frontier AI news, to speed up future runs
metadata:
  type: project
---

From the 2026-07-11 (first) report:

**High value:**
- Direct WebSearch queries per-lab ("<lab> new model release <month year>") surfaced primary lab blog posts (anthropic.com/news, x.ai/news, ai.meta.com/blog, mistral.ai/news) reliably and quickly — more efficient than trying to browse newsletter sites directly.
- TechCrunch, Axios, and Bloomberg consistently had the clearest first-party-adjacent reporting on release timing and pricing; good default secondary sources.
- WebFetch directly against anthropic.com/news worked well to disambiguate confusing model-naming (Fable vs. Mythos vs. Opus vs. Sonnet) — worth doing a direct fetch when naming is unclear rather than relying on search snippets.
- Artificial Analysis (artificialanalysis.ai) and SWE-bench.com / BenchLM.ai are the go-to benchmark aggregators for the "who's ahead" table — check these directly each cycle rather than searching generically for "AI benchmark."

**Lower value / caution:**
- Some "Gemini 3.5 Pro" spec details (2M context, Deep Think, pricing) are sourced only from leak/rumor accounts (X posts, "leaked" blog posts) — treat these as unconfirmed until Google's own post appears. Flagged explicitly in the 2026-07-11 report; verify on next run once the model actually ships (targeted July 17, 2026).
- Did not get direct access to newsletter-tier sources (Import AI, Interconnects, The Batch, SemiAnalysis, AInews/smol.ai) via search this run — search results surfaced mostly SEO/aggregator sites (releasebot.io, felloai.com, coursiv.io) rather than the actual newsletters. Consider WebFetch-ing these newsletter homepages/archives directly on future runs instead of relying on WebSearch to surface them.
- Meta's model naming/timeline is confusing (Avocado → absorbed into Muse Spark line under Meta Superintelligence Labs) — double check current naming each cycle before citing.

**Tactic that worked well:** running 4-5 parallel WebSearch calls per batch (one per lab/topic) rather than sequential single searches — much faster convergence on the two-week window's major stories.
