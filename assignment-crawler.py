# import the urlopen function from the urllib2 module
from urllib2 import urlopen
# import the BeautifulSoup function from the bs4 module
from bs4 import BeautifulSoup
# import pprint to print things out in a pretty way
import pprint
# choose the url to crawl
url = 'http://www.codingdojo.com'
# get the result back with the BeautifulSoup crawler
item = BeautifulSoup(urlopen(url), "html.parser")
# print soup to see the result!!
# your code here to find all the links from the result
# and complete the challenges below
#I'm getting a error from this.
item = soup.findall('a')