# 📊 (Gen)erate (Me)trics for LaTeX projects

[![Marketplace](https://img.shields.io/badge/GitHub%20Marketplace-Generate%20Metrics-blue?logo=github)](https://https://github.com/marketplace/actions/gen-erate-me-trics-for-latex-documents)
[![Version](https://img.shields.io/github/v/tag/your-username/genme?label=version)](https://github.com/Michaelazzz/genme/releases/tag/v1.2.1)


This GitHub Action analyzes a LaTeX project, collecting key metrics like:

- 📄 Word count
- 📚 Section structure
- 🎨 Formatting and packages
- 🔗 Reference style and citation count
- ✍️ Author and title

It generates a summary in the `README.md` of the LaTeX repo.

## 🔧 Inputs

| Name       | Description                   | Default        |
|------------|-------------------------------|----------------|
| `tex_file` | Path to your main `.tex` file | `main.tex`  |

## 🚀 Usage

```yaml
uses: Michaelazzz/genme@v1.2.2
with:
  tex_file: "main.tex"
