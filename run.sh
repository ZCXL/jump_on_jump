#!/bin/sh
while ((i<=100)); do
    sh screenshot.sh
    python touch.py
    sleep 3
done
