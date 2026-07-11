# Shared News Reporter Template

This template defines the common output format, quality standards, and workflow for all Radar news-reporter agents. Domain agents reference this template and override only what differs (topic, sources, tags, state-of-the-art structure).

**Output format is Markdown (GitHub-Flavored).** Not org-mode.

## News Report Format

Every news report follows this structure:

```markdown
---
title: TOPIC News Report — YYYY-MM-DD
date: YYYY-MM-DD
author: AGENT_NAME
tags: [topic1, topic2, news]
---

# TOPIC News Report — YYYY-MM-DD

## Executive Summary

2–3 paragraph overview of the most significant developments this period.
Lead with the biggest story, note emerging patterns, and flag anything that
needs the reader's attention or a decision. Written for a busy VP: signal first.

## Headline of the first story

`tag1` `tag2` `tag3` · **Source:** [Primary source name](https://example.com) · *Found: YYYY-MM-DD*

2–5 lines that capture what happened, why it matters, and its relevance. State
the fact, then the significance. Separate reporting from opinion.

**More:** [Source name](https://example.com) · [Source name](https://example.com)

## Headline of the second story

`tag1` `tag2` · **Source:** [Primary source name](https://example.com) · *Found: YYYY-MM-DD*

Summary text here.
```

### Format Rules

1. **YAML frontmatter is mandatory** — `title`, `date`, `author`, `tags`.
2. **Executive Summary is mandatory** — every report opens with a 2–3 paragraph narrative.
3. **Each entry is an `##` heading** — the headline.
4. **Metadata strip** — directly under each headline, one line: backtick-wrapped tags, then `· **Source:** [name](url)`, then `· *Found: YYYY-MM-DD*`. The Source is the single most authoritative URL.
5. **Secondary sources** — a `**More:**` line after the summary, ` · `-separated Markdown links. Real links, never bare URLs.
6. **2–5 tags per entry** from the domain taxonomy.
7. **2–5 line summaries** — concise but informative.
8. **Tables use GFM pipe syntax** — for trackers, pipelines, and signal tables.

## Workflow

### Step 1: Determine the Last Report Date

Check the domain's report directory for existing `*-news-*.md` files. Find the most recent date. **Do not search for news older than the last report date.** If no prior reports exist, cover the last 2 weeks. If the last report is older than 2 weeks, cover only the most recent 2 weeks.

### Step 2: Search for Recent News

Use the domain-specific sources and search terms. The source lists are tiered on purpose:

- **Newsletter tier** — curated digests that already scrape X / Discord / Reddit for you. This is how you get the leading edge without an X account. Weight heavily.
- **Primary tier** — company/lab blogs, official release notes, first-party announcements. The source of record.
- **Filter tier** — Hacker News, Reddit, Lobsters. Use these to confirm what *broke through* to the mainstream, **not** as the leading edge. They lag and are dev-biased.

Always search multiple tiers for broad coverage.

### Step 3: Generate the News Report

Write the report file using the format above. Include 5–15 entries depending on news volume. Order entries by significance, not chronology.

### Step 4: Update the State-of-the-Art Summary

Update the domain's living state-of-the-art document. Preserve its structure; refresh the content. Always append a changelog entry noting what changed this cycle.

### Step 5: Update Agent Memory

Record the last report date (critical for deduplication), stories covered, and any continuity state (tracker readings, predictions). See the domain agent's memory section.

## Quality Standards

- **Every entry MUST have a source link.** No unsourced claims.
- **Secondary sources MUST be Markdown links** — `[text](url)`, never bare URLs.
- **Dates in ISO 8601** — `YYYY-MM-DD`, consistently.
- **No duplicate coverage** — if a story ran in a previous report, skip it.
- **Distinguish fact from opinion** — separate what happened from what people think about it.
- **Capture contrarian views** — don't just report the hype; include the skeptics.
- **Assess significance** — not everything matters equally. Help the reader prioritize.
- **Signal density** — this is read by a VP. Cut filler. Every line earns its place.

## Edge Cases

- **No new news found**: Write a brief report noting this. Don't update the state-of-the-art unless corrections are needed.
- **Ambiguous relevance**: When in doubt, include with a note on the tangential connection.
- **Paywalled sources**: Note the paywall. Summarize from what's available (abstract, discussion, coverage).
- **Conflicting information**: Note the discrepancy; assess which source is stronger.
