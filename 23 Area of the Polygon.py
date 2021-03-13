#Area of regular Polygon.
#Asking values of length of side(s) and Number of sides (n)
s = float(input('Enter the length of side of polygon = '))
n = float(input('Enter number of sides = '))
import math
print('Area of the Polygon = ', (n * (s ** 2)) / (4 * math.tan((math.pi / n ))),' sq.m')
