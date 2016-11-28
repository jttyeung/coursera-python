import json
import urllib

url = raw_input('Enter JSON url: ')
data = urllib.urlopen(url).read()
jsonData = json.loads(data)

comments = jsonData['comments']
sum = 0

for item in comments :
  sum = sum + item['count']

print sum
