# 50 Roots of a Quadratic Function
a = int(input("Enter the value of a :"))
b = int(input("Enter the value of b :"))
c = int(input("Enter the value of c :"))
import math
x = (b**2 - 4*a*c)
if x > 0:
    y = math.sqrt(x)
    r1 = (-b + y)/(2*a)
    r2 = (-b - y)/(2*a)
    print("The roots of the quadratic equation are real and their values are  ",r1," and ",r2," respectively")
elif x == 0:
    r1 = (-b)/(2*a)
    print("The root of the quadratic equation is real and equal  and its  values is ",r1)
elif x < 0:
    print("The quadratic equation has imaginary roots")
    
