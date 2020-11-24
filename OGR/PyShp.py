import shapefile


shp = shapefile.Reader("point.shp")
for feature in shp.shapeRecords():
    point = feature.shape.points[0]
    rec = feature.records[0]
    print(point[0], point[1], rec)