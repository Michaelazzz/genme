import sys

from scripts.extract_word_count import get_word_count
from scripts.extract_structure import get_structure
from scripts.extract_format import get_format
from scripts.extract_references import get_reference_info, count_references
from scripts.extract_details import get_details
from scripts.generate_readme import write_readme

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <tex_file>")
        sys.exit(1)

    tex_file = sys.argv[1]
    
    word_count = get_word_count(tex_file)
    structure = get_structure(tex_file)
    format_info = get_format(tex_file)
    references = get_reference_info(tex_file)
    reference_count = count_references(tex_file)
    author, title = get_details(tex_file)

    write_readme(word_count, structure, format_info, references, reference_count, author, title)

if __name__ == "__main__":
    main()
