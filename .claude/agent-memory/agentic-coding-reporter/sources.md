---
name: sources
description: Source quality notes from each reporting cycle — which sources delivered real signal vs. noise, to tune future searches.
metadata:
  type: reference
---

## From 2026-07-11 cycle (first run, no prior baseline)

**High signal, worth prioritizing again:**
- blog.modelcontextprotocol.io — primary source for MCP spec changes, detailed and dated.
- flatt.tech (GMO Flatt Security research blog) — original-source security research (Claude Code Action flaw), high technical detail.
- noma.security blog — original-source security research (GitLost).
- thehackernews.com — reliably fast aggregation of security disclosures; good for surfacing stories to then verify at the primary source.
- Sourcegraph's own blog (sourcegraph.com/blog) and Devin's own blog (devin.ai/blog) — primary source for business/product moves, get these directly rather than via secondary write-ups.
- simonwillison.net — as expected, best practical hands-on signal; check the `agentic-engineering` tag specifically.
- github.blog/changelog — primary source for Copilot, dated and specific, filter by month URL (`/changelog/month/07-2026/`).
- developers.openai.com/codex/changelog — primary source for Codex, good version-level detail.

**Useful but secondary/aggregator — cross-check before quoting figures:**
- releasebot.io — decent changelog aggregation across multiple vendors (Anthropic, OpenAI, GitHub, Windsurf) but is itself a secondary aggregator; use to find primary sources, not as the citation.
- codingfleet.com/blog and morphllm.com — benchmark leaderboard secondary aggregators; single-source risk, worth checking against swebench.com / swe-bench-live.github.io directly next cycle.
- Anthropic's own "2026 Agentic Coding Trends Report" (resources.anthropic.com) — primary source but vendor-authored; treat adoption percentages as marketing, not independent research.

**Noise / low priority:**
- Generic SEO/listicle blogs (digitalapplied.com, byteiota.com, etc.) turned up repeatedly in search results with overlapping rehashed content — fine as a secondary confirmation link but don't rely on them as the primary source when a company blog or original researcher post exists.

## Gaps to try next cycle
- Did not directly pull from Hacker News front page (used search-engine-mediated HN results instead) — consider fetching news.ycombinator.com directly for what's on the front page right at report time.
- Did not check Lobste.rs, r/LocalLLaMA, or r/ChatGPTCoding directly this cycle — relied on WebSearch aggregation. Worth a direct pass next time to catch anything WebSearch's ranking missed.
- Did not deep-dive Interconnects (Nathan Lambert) or The Batch (Andrew Ng) this cycle — no obviously relevant agentic-coding-specific posts surfaced in search, but worth a direct check next cycle rather than relying on search recall.
