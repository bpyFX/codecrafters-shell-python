#!/bin/sh

# Use this script to run the shell locally.
# Note: Changing this script WILL NOT affect how Codecrafters runs your program.

set -e  # Exit early if any commands fail

# Copied from .codecrafters/run.sh

# Edit this to change how your program runs locally
# Execute the Python entry point with $@ args, forwarding any arguments
exec python3 -u app/main.py "$@"
