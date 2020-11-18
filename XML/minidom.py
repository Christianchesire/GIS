from xml.dom import minidom

kml = minidom.parse("time-stamp-point.kml")
Placemarks = kml.getElementsByTagName("Placemark")

# print(len(Placemarks))
print(Placemarks[0].toxml())

coordinates = Placemarks[0].getElementsByTagName("coordinates")
point = coordinates[0].firstChild.data
print(point)

# Converting the resulting strings into python
x, y, z = point.split(",")
print("\nx:", x, "\ny:", y, "\nz:", z)

x, y, z = [float(c) for c in point.split(",")]
print(x, y, z)
