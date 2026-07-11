#!/bin/bash
# Remove the Radar weekly LaunchAgent.
set -euo pipefail

LABEL="com.larryhau.radar.weekly"
PLIST="${HOME}/Library/LaunchAgents/${LABEL}.plist"
UID_NUM="$(id -u)"

launchctl bootout "gui/${UID_NUM}/${LABEL}" 2>/dev/null || true
rm -f "${PLIST}"
echo "Removed ${LABEL} (${PLIST})"
