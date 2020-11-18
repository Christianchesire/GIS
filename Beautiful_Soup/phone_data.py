""""
We use GPS Exchange Format (GPX) tracking file from a smartphone
"""
from xml.dom import minidom
from bs4 import BeautifulSoup
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
"""
Different parsers face the same problem with mismatched tags
"""

# gpx = minidom.parse("broken_data.gpx")
# ET.ElementTree(file="broken_data.gpx")

# implementing beautiful soup
gpx = open("broken_data.gpx")
soup = BeautifulSoup(gpx.read(), features="xml")
# print(soup.trkpt), # beautiful soup turn tags into attributes of the parse tree
tracks = soup.findAll("trkpt")
print(len(tracks))

"""
Using prettify method to format the XML with nice indentation
"""
fixed = open("fixed_data.gpx", "w")
fixed.write(soup.prettify())
fixed.close()