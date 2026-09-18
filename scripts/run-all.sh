#!/bin/bash
# Radar — run all reporter agents and regenerate the weekly digest.
# Wire to cron (see README). Runs each agent headless with a cost cap.
set -euo pipefail

CLAUDE="${CLAUDE_BIN:-$(command -v claude || echo /opt/homebrew/bin/claude)}"
REPO="${RADAR_REPO:-$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)}"
MODEL="${RADAR_MODEL:-sonnet}"
BUDGET="${RADAR_BUDGET_USD:-2.00}"
TODAY="$(date +%Y-%m-%d)"

# In --print mode the agent delegates the report to a background task, and print
# mode kills anything still running when this ceiling expires. The 600s default
# silently decapitated frontier-watch on 2026-09-14 (a full run takes ~13min).
# Deliberately a large bound rather than 0/unlimited, so a genuinely hung agent
# can't stall the whole weekly run forever.
export CLAUDE_CODE_PRINT_BG_WAIT_CEILING_MS="${RADAR_BG_WAIT_CEILING_MS:-1800000}"

# Preflight: don't burn a scheduled run against a dead network (e.g. mid-travel).
# Retry for a few minutes since connectivity often comes back quickly (wifi handshake, landed plane, etc).
NETWORK_CHECK_ATTEMPTS=10
NETWORK_CHECK_DELAY=30
network_up() {
  # Note: no -f — api.anthropic.com's bare root path 404s even when reachable.
  # We only care that the TCP/TLS/HTTP round-trip completed at all.
  curl -sS --max-time 5 https://api.anthropic.com -o /dev/null 2>&1
}
attempt=1
until network_up; do
  if [ "${attempt}" -ge "${NETWORK_CHECK_ATTEMPTS}" ]; then
    echo "!! No network after ${NETWORK_CHECK_ATTEMPTS} attempts (${TODAY}) — skipping this run entirely, no commit."
    exit 1
  fi
  echo "==> Network unreachable, retrying (${attempt}/${NETWORK_CHECK_ATTEMPTS})..."
  attempt=$((attempt + 1))
  sleep "${NETWORK_CHECK_DELAY}"
done

SUCCESS_COUNT=0
FAIL_COUNT=0

AGENTS=(
  frontier-watch-reporter
  agentic-coding-reporter
  production-ai-eng-reporter
  ai-economics-reporter
)

# Research pulse runs bi-weekly (every other week)
WEEK_NUM=$(date +%V)  # ISO week number
if [ $((WEEK_NUM % 2)) -eq 0 ]; then
  AGENTS+=(research-pulse-reporter)
fi

cd "${REPO}"

for agent in "${AGENTS[@]}"; do
  echo "==> ${agent} (${TODAY})"

  # frontier-watch-reporter -> reports/frontier-watch/frontier-watch-news-<date>.md
  domain="${agent%-reporter}"
  expected="${REPO}/reports/${domain}/${domain}-news-${TODAY}.md"

  if ! "${CLAUDE}" --agent "${agent}" \
    --model "${MODEL}" \
    --max-budget-usd "${BUDGET}" \
    --allowedTools "WebSearch" "WebFetch" "Read" "Write" "Edit" "Glob" "Grep" "Agent(article-summarizer)" \
    --print \
    -p "Generate today's report. Today is ${TODAY}."
  then
    FAIL_COUNT=$((FAIL_COUNT + 1))
    echo "!! ${agent} exited nonzero — continuing"
  elif [ ! -f "${expected}" ]; then
    # Exit 0 is not proof of work: a background-wait kill leaves the status clean
    # but writes nothing, which is how 2026-09-14 got committed with a hole in it.
    FAIL_COUNT=$((FAIL_COUNT + 1))
    echo "!! ${agent} exited clean but wrote no ${domain}-news-${TODAY}.md — counting as failed"
  else
    SUCCESS_COUNT=$((SUCCESS_COUNT + 1))
  fi
done

if [ "${SUCCESS_COUNT}" -eq 0 ]; then
  echo "!! All ${FAIL_COUNT} agent(s) failed (${TODAY}) — skipping digest regeneration and commit."
  exit 1
fi

# Regenerate the weekly digest: an index linking the newest report + state-of-the-art per domain.
DIGEST="${REPO}/reports/weekly-digest.md"
{
  echo "# Radar — Weekly Digest (${TODAY})"
  echo
  echo "One place to start. Newest delta report and standing briefing per domain."
  echo
  for dir in frontier-watch agentic-coding production-ai-eng ai-economics research-pulse; do
    name="$(echo "${dir}" | tr '-' ' ')"
    latest="$(ls -1 "${REPO}/reports/${dir}"/*-news-*.md 2>/dev/null | sort | tail -n1 || true)"
    sota="${REPO}/reports/${dir}/${dir}-state-of-the-art.md"
    echo "## ${name}"
    if [[ -n "${latest}" ]]; then
      echo "- Latest report: [$(basename "${latest}")](${dir}/$(basename "${latest}"))"
    else
      echo "- Latest report: _none yet_"
    fi
    if [[ -f "${sota}" ]]; then
      echo "- State of the art: [${dir}-state-of-the-art.md](${dir}/${dir}-state-of-the-art.md)"
    fi
    echo
  done
} > "${DIGEST}"

echo "==> Digest written to ${DIGEST}"

# Push this run's reports to GitHub so they're readable/retained there.
# Agent memory goes too: it's each reporter's dedup log, so losing it means the
# next cycle re-reports old news. Previously only reports/ was staged, leaving
# every agent's memory local-only and one `git clean` from gone.
git add reports/ .claude/agent-memory/
if git diff --cached --quiet; then
  echo "==> No report changes to commit"
else
  if [ "${FAIL_COUNT}" -gt 0 ]; then
    git commit -m "Radar: reports for ${TODAY} (${SUCCESS_COUNT} ok, ${FAIL_COUNT} failed)"
  else
    git commit -m "Radar: reports for ${TODAY}"
  fi

  PUSH_ATTEMPTS=5
  PUSH_DELAY=30
  attempt=1
  until git push origin HEAD; do
    if [ "${attempt}" -ge "${PUSH_ATTEMPTS}" ]; then
      echo "!! git push failed after ${PUSH_ATTEMPTS} attempts — changes committed locally only, push manually"
      break
    fi
    echo "==> git push failed, retrying (${attempt}/${PUSH_ATTEMPTS})..."
    attempt=$((attempt + 1))
    sleep "${PUSH_DELAY}"
  done
fi
