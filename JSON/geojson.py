import geojson
from shapely.geometry import asShape

p = geojson.Point([-92, 37])
geojs = geojson.dumps(p, indent=4)
print(geojs)

point = asShape(p)
print(point.wkt)