#!/bin/bash
# Get the response body for a given URL for 200 status code responses.

# Usage: ./script.sh <URL>

# Use curl to fetch the URL and follow redirects (-L).
# Suppress progress meter and output (-s).
curl -sL "$1"
