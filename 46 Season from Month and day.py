#46 Season from Month And Day
#Aasking for Name of month and day
x = input("Enter the name of month : ")
y = int(input("Enter the day : "))
if x == "January" or x == "February":
    z = "Winter"
elif x == "March" :
    if y < 20:
        z = "Winter"
    elif y == 20:
        z = "Spring"
    else:
        z = "Spring"
elif x == "April" or x == "May":
    z = "Spring"
elif x == "June":
    if y < 21:
        z = "Spring"
    elif y == 21:
        z = "Summer"
    else:
        z = "Summer" 
elif x == "July" or x == "August":
    z = "Summer"
elif x == "September":
    if y < 22:
        z = "Summer"
    elif y == 22:
        z = "Fall"
    else:
        z = "Fall" 
elif x == "October" or x == "November":
    z = "Fall"
elif x == "December":
    if y < 21:
        z = "Fall"
    elif y == 21:
        z = "Winter"
    else:
        z = "Winter"
print("The season is ",z) 
    
