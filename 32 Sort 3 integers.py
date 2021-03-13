#32 Sort 3 integers
#Asking for integers.
x = int(input("Enter the number = "))
y = int(input("Enter the number = "))
z = int(input("Enter the number = "))
mn = min(x,y,z)
mx = max(x,y,z)
md = x + y + z - mn - mx
print(mn,mx,md)
