---
name: source-notes
description: Which sources/search strategies proved most/least valuable for finding landmark research — use to prioritize search effort each cycle
metadata:
  type: reference
---

## High value

- **Direct Anthropic searches by topic** ("Anthropic research blog September 2026", "Anthropic [specific capability] capabilities") reliably surface multiple distinct posts with exact dates — Anthropic remains the single most prolific and highest-signal technical publisher across both alignment.anthropic.com and anthropic.com/research. Check both URLs, and also search for specific named eval/report titles once a lead surfaces.
- **arXiv ID search via title/keyword once a candidate is known** (e.g. searching a distinctive project codename) reliably surfaces exact arXiv ID, abstract, and scale details — worked again this cycle for NCP-ArchPreview (found via a generic "Hugging Face trending papers" search first, then confirmed via direct title search).
- **Hugging Face trending papers search** ("Hugging Face daily papers trending <month> <year> <topic>") is consistently good for surfacing the single top trending paper of the week even without knowing its name in advance — this is how NCP-ArchPreview was found. Worth running early in each cycle as a discovery step, not just a confirmation step.
- **article-summarizer agent** worked cleanly this cycle for pulling structured facts (dates, scale numbers, methodology, caveats) out of a long Anthropic research page without ingesting the full page into the main context. Use it for any single "must get exact numbers right" source rather than relying on WebSearch snippets alone.
- **Direct researcher-name + "date" checks confirm negatives cheaply.** Checking Karpathy, LeCun/AMI Labs, and Sutskever/SSI directly each cost one search and confirmed "still nothing new" with specific supporting facts (Karpathy's last talk was April; LeWorldModel is still the March arXiv ID; SSI's only news is a partnership) — cheap enough to do every cycle rather than skipping the check.

## Low value / noisy

- **BAIR blog** — confirmed again this cycle: web search returns nothing newer than July 2026 (Adaptive Parallel Reasoning, May 8; Gradient-based Planning, April 20). Two cycles in a row with no in-window BAIR result via search. Consider trying a direct WebFetch of bair.berkeley.edu/blog/ instead of WebSearch next cycle, since search may simply be under-indexing it.
- **Generic "arXiv landmark paper <month> new architecture" queries** — confirmed again this cycle: mostly return stale survey/interpretability-overview pages from earlier in the year, not in-window results. Always pivot to a specific project/codename search instead.
- **Watch for date confusion in search-summarized results.** One search claimed LeCun's LeWorldModel paper was "introduced in early September 2026," but the actual arXiv ID (2603.19312) submission-numbers to March 2026 — the September reference was likely a conference presentation or v2 update, not a new result. Always cross-check the arXiv ID's month prefix against the claimed publication date before treating something as in-window.
- **"Recent" framing in search snippets can mean weeks-old, not days-old.** The Anthropic protein-design/analytical-chemistry post surfaced in a "life scientists" search framed as current, but was actually published mid-August 2026 (confirmed via "X months ago" metadata) — outside this cycle's window. Always verify the actual publication date before including, even when a source frames it as recent.

## Gotchas

- OpenAI's openai.com/index/ pages still 403 the article-summarizer's fetch tool (unconfirmed this cycle, not retested, but assume still true). Rely on WebSearch snippets, or third-party technical coverage (e.g. Simon Willison's blog reliably summarizes OpenAI research posts in detail and is fetchable).
- Budget discipline: this cycle ran well within a ~$2 session budget using ~15 WebSearch calls + 1 article-summarizer dispatch + no other agent delegation. Direct WebSearch is cheap enough to be the default; reserve article-summarizer for the 1-2 sources where exact figures matter most (e.g. the headline story).
