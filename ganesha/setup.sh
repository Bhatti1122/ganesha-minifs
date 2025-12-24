#!/usr/bin/env bash
set -euo pipefail
sudo apt-get update
sudo apt-get install -y nfs-ganesha nfs-ganesha-vfs nfs-common python3-pytest fio fuse
sudo install -m 644 "$(dirname "$0")/ganesha.conf" /etc/ganesha/ganesha.conf
sudo install -m 644 "$(dirname "$0")/exports.conf" /etc/ganesha/exports.conf
sudo systemctl enable nfs-ganesha
sudo systemctl restart nfs-ganesha
echo "Ganesha ready."
