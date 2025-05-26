import sys
from site_generator import generate_pages_recursive
from copy_directory_recursive import copy_directory_recursive

if __name__ == "__main__":
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    copy_directory_recursive("static", "docs")
    generate_pages_recursive("content", "template.html", "docs", basepath)