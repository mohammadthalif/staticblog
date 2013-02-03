import sys
sys.path.append(".")
import markdown2
IN_FILE = "test.md"
OUT_FILE = "test.html"
html = markdown2.markdown_path(IN_FILE)
fp = open(OUT_FILE, 'w') 
fp.write(html)
fp.close()
