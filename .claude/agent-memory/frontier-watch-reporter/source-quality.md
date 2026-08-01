---
name: source-quality
description: Which sources/search tactics proved most and least valuable when researching frontier AI news, to speed up future runs
metadata:
  type: project
---

From the 2026-07-11 (first) report, reconfirmed 2026-07-31:

**High value:**
- Direct WebSearch queries per-lab ("<lab> new model release <month year>") surfaced primary lab blog posts (anthropic.com/news, x.ai/news, ai.meta.com/blog, mistral.ai/news, blog.google, newsroom.amd.com) reliably and quickly.
- TechCrunch, CNBC, Bloomberg, and AMD/company newsroom press releases consistently had the clearest first-party-adjacent reporting on release timing, pricing, and deal terms (e.g. the AMD-Anthropic deal was best sourced directly from newsroom.amd.com).
- llm-stats.com, BenchLM.ai, and swebench.com are reliable benchmark-aggregator hits for "who's ahead" data (SWE-bench Verified/Pro/Lite splits) — check these directly each cycle.
- Digitalapplied.com's "wave tracker" style posts (e.g. the July 2026 open-weight wave roundup) were unusually good at synthesizing a multi-lab story (Kimi K3 + Inkling + Mistral + MiniMax) in one search hit — worth searching for "<topic> wave" or "<topic> tracker" style queries when multiple labs move at once.

**Lower value / caution:**
- Low-quality SEO aggregators (skycrumbs.com, coursiv.io, releasebot.io) sometimes synthesize claims (e.g. a "DeepMind prospective credit assignment paper") that could not be verified against any primary source on follow-up search — treat single-aggregator-sourced technical/research claims as unconfirmed until a primary source (arxiv.org, deepmind.google) is found. Dropped one such claim entirely in the 2026-07-31 report rather than report it with a hedge.
- Still did not get direct hits on newsletter-tier sources (Import AI, Interconnects, The Batch, SemiAnalysis, AInews/smol.ai) via generic WebSearch two cycles in a row — consider WebFetch-ing their homepages/archives directly next run instead of relying on search snippets to surface them.
- When a last report is >2 weeks old (as it was this cycle: 20 days), a strict "most recent 2 weeks only" window creates a coverage gap (here, 07-11 to 07-17) — resolved by backfilling only stories foundational to an in-window follow-on (Inkling/Kimi K3 origin dates, since their public-weights release was in-window). Worth deciding proactively next time a gap appears rather than re-deriving the judgment call.

**Tactic that worked well:** 5-6 parallel WebSearch calls per batch (one per lab/topic), across 3 batches total (labs → open-weight/capex/papers/benchmarks → compute deals/gov't status follow-ups) — converged on all major stories for a ~$1.5 total budget spend on a $2 cap. Papers/research searches remain the weakest link — two cycles running, generic "landmark paper" searches surface either nothing citable or low-quality aggregator synthesis; consider going directly to arxiv.org listing pages or Hugging Face Daily Papers next time instead of keyword search.
