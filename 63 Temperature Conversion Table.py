#63: Temperature Conversion Table
print("Degree Celsius",end="    ")
print("Degree Fahrenheit")
a=[0,10,20,30,40,50,60,70,80,90,100]
for i in a:
    print('{:^15}'.format(i),end="   ")
    print('{:^15}'.format((i*9/5)+32))
