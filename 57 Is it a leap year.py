#57: Is it a Leap Year?
a=int(input("Enter the year:"))
if a%400==0:
    x=True
elif a%100==0:
    x=False
elif a%4==0:
    x=True
else:
    x=False
if x:
    print("It is leap year")
else:
    print("It is not a leap year.")
