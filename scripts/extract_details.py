def get_details(tex_path: str) -> tuple[str, str]:
  import re
  author = title = "Unknown"
  with open(tex_path) as f:
    for line in f:
      if '\\author{' in line:
        m = re.search(r'\\author{(.+?)}', line)
        if m: author = m.group(1)
      if '\\title{' in line:
        m = re.search(r'\\title{(.+?)}', line)
        if m: title = m.group(1)
  return author, title