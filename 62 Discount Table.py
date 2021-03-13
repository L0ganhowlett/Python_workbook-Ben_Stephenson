#62: Discount Table
print("Original prices",end="   ")
print("Discounted price",end="  ")
print("New price")
a=[4.95,9.95,14.95,19.95,24.95]
for i in a:
    print('{:^15}'.format(i),end="  ")
    print('{:^20}'.format(round(i*0.4,2)),end=" ")
    print('{:^5}'.format(round(i*0.6,2)))
