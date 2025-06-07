def get_word_count(tex_path: str) -> int:
  import subprocess
  try:
    output = subprocess.check_output(["texcount", "-1", tex_path], universal_newlines=True)
    return int(output.strip())
  except Exception:
    return -1