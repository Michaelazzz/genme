def get_format(tex_path: str) -> str:
  import re
  lines = open(tex_path).readlines()
  doc_class = next((re.search(r'\\documentclass\[?(.*?)\]?{(.*?)}', l) for l in lines if '\\documentclass' in l), None)
  pkgs = [re.search(r'\\usepackage(?:\[.*?\])?{(.*?)}', l) for l in lines if '\\usepackage' in l]
  doc_info = f"- Document Class: `{doc_class.group(2)}`\n- Options: `{doc_class.group(1)}`" if doc_class else "Unknown"
  packages = [pkg.group(1) for pkg in pkgs if pkg]
  return f"{doc_info}\n- Packages: {', '.join(packages)}"