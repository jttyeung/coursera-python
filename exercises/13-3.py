import urllib
import json

api = 'http://python-data.dr-chuck.net/geojson?'

while True:
  location = raw_input('Enter a location: ')
  if len(location) < 1 : break

  url = api + urllib.urlencode({'sensor':'false', 'address': location})
  print 'Retreiving', url
  data = urllib.urlopen(url).read()
  print 'Retrieved ',len(data),' characters'

  # try/except filters for bad data that can't be deserialized
  # json.loads creates a dictionary (object) of the data
  try: js = json.loads(str(data))
  except: js = None
  if 'status' not in js or js['status'] != 'OK' :
    print 'Failed to Retrieve'
    print data
    continue

  # json.dumps takes an object and creates a string
  # indent = 4 indents lines by 4 to prettify data
  print json.dumps(js, indent = 4)

  placeid = js['results'][0]['place_id']
  print 'Place ID', placeid
