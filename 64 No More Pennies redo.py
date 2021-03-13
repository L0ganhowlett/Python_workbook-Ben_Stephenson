#64: No More Pennies
sum=0
x=input("Enter price:")
while x!="":
    sum+=float(x)
    x=input("Enter price:")
print("Total:%.2f"%sum)
y=sum*100%5
if y<2.5:
    z=sum-y/100
else:
    z=sum+0.05-y/100
print("Total payable:%.2f"%z)


    
