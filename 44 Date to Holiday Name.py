#44 Date of holiday.
#Asking for month and day from user.
x = input("Enter month name : ")
y = int(input("Enter the day : "))
z = ""
if x == "January" and y == 1:
    z = "New year's day"
elif x == "July" and y == 1:
    z = "Canada day"
elif x == "December" and y == 25:
    z = "Christmas day"
else:
    z = "The entered month and day do not correspond to a fixed-date holiday"
print(z)
