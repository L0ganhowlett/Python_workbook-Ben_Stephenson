#65: Compute the Perimeter of a Polygon
import math
dist=lambda x,y,w,z:float(math.sqrt(((w-x)**2)+((z-y)**2)))
perimeter=0.0
x=input("Enter the x-coordinate:")
y=input("Enter the y-coordinate:")
w=x
z=y
while x!="":
    a=x
    b=y
    x=input("Enter the x-coordinate:")
    y=input("Enter the y-coordinate:")
    if x!="":
        perimeter+=dist(float(x),float(y),float(a),float(b))
    else:
        perimeter+=dist(float(a),float(b),float(w),float(z))
print("Perimeter:",perimeter)
