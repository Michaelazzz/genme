#!/bin/bash
set -e

TEX_FILE=${1:-main.tex}
echo "📂 Running LaTeX metrics on: $TEX_FILE"
python /app/main.py "$TEX_FILE"

echo "✅ Metrics extraction complete. README.md generated."
