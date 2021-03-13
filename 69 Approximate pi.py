#69: Approximate pi
c=1
a=3
add=lambda x,y:x+y
for i in range(2,31,2):
    if c%2==0:
        y=-4/(i*(i+1)*(i+2))
    else:
        y=4/(i*(i+1)*(i+2))
    c+=1
    a=add(a,y)
    print("The value of pi:",a)
