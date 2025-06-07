def get_structure(tex_path: str) -> str:
  import re
  structure = []
  with open(tex_path) as f:
    for line in f:
      if '\\section{' in line:
        title = re.search(r'\\section{(.+?)}', line)
        if title:
          structure.append(f"- Section: {title.group(1)}")
      elif '\\subsection{' in line:
        title = re.search(r'\\subsection{(.+?)}', line)
        if title:
          structure.append(f"  - Subsection: {title.group(1)}")
  return "\n".join(structure)