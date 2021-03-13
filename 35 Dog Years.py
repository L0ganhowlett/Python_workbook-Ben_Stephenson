# 35 Dog Years
x = int(input("Enter the number of human years = "))
if x < 2:
    age = 10.5 * x
else:
    age = 21 + (x - 2) * 4
print("The number of dog years is = ",age)
