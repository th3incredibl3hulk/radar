#!/bin/bash
# Install (or reinstall) the Radar weekly LaunchAgent — Monday 07:00 local.
# Re-run this after moving the radar/ directory; it regenerates the plist with
# the new absolute path and reloads it. Runs as your GUI user, so it inherits
# your Claude Code subscription login. (For API billing, add ANTHROPIC_API_KEY
# to the EnvironmentVariables block below.)
set -euo pipefail

LABEL="com.larryhau.radar.weekly"
RADAR_REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PLIST="${HOME}/Library/LaunchAgents/${LABEL}.plist"
UID_NUM="$(id -u)"

mkdir -p "${HOME}/Library/LaunchAgents"

cat > "${PLIST}" <<PLIST
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>${LABEL}</string>
    <key>ProgramArguments</key>
    <array>
        <string>/bin/bash</string>
        <string>${RADAR_REPO}/scripts/run-all.sh</string>
    </array>
    <key>StartCalendarInterval</key>
    <dict>
        <key>Weekday</key>
        <integer>1</integer>
        <key>Hour</key>
        <integer>7</integer>
        <key>Minute</key>
        <integer>0</integer>
    </dict>
    <key>EnvironmentVariables</key>
    <dict>
        <key>PATH</key>
        <string>/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin</string>
    </dict>
    <key>StandardOutPath</key>
    <string>${RADAR_REPO}/scripts/run.log</string>
    <key>StandardErrorPath</key>
    <string>${RADAR_REPO}/scripts/run.log</string>
    <key>RunAtLoad</key>
    <false/>
    <key>ProcessType</key>
    <string>Background</string>
</dict>
</plist>
PLIST

# Reload (modern launchctl: bootout the old, bootstrap the new).
launchctl bootout "gui/${UID_NUM}/${LABEL}" 2>/dev/null || true
launchctl bootstrap "gui/${UID_NUM}" "${PLIST}"
launchctl enable "gui/${UID_NUM}/${LABEL}"

echo "Installed ${LABEL}"
echo "  plist:    ${PLIST}"
echo "  runs:     Mondays 07:00 local (missed runs fire on next wake)"
echo "  script:   ${RADAR_REPO}/scripts/run-all.sh"
echo "  log:      ${RADAR_REPO}/scripts/run.log"
echo
echo "Test it now:   launchctl kickstart -k gui/${UID_NUM}/${LABEL}"
echo "Check status:  launchctl print gui/${UID_NUM}/${LABEL} | grep -E 'state|last exit'"
echo "Remove it:     ${RADAR_REPO}/scripts/uninstall-launchd.sh"
