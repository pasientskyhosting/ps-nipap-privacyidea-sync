#!/bin/sh

sed -i "s|{nipapurl}|$NIPAPURL|" /sync.py

exec cron -f
