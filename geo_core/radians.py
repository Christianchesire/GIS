"""Converting distance to radians"""
import math
x1 = -90.21
y1 = 32.31
x2 = -88.95
y2 = 30.43
x_dist = math.radians(x1 - x2)
y_dist = math.radians(y1 - y2)
dist_sq = x_dist**2 + y_dist**2
dist_rad = math.sqrt(dist_sq)
dist_rad = dist_rad * 6371251.46
print("Shows distance in radians", dist_rad)
# 251664.4668769659