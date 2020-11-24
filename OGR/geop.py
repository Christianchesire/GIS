import geopandas
import matplotlib.pyplot as plt
gdf = geopandas.GeoDataFrame
census = gdf.from_file("GIS_CensusTract_poly.shp")
census.plot()
plt.show()