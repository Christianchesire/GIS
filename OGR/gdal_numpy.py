from osgeo import gdal_array

srcArray = gdal_array.LoadFile("SatImage.tif")
band1 = srcArray[0]
gdal_array.SaveArray(band1, "band1.jpg", format="JPEG")