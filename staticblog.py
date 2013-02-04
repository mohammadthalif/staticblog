OUT_DIR = "out"
TEST_DIR = "test"
IN_FILE = "test_2.md"
OUT_FILE = "test_2.html"
HEADER = "site/common/header.ht"
FOOTER = "site/common/footer.ht"


import sys
import os
sys.path.append(".")
import markdown2

def read_file(filename):
    fp = open(filename, 'r')
    data = fp.read()
    fp.close()
    return data

def write_file(filename, data):
    if os.path.exists(filename):
        try:
            os.remove(filename)
        except:
            print "Exception: ",str(sys.exc_info())
    print "Creating file :", filename
    fp = open(filename, 'a')
    fp.write(data)
    fp.close()

    
def convert():
    print "Converting"
    in_file = TEST_DIR + "/" + IN_FILE
    out_file = OUT_DIR + "/" + OUT_FILE
    html = markdown2.markdown_path(in_file)
    header = read_file(HEADER)
    footer = read_file(FOOTER)
    write_file(out_file, header + html + footer)
    #write_file(out_file, html)
    #write_file(out_file, footer)
    

def create_dir():
    if not os.path.exists(OUT_DIR):
        os.makedirs (OUT_DIR);
    

create_dir();
convert();
