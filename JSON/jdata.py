"""
    Working with GeoJSON Document
"""

jsdata = """{
    "type" : "Feature",
    "id" : "OpenLayers.Feature.Vectors_314",
    "properties" : {},
    "geometry" : {
        "type": "Point",
        "coordinates": [
            97.03125,
            39.7265625
        ]
    },
    "crs": {
        "type": "name",
        "properties": {
            "name": "urn.ogc:def:crs:OGC:1.3:CRS84"
            }
        }
    }"""
point = eval(jsdata)
print(point["geometry"])

"""Using json module"""
import json
print("\n",json.loads(jsdata))

pydata =  json.loads(jsdata)
print("\n",json.dumps(pydata))

print(json.dumps(pydata, indent=4))