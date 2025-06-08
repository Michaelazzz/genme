# 📊 (Gen)erate (Me)trics

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
uses: Michaelazzz/genme@v1.2
with:
  tex_file: "main.tex"
