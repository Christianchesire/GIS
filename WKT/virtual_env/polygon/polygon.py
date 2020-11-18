import shapely.wkt
from osgeo import gdal
from osgeo import ogr

shape = ogr.Open("polygon.shp")
layer = shape.GetLayer()
feature = layer.GetNextFeature()
geom = feature.GetGeometryRef()
wkt = geom.ExportToWkt()
print(wkt)

poly = ogr.CreateGeometryFromWkt(wkt)
print(poly.GetEnvelope())