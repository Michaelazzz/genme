def get_reference_info(tex_path: str) -> str:
  with open(tex_path) as f:
    content = f.read()
    if '\\bibliography{' in content or '\\addbibresource{' in content:
      if 'IEEEtran' in content:
        return 'Reference Style: IEEE'
      elif 'apalike' in content:
        return 'Reference Style: APA'
      elif 'biblatex' in content or '\\addbibresource{' in content:
        return 'Reference Style: biblatex'
      return 'Reference style used (unspecified)'
  return 'No references found'

def count_references(tex_path: str) -> int:
    import re
    count = 0
    citation_patterns = [
      r'\\cite{.*?}',
      r'\\citep{.*?}',
      r'\\citet{.*?}',
      r'\\autocite{.*?}',
      r'\\textcite{.*?}'
    ]
    with open(tex_path) as f:
      for line in f:
        for pattern in citation_patterns:
          count += len(re.findall(pattern, line))
    return count