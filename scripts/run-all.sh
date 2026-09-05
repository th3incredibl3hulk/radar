#!/bin/bash
# Radar — run all reporter agents and regenerate the weekly digest.
# Wire to cron (see README). Runs each agent headless with a cost cap.
set -euo pipefail

CLAUDE="${CLAUDE_BIN:-$(command -v claude || echo /opt/homebrew/bin/claude)}"
REPO="${RADAR_REPO:-$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)}"
MODEL="${RADAR_MODEL:-sonnet}"
BUDGET="${RADAR_BUDGET_USD:-2.00}"
TODAY="$(date +%Y-%m-%d)"

# Preflight: don't burn a scheduled run against a dead network (e.g. mid-travel).
# Retry for a few minutes since connectivity often comes back quickly (wifi handshake, landed plane, etc).
NETWORK_CHECK_ATTEMPTS=10
NETWORK_CHECK_DELAY=30
network_up() {
  curl -fsS --max-time 5 https://api.anthropic.com > /dev/null 2>&1
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
  if "${CLAUDE}" --agent "${agent}" \
    --model "${MODEL}" \
    --max-budget-usd "${BUDGET}" \
    --allowedTools "WebSearch" "WebFetch" "Read" "Write" "Edit" "Glob" "Grep" "Agent(article-summarizer)" \
    --print \
    -p "Generate today's report. Today is ${TODAY}."
  then
    SUCCESS_COUNT=$((SUCCESS_COUNT + 1))
  else
    FAIL_COUNT=$((FAIL_COUNT + 1))
    echo "!! ${agent} failed — continuing"
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
git add reports/
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
