def write_readme(word_count, structure, format_info, references, reference_count, author, title):
  with open("README.md", "w") as f:
    f.write("# 📊 LaTeX Project Metrics\n\n")
    f.write("## 📜 Title & Author\n")
    f.write(f"- **Title**: {title}\n")
    f.write(f"- **Author**: {author}\n\n")

    f.write("## 📝 Word Count\n")
    f.write(f"{word_count} words\n\n")

    f.write("## 📚 Structure\n")
    f.write(structure + "\n\n")

    f.write("## 🧉 Formatting\n")
    f.write(format_info + "\n\n")

    f.write("## 🔗 References\n")
    f.write(references + "\n")
    f.write(f"- **Total citations used**: {reference_count}\n")