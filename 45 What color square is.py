#45 What color is square ?
# Asking for number and letter
x = input("Enter the letter : ")
y = int(input("Enter the number : "))
#Assuming a1 as black
if x == "a" or x == "c" or x == "e" or x == "g":
    if y % 2 == 0:
        z = "White"
    else:
        z = "Black"
if x == "b" or x == "d" or x == "f" or x == "h":
    if y % 2 == 0:
        z = "Black"
    else:
        z = "White"
print(z)
