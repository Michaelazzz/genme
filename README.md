# 📊 (Gen)erate (Me)trics for Latex projects

[![Action Status](https://github.com/Michaelazzz/genme/actions/workflows/test.yml/badge.svg)](https://github.com/Michaelazzz/genme/actions)
[![Marketplace](https://img.shields.io/badge/GitHub%20Marketplace-LaTeX%20Metrics-blue?logo=github)](https://github.com/marketplace/actions/genme)
[![Version](https://img.shields.io/github/v/tag/your-username/genme?label=version)](https://github.com/Michaelazzz/genme/releases)


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
| `tex_file` | Path to your main `.tex` file | `project.tex`  |

## 🚀 Usage

```yaml
uses: Michaelazzz/genme@v1.2.2
with:
  tex_file: "main.tex"
