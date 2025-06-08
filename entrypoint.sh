#!/bin/bash
set -e

TEX_FILE=${1:-main.tex}
echo "📂 Running LaTeX metrics on: $TEX_FILE"
python main.py "$TEX_FILE"

echo "Done! Results in README.md"
