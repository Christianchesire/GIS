from area import area

# Out points making up the polygon
polygon = {"type":"Polygon","coordinates":
           [[[-89.324, 30.312], [-89.326, 30.31],
             [-89.322, 30.31], [-89.321, 30.311],
             [-89.321, 30.312], [-89.324, 30.312]]]}

a = area(polygon)
a = round(a, 2)
print(a)
# prints 80235.139 square meters