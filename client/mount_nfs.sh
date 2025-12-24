#!/usr/bin/env bash
set -euo pipefail
sudo mkdir -p /mnt/nfsmini
sudo mount -t nfs4 127.0.0.1:/export /mnt/nfsmini
mount | grep /mnt/nfsmini && echo "Mounted at /mnt/nfsmini"
