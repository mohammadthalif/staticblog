OUT_DIR = "out"
IN_FILE = "test.md"
OUT_FILE = "test.html"

import sys
sys.path.append(".")
import markdown2

def convert():
    html = markdown2.markdown_path(IN_FILE)
    fp = open(OUT_FILE, 'w')
    fp.write(html)
    fp.close()
