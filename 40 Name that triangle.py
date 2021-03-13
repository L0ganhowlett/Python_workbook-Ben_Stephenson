#40 Name of the triangle.
#Asking for the lengths of sides of triangle.
a = int(input("Enter the length of the first side = "))
b = int(input("Enter the length of side second side = "))
c = int(input("Enter the length of third side = "))
if a == c and b == c:
    print("Triangle is an equilateral triangle")
elif a == b or b == c or a == c:
    print("Triangle is an isoceles triangle")
elif a != b and b != c and c != a:
    print("Triangle is an scalene triangle")
