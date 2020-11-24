import fiona
from pprint import pprint
f = fiona.open("GIS_CensusTract_poly.shp")
print(f.driver)

# Check coordinate refernce
f.crs

# Bounding box
f.bounds

# View data schema as geojson
pprint(f.schema)

# Count the number of features
len(f)
pprint(f[1])