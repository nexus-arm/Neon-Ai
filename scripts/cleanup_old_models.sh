#!/usr/bin/env bash
# Lists model artifacts older than a given age. Add your own deletion/archival logic if desired.

set -euo pipefail

TARGET_DIR=${1:-models}
AGE_DAYS=${AGE_DAYS:-30}

if [ ! -d "$TARGET_DIR" ]; then
  echo "Directory '$TARGET_DIR' not found. Nothing to clean." >&2
  exit 0
fi

echo "Scanning '$TARGET_DIR' for files older than $AGE_DAYS days..."
find "$TARGET_DIR" -type f -mtime +"$AGE_DAYS" -print

echo "No files removed. Add deletion/archival steps once you confirm the matches above."
