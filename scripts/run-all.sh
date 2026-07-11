#!/bin/bash
# Radar — run all reporter agents and regenerate the weekly digest.
# Wire to cron (see README). Runs each agent headless with a cost cap.
set -euo pipefail

CLAUDE="${CLAUDE_BIN:-/opt/homebrew/bin/claude}"
REPO="${RADAR_REPO:-$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)}"
MODEL="${RADAR_MODEL:-sonnet}"
BUDGET="${RADAR_BUDGET_USD:-1.50}"
TODAY="$(date +%Y-%m-%d)"

AGENTS=(
  frontier-watch-reporter
  agentic-coding-reporter
  production-ai-eng-reporter
  ai-economics-reporter
)

cd "${REPO}"

for agent in "${AGENTS[@]}"; do
  echo "==> ${agent} (${TODAY})"
  "${CLAUDE}" --agent "${agent}" \
    --model "${MODEL}" \
    --max-budget-usd "${BUDGET}" \
    --allowedTools "WebSearch" "WebFetch" "Read" "Write" "Edit" "Glob" "Grep" \
    --print \
    -p "Generate today's report. Today is ${TODAY}." \
    || echo "!! ${agent} failed — continuing"
done

# Regenerate the weekly digest: an index linking the newest report + state-of-the-art per domain.
DIGEST="${REPO}/reports/weekly-digest.md"
{
  echo "# Radar — Weekly Digest (${TODAY})"
  echo
  echo "One place to start. Newest delta report and standing briefing per domain."
  echo
  for dir in frontier-watch agentic-coding production-ai-eng ai-economics; do
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
