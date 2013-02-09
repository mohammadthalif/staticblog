from urllib2 import Request, urlopen, URLError, HTTPError

def stealStuff(file_name,file_mode,base_url):
    #create the url and the request
    url = base_url + file_name
    req = Request(url)
        
    # Open the url
    try:
        f = urlopen(req)
        print "downloading " + url

        # Open our local file for writing
        local_file = open(file_name, "w" + file_mode)
        #Write to our local file
        local_file.write(f.read())
        local_file.close()
        #handle errors
    except HTTPError, e:
        print "HTTP Error:",e.code , url
    except URLError, e:
        print "URL Error:",e.reason , url

# download an image from a given link
def downloader():
    # Set the range of images to 1-50.It says 51 because the
    # range function never gets to the endpoint.
    image_range = range(1,51)

    # Iterate over image range
    for index in image_range:
        base_url = 'http://www.techniqal.com/'
        #create file name based on known pattern
        file_name =  str(index) + ".jpg"
        # Now download the image. If these were text files, 
        # or other ascii types, just pass an empty string 
        # for the second param ala stealStuff(file_name,'',base_url)
        stealStuff(file_name,"b",base_url)

import shutil
import os
import time
import datetime
import math
import urllib
from array import array
outfile = open("out.html", 'w')
filehandle = urllib.urlopen('http://www.mohammadthalif.wordpress.com')

for lines in filehandle.readlines():
    outfile.write(lines);
    
filehandle.close()
outfile.close()
