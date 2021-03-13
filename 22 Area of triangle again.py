#Area of triangle again (By Gheron's formula)
#Asking for lengths of tiangle a,b and c.
a = float(input("Enter the length of side 1 = "))
b = float(input('Enter the length of side 2 = '))
c = float(input('Enter the length of side 3 = '))
s = (a + b + c)/2
import math
print('Area of triangle is =',math.sqrt(s * (s - a) * (s - b) * (s - c)),"sq.m")
