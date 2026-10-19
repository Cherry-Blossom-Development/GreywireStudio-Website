#!/usr/bin/env bash
# Copies the site to the EC2 server, replacing what's in /var/www/greywirestudio.com.
# Run from Git Bash in this folder: ./deploy.sh
set -euo pipefail

SERVER=ec2-user@44.225.148.34
KEY=~/.ssh/Hostgator-Key-1.pem
WEBROOT=/var/www/greywirestudio.com

cd "$(dirname "$0")"

# Only the files the site serves; the README, this script and git stay behind
tar -czf - ./*.html css img \
  | ssh -i "$KEY" "$SERVER" "find $WEBROOT -mindepth 1 -delete && tar -xzf - -C $WEBROOT"

echo "Deployed to https://greywirestudio.com"
