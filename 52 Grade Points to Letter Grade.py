#52: Grade Points to Letter Grade
a =float(input("Enter the grade point:"))
x=round(a,2)
if x == 4.0:
    print("Grade is A+")
elif 3.7<x<4.0:
    print("Grade is A")
elif 3.3<x<=3.7:
    print("Grade is A-")
elif 3.0<x<=4.0:
    print("Grade is B+")
elif 2.7<x<=3.0:
    print("Grade is B")
elif 2.3<x<=2.7:
    print("Grade is B-")
elif 2.0<x<=2.3:
    print("Grade is C+")
elif 1.7<x<=2.0:
    print("Grade is C")
elif 1.3<x<=1.7:
    print("Grade is C-")
elif 1.0<x<=1.3:
    print("Grade is D+")
elif 0<x<=1.0:
    print("Grade is D")
elif x<=0:
    print("Grade is F")
