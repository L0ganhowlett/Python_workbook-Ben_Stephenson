#38 Month name to number of days
#Asking for name of the month
x = str(input("Enter the name of month : "))
if x == "January" or x == "March" or x == "May" or x == "July" or x == "August" or x == "October" or x == "December":
    print("The month has 31 days.")
elif x == "February":
     y = input("Is it a leap year? please enter Yes or no: ")
     if y == "Yes":    
       print("The month has 29 days.")
     elif y == "No":
         print("The month has 28 days.")
    
else:
    print("The month has 30 days.")
    
