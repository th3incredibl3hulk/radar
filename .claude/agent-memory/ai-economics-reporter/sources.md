---
name: sources
description: Source performance notes — updated 2026-09-05
metadata:
  type: reference
---

## Delivered well this cycle
- Direct WebSearch for primary press releases (e.g. `"NVIDIA" second quarter fiscal 2027 financial results press release`) resolved conflicting secondary-aggregator figures reliably — go straight to the company's own newsroom/investor-relations naming convention when aggregators disagree, rather than trying more aggregator queries.
- BLS-specific searches ("BLS database occupations AI exposure 2026 release", "BLS jobs report August 2026") surfaced genuinely primary, dated releases directly — BLS remains the most reliable Tier-1 channel in this report's source list.
- Challenger's own site (wp-content/uploads/YYYY/MM/ URL pattern) is a reliable way to spot-check whether a "Challenger Report" search hit is the current month's primary PDF or a recycled older one — check the URL path date, not just the article date.

## Underperformed / need better queries next cycle
- article-summarizer hit 403 on CNBC this cycle (in addition to prior 403s on Dataconomy, Washington Post, Bloomberg) — CNBC earnings-live-blog pages appear to be bot-blocked. For earnings data, go directly to the company's newsroom/IR press release via WebSearch rather than dispatching article-summarizer to CNBC.
- Named-economist searches (Autor, Restrepo, Syverson, Rock, Brynjolfsson + "2026") continue to surface mostly already-covered or older work — confirmed structurally quiet channel across 3+ cycles now. Recommend checking monthly rather than every cycle going forward to conserve budget.
- BofA Global Fund Manager Survey results are scattered across many secondary aggregators (Seeking Alpha, Investing.com, Trustnet, Fortune) reporting different months' data under similar headlines — always check the article's stated survey period (e.g., "conducted July 2-9") against the publish date before citing, since old FMS results get recycled in later coverage.
