OUT_DIR = "out"
TEST_DIR = "test"
IN_FILE = "test_2.md"
OUT_FILE = "test_2.html"

import sys
import os
sys.path.append(".")
import markdown2

def convert():
    print "Converting"
    in_file = TEST_DIR + "/" + IN_FILE
    out_file = OUT_DIR + "/" + OUT_FILE
    html = markdown2.markdown_path(in_file)
    fp = open(out_file, 'w')
    fp.write(html)
    fp.close()

def create_dir():
    if not os.path.exists(OUT_DIR):
        os.makedirs (OUT_DIR);
    

create_dir();
convert();
