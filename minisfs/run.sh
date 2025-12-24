#!/usr/bin/env bash
set -euo pipefail
MNT=/mnt/minifs
sudo mkdir -p "$MNT" /var/tmp/minifs_store
# run MiniFS in foreground (open a second terminal for other steps)
sudo -E python3 "$(dirname "$0")/minisfs.py" "$MNT"
