#!/bin/bash
set -e

echo "Running LaTeX metrics generator..."
python main.py

echo "Done! Results in README.md"
