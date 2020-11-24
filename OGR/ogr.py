import ogr


shp = ogr.Open("point.shp")
layer = shp.GetLayer()
for feature in layer:
    geometry = feature.GetGeometry()
    print(geometry.GetX(), geometry.GetY(), feature.GetField("FIRST_FLD"))