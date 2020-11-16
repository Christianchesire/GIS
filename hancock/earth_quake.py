"""
 Accessing the United States Geological Survey (USGS) earthquake feed

"""

import urllib.request
import urllib.parse
import urllib.error

url = "http://earthquake.us-gs.gov/eathquakes/feed/v1.0/summary/all_hour.csv"
earthquakes = urllib.request.urlopen(url)
earthquakes.readline()

for record in earthquakes:
    print(record)
