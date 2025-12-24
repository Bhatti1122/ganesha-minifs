#!/usr/bin/env bash
set -euo pipefail
fio --name=smoke --filename=/mnt/nfsmini/fio.bin --size=64m \
    --bs=4k --iodepth=8 --rw=randrw --rwmixread=70 --time_based --runtime=30 --ioengine=psync
