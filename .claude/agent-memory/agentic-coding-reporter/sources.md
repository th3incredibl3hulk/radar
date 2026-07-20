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

## From 2026-07-20 cycle

**High signal, worth prioritizing again:**
- openai.com/index — primary source for OpenAI's SWE-Bench Pro credibility audit; OpenAI is now doing methodology-audit posts as a recurring content type (did the same for SWE-bench Verified in Feb 2026) — check this URL pattern specifically each cycle for benchmark-integrity news, not just model launches.
- code.claude.com/docs/en/whats-new — excellent primary source, structured as dated weekly digests with version-range tags (e.g. "Week 29, July 13-17, v2.1.207-212"). Much better signal-per-fetch than searching; fetch directly each cycle instead of relying on WebSearch summaries of it.
- andrewkelley.me (and other individual practitioner blogs surfaced via HN) — worth searching for by name once a controversy is flagged via aggregator search; primary-source rebuttals are more useful to cite than secondary write-ups of them.
- simonwillison.net — again the best hands-on signal; his Kimi K3 post was the clearest independent read on that model's coding capability.
- github.blog/changelog/month/07-2026/ — WebFetch on this URL directly (not WebSearch) returned clean, dated, specific entries. Prefer direct fetch over search for GitHub changelog going forward.

**Useful but secondary/aggregator — cross-check before quoting figures:**
- CNBC, TechCrunch, VentureBeat — reliable for dating major model launches (GPT-5.6, Kimi K3) precisely; use for date confirmation even when citing the primary lab blog for technical detail.
- usagebox.com, techtimes.com — picked up the Fable 5 billing-cutover specifics accurately and matched Anthropic's own help-center language; useful secondary confirmation for pricing/billing changes specifically.

**Noise / low priority:**
- Same generic SEO/listicle blogs as last cycle (digitalapplied.com, byteiota.com, explainx.ai, etc.) continue to show up heavily and rehash the same facts with no new reporting — keep treating as secondary-confirmation-only, never as the cited primary source.

## Gaps to try next cycle (updated)
- code.claude.com/docs/en/whats-new fetched cleanly this cycle via WebFetch — keep doing this directly rather than searching for Claude Code news.
- Still haven't done a direct Lobste.rs/Reddit pass — the HN-front-page angle worked well this cycle (found the Bun/Zig story and the SWE-Bench Pro thread) but Reddit/Lobsters remain unchecked.
- Consider checking x.ai/news and cognition.com/blog directly next cycle for SpaceXAI/Grok and Devin primary-source updates instead of relying on secondary aggregation — this cycle relied on secondary sources for both and found nothing new in-window, but a direct primary-source check would be more reliable than trusting "nothing new" from search results alone.
