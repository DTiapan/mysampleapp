import urllib.parse
import urllib
from bs4 import BeautifulSoup

url = "http://nytimes.com"

urls = [url] #stack of urls to scrape
visited = [url] # Historic records of URLS

while len(urls) > 0 :
    try:
        htmltext = urllib.urlopen(urls[0]).read()
    except:
        print (urls[0])
    soup = BeautifulSoup(htmltext)

    urls.pop(0)
    print (soup.findAll('a', href = True))
          
      




