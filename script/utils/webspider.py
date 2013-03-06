#!/usr/bin/python

import mechanize
from bs4 import BeautifulSoup


BASE_URL = "http://www.utexas.edu/world/univ/alpha/"

def write_to_file(filename, buffer):
    fp = open(filename, 'w')
    fp.write(buffer)
    fp.close()

def get_webpage(url):
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
    
    data = br.open(url).get_data()
    return data

def scrape_links(url):
    """
    Scrape links pointing to articles pages
    """
    data = get_webpage(url)
    soup = BeautifulSoup(data)
    links=soup.findAll('a',{'class':'institution'})
    #links = soup.findAll('div', attrs={'class': 'list-authors'})
    print '''University------Web address'''
    count = 1
    for link in links:
        print str(count) + "." + link.get('href') + "  ------  " + link.text
        count += 1
        
        #print(link.get('href'))
    return links
    

#links = mechanize.  
#br = mechanize.Browser()
#data = br.open(BASE_URL).get_data()
#links = scrape_links(BASE_URL, data)

def main():
    """
    Get article network main page and follow the links
    to get the whole list of articles available
    """

    # Ouput is the list of titles and URLs for each article found
    print ("Starting spider")
    scrape_links(BASE_URL)

                        
if __name__ == "__main__":
    main()
