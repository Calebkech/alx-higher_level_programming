#!/bin/bash
# Get the byte size of the HTTP response header for a given URL.

# Usage: ./script.sh <URL>

# Use curl to fetch the URL and suppress output (-s).
# Pipe the output to wc to count characters (-c).
curl -s "$1" | wc -c
