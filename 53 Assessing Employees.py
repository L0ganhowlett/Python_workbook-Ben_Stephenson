#53: Assessing Employees
a=float(input("Enter the rating of the employee: "))
if a==0.0:
    print("Unacceptale perfotmance")
    r = 2400*a
    print("Raise:",r)
elif a==0.4:
    print("Acceptable performance")
    r = 2400*a
    print("Raise:",r)
elif a>=0.6:
    print("Meritorius performance")
    r = 2400*a
    print("Raise:",r)
else:
    raise Exception("Sorry invalid rating entered")
