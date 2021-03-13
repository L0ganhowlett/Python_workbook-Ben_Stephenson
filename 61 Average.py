#61: Average
count=0
a=1
summ=0
while a!=0:
    a=float(input("Enter the number:"))
    summ+=a
    count+=1
print("Average:",(summ)/(count-1))
