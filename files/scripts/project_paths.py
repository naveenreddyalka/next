"""Canonical project root — works regardless of install location."""
from pathlib import Path

# files/scripts/project_paths.py -> project root is two levels up from files/
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
SCRIPTS_DIR = PROJECT_ROOT / "files" / "scripts"
FILES_DIR = PROJECT_ROOT / "files"
