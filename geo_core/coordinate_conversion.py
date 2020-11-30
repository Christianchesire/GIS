"""Convert point coordinate between different coordinate system"""

import utm
y = 479747.0453210057
x = 5377685.825323031
zone = 32
band = 'U'
print(utm.to_latlon(y, x, zone, band))

print(utm.from_latlon(48.55199390882121, 8.7255557290717631))