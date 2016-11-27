import urllib
from BeautifulSoup import *

url = raw_input('Enter url: ')
html = urllib.urlopen(url).read()
reformattedHtml = BeautifulSoup(html)

tags = reformattedHtml('span')
sum = 0

for tag in tags:

  # output is [u'50'] (u for unicode) instead of just the number 50. [0] removes the 'u'
  sum = sum + int(tag.contents[0])
print sum
