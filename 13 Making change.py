#13 Making Change
#Assigning the worth of cents to respective change catgories.
cents = int(input("Enter the number of Cents ="))
loonies = cents // 200
cents = cents % 200
toonies = cents // 100
cents = cents % 100
quarters = cents // 25
cents = cents % 25
dimes = cents // 10
cents = cents % 10
nickels = cents // 2
cents = cents % 2
pennies = cents // 1
cents = cents % 1
print("Required change is = ",loonies," toonies, ",toonies," loonies, ",quarters," quarters, ",dimes," dimes, ",nickels," nickels, ",pennies," pennies, ")
