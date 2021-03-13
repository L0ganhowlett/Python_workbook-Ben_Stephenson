#51 Letter Grade to Grade Points
a = input("Enter the Grade:")
if a == "A+" or a == "A":
    print("Grade points are 4.0")
elif a == "A-":
    print("Grade points are 3.7")
elif a == "B+":
    print("Grade points are 3.3")
elif a == "B":
    print("Grade points are 3.0")
elif a == "B-":
    print("Grade points are 2.7")
elif a == "C+":
    print("Grade points are 2.3")
elif a == "C":
    print("Grade points are 2.0")
elif a == "C-":
    print("Grade points are 1.7")
elif a == "D+":
    print("Grade points are 1.3")
elif a == "D":
    print("Grade points are 1.0")
elif a == "F":
    print("Grade points are 0")
else:
    print("Please enter an appropriate grade")

