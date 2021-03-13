#43 Faces on money
#Asking for amount from user
x = int(input("Enter the amount of dollars : "))
y = ""
if x == 1:
    y = "George Washington"
elif x == 2:
    y = "Thomas Jefferson"
elif x == 5:
    y = "Abraham Lincoln"
elif x == 10:
    y = "Alexander Hamilton"
elif x == 20:
    y = "Andrew Jackson"
elif x == 50:
    y = "Ulysses S.Grant"
elif x == 100:
    y = "Benjamin Franklin"
print("The individual on note is",y)
