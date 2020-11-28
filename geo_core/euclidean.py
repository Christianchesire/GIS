""" Pythagorean theorem  a**2 + b**2 = c**2 """
import math
# First point
x1 = 456456.23
y1 = 1279721.064
# Second point
x2 = 576628.34
y2 = 1071740.33
# X distance
x_dist = x1 - x2
# Y distance
y_dist = y1 -y2
# Pythagorean theorem
dist_sq = x_dist**2 + y_dist**2
distance = math.sqrt(dist_sq)
print("Shows distance in meters",distance)
