---
name: source-quality
description: Which sources and tactics worked for frontier-watch
metadata:
  type: project
---

2026-10-26 findings:
- WebFetch https://www.anthropic.com/news works and lists dated posts (best primary check). openai.com/news returns 403.
- news.smol.ai redirects to https://latent.space/news/ — fetching it gives a dated headline list per day (headlines only, no bodies). Best leading-edge index found; verify each headline with a follow-up search (Kimi 3.1 Pro and 722-math-papers did not verify).
- Search snippets: letsdatascience.com, decrypt, techcrunch, ppc.land useful; orcarouter/af.net/aitoolly/manifold are low quality — cross-check.
- Generic "this week" queries return mostly trackers; named-story queries work much better.
- Budget: a full run cost ~$0.65 with ~14 searches and 5 fetches.
