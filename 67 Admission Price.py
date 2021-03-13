#67: Admission Price
add=lambda x,y:x+y
b=0
while True:
    a=input("Enter the age:")
    if a=="":
        break
    if 3<=int(a)<=12:
        b=add(b,14)
    elif int(a)>=65:
        b=add(b,18)
    elif 12<int(a)<65:
        b=add(b,23)
print("The total cost:%.2f"%b)
        
