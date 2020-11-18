from shapely.wkt import dumps, loads
wktPoly = "POLYGON((0 0,4 0,4 4,0 4,0 0), (1 1, 2 1, 2 2, 1 2, 1 1))"
poly = shapely.wkt.loads(wktPoly)
poly.area