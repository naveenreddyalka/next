#!/bin/bash
# Source this from other shell scripts: . "$(dirname "$0")/project_root.sh"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]:-$0}")" && pwd)"
export PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
export SCRIPTS_DIR="$PROJECT_ROOT/files/scripts"
