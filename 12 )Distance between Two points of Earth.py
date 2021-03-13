#12 Dsitance  between two points of Earth
#Ask for (t1,g1) and (t2,g2)
t1 = float(input('Enter value of t1 ='))
t2 = float(input('Enter value of t2 ='))
g1 = float(input("Enter value of g1 ="))
g2 = float(input('Enter value of g2 ='))
import math
x = math.sin(t1)
y = math.asin(t2)
z = math.acos(t1)
a = math.acos(g1 - g2)
print(x)
