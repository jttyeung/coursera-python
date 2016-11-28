import urllib
from BeautifulSoup import *

url = raw_input('Enter url: ')
count = int(raw_input('Enter number of times to repeat: '))
position = int(raw_input('Enter position number: '))

links = list()

while count >= 0 :
  html = urllib.urlopen(url).read()
  formattedHtml = BeautifulSoup(html)
  tags = formattedHtml('a')
  for tag in tags :
    links.append(str(tag.get('href', None)))
  print 'Retrieving: ' + url
  # find the url at position - 1 offset for index starting at 0
  url = links[position-1]
  # refresh the links list to the new list of the next url
  del links[:]
  count = count - 1
