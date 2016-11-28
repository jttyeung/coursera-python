import urllib
import xml.etree.ElementTree as ET

url = raw_input('Enter XML url: ')
data = urllib.urlopen(url).read()
tree = ET.fromstring(data)

counts = tree.findall('comments/comment/count')
sum = 0

for count in counts :
  sum = sum + int(count.text)

print sum
