import urllib.request
import urllib.parse
import urllib.error
import zipfile
import io
import struct

url = "https://github.com/GeospatialPython/Learn/raw/master/hancock.zip"

cloudshape = urllib.request.urlopen(url)
memoryshape = io.BytesIO(cloudshape.read())
zipshape = zipfile.ZipFile(memoryshape)
cloudshp =  zipshape.read("hancock.shp")

# Access python string as an array
print(struct.unpack("<dddd", cloudshp[36:68]))
