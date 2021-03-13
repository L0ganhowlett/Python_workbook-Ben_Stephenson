#33 Day old Bread
#Asking for number of day old breads.
x = int(input("Enter the number of loaves of day old breads = "))
#Cost of a fresh loaf of bread = $3.49
cp = 3.49
tp = x * 3.49
dp = x * 2.094
y = tp - dp
print("The regular price is = ",cp)
print("The total price is = ",tp)
print("The discounted price is = ",y)
