#!/bin/bash
# Regenerate all company index.html + company_info.html from source data.
# Runs automatically via LaunchAgent (see files/launchd/) or manually by an agent.

set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
# shellcheck source=project_root.sh
. "$SCRIPT_DIR/project_root.sh"
ROOT="$PROJECT_ROOT"
SCRIPTS="$SCRIPTS_DIR"
LOG="$ROOT/.refresh_company_pages.log"

{
  echo "=== $(date '+%Y-%m-%d %H:%M:%S %Z') refresh start ==="
  cd "$SCRIPTS"
  python3 update_latest_questions.py
  python3 build_company_pages_data.py
  python3 gen_company_index.py
  python3 gen_company_info.py
  echo "=== $(date '+%Y-%m-%d %H:%M:%S %Z') refresh done ==="
} >> "$LOG" 2>&1
