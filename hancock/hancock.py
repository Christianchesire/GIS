"""
  Downloading a zip file using urlib

"""

import urllib.request
import urllib.parse
import urllib.error
url = "https://github.com/GeospatialPython/Learn/raw/master/hancock.zip"
fileName = "hancock.zip"
urllib.request.urlretrieve(url,fileName)

