#!/bin/bash
# One-time setup: install weekly auto-refresh for company HTML pages.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
# shellcheck source=project_root.sh
. "$SCRIPT_DIR/project_root.sh"

PLIST_SRC="$PROJECT_ROOT/files/launchd/com.naveen.next.refresh-company-pages.plist"
PLIST_DST="$HOME/Library/LaunchAgents/com.naveen.next.refresh-company-pages.plist"
REFRESH="$SCRIPTS_DIR/refresh_company_pages.sh"
LOG="$PROJECT_ROOT/.refresh_company_pages.log"

# Regenerate plist with current project path
mkdir -p "$PROJECT_ROOT/files/launchd"
cat > "$PLIST_SRC" <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key>
  <string>com.naveen.next.refresh-company-pages</string>
  <key>ProgramArguments</key>
  <array>
    <string>/bin/bash</string>
    <string>$REFRESH</string>
  </array>
  <key>StartCalendarInterval</key>
  <dict>
    <key>Weekday</key>
    <integer>0</integer>
    <key>Hour</key>
    <integer>9</integer>
    <key>Minute</key>
    <integer>0</integer>
  </dict>
  <key>RunAtLoad</key>
  <true/>
  <key>StandardOutPath</key>
  <string>$LOG</string>
  <key>StandardErrorPath</key>
  <string>$LOG</string>
</dict>
</plist>
EOF

chmod +x "$REFRESH"
chmod +x "$SCRIPT_DIR/install_refresh_schedule.sh"

mkdir -p "$HOME/Library/LaunchAgents"
cp "$PLIST_SRC" "$PLIST_DST"

# Unload if already loaded, then load fresh
launchctl bootout "gui/$(id -u)/com.naveen.next.refresh-company-pages" 2>/dev/null || true
launchctl bootstrap "gui/$(id -u)" "$PLIST_DST"

echo "Installed: com.naveen.next.refresh-company-pages"
echo "Schedule: every Sunday 9:00 AM + once now (RunAtLoad)"
echo "Log: $LOG"
echo "Project root: $PROJECT_ROOT"
echo "Source data (edit these, HTML rebuilds automatically):"
echo "  $SCRIPTS_DIR/company_extra_data.py"
echo "  $SCRIPTS_DIR/build_company_pages_data.py (applications + base company rows)"
